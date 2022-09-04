from django.db.models import Q
from graphene_django import DjangoObjectType
from itertools import chain
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
    tips_by_keyword = graphene.List(TipType, keyword=graphene.String())
    tips_by_many_conditions = graphene.List(TipType, keyword=graphene.String(), sort=graphene.String(),
                                            tags=graphene.List(graphene.String), rating=graphene.Int())

    def resolve_all_tips(self, info):
        return (
            Tip.objects.all()
        )

    def resolve_tip_by_hash(self, info, url_hash):
        return Tip.objects.get(url_hash=url_hash)

    def resolve_tips_by_tag(self, info, tag):
        return Tip.objects.filter(Q(tags__name__iexact=tag.lower()))

    def resolve_tips_by_keyword(self, info, keyword):
        return (Tip.objects.filter(
            Q(heading__icontains=keyword.lower()) |
            Q(tags__name__icontains=keyword.lower())
        )).distinct()[:5]

    def resolve_tips_by_many_conditions(self, info, keyword, sort, tags, rating):
        print('-----', keyword, sort, tags, rating)
        if keyword != "":
            tips_by_keyword = Tip.objects.filter(
                Q(heading__icontains=keyword.lower()) |
                Q(description__icontains=keyword.lower()) |
                Q(tags__name__icontains=keyword.lower())
            ).distinct()
        else:
            tips_by_keyword = Tip.objects.all()
        if len(tags) > 0 and not (len(tags) == 1 and tags[0] == ""):
            tips_by_tags = chain(*[Tip.objects.filter(Q(tags__name__iexact=tag.lower())) for tag in tags])
            summary_list = list(set(tips_by_keyword).intersection(list(tips_by_tags)))
        else:
            summary_list = list(tips_by_keyword)
        all_tips = filter(lambda instance: int(instance.rating) >= int(rating), summary_list)
        output_tips = Tip.objects.filter(id__in=[tip.id for tip in list(all_tips)])
        if sort == 'r-up':
            output_tips = output_tips.order_by('-rating')
        if sort == 'r-down':
            output_tips = output_tips.order_by('rating')
        if sort == 'dt-up':
            output_tips = output_tips.order_by('-date_modified')
        if sort == 'dt-down':
            output_tips = output_tips.order_by('date_modified')
        return output_tips


schema = graphene.Schema(query=Query)
