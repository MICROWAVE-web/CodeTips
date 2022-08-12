from graphene_django import DjangoObjectType

from .models import Tip, Tag
import graphene


class TipType(DjangoObjectType):
    class Meta:
        model = Tip


class TagType(DjangoObjectType):
    class Meta:
        model = Tag


class Query(graphene.ObjectType):
    all_tips = graphene.List(TipType)
    tip_by_hash = graphene.Field(TipType, url_hash=graphene.String())
    tips_by_tag = graphene.List(TipType, tag=graphene.String())

    def resolve_all_tips(self, info):
        return (
            Tip.objects.all()
        )

    def resolve_tip_by_hash(self, info, url_hash):
        return Tip.objects.objects.select_related("user").get(url_hash=url_hash)

    def resolve_tips_by_tag(self, info, url_hash):
        return Tip.objects.objects.select_related("user").get(url_hash=url_hash)


schema = graphene.Schema(query=Query)