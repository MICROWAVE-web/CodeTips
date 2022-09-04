<template>
  <!DOCTYPE html>
  <html lang="en">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>SearchPage</title>
  </head>

  <body>
  <HeaderComp/>
  <div class="m-3 p-3" style="min-height: 100vh;">
    <div class="row justify-content-center ">
      <div class="col-sm-2 card rounded-30 bg-white mt-3"
           style="height: fit-content; padding: 0 0 0 0; min-width: 190px;">

        <div class="p-4 rounded">
          <label class="control-label mb-3 fw-bold">Sort by:</label>
          <select class="form-select" aria-label="Default select example" @change="ChangeSortType">
            <option value="default" selected>Choose type of sorting</option>
            <option value="r-up">Rating Up</option>
            <option value="r-down">Rating Down</option>
            <option value="dt-up">Newest</option>
            <option value="dt-down">Oldest</option>

          </select>
        </div>

        <div class="p-4 border-top">
          <label class="control-label mb-3 fw-bold">Add tag:</label>
          <div class="input-group mb-3" style="width: auto;">
            <input type="text" id="new_tag_input" class="form-control" placeholder="Some tag"
                   aria-label="Recipient's username" aria-describedby="basic-addon2">
            <button class="input-group-text" id="basic-addon2" @click="AddTag">Add</button>
          </div>
          <div class='m-3 text-danger fw-bolder' v-if="Errors.TagsErrorMsg">{{ Errors.TagsErrorMsg }}</div>
          <ul class="list-group" style="overflow: auto; max-height: 200px;">
            <li v-for="(item, index) in tags">
              <div class="input-group mb-3" style="width: auto;">
                <input type="text" class="form-control no-mouse" style="outline: none;" :value="item"
                       aria-label="Recipient's username" :aria-describedby="'basic-addon' + index" readonly>
                <button class="input-group-text" style="background-color: #de5656; color: white;"
                        :id="'basic-addon' +index" @click="PopTag(index)">Delete
                </button>
              </div>
            </li>
          </ul>
        </div>

        <div class="p-4 border-top">
          <label class="control-label mb-3 fw-bold">With rating more then:</label>
          <input type="range" class="form-range" min="-10" max="10" step="1" id="customRange3" v-model="MinRating"
                 @change="SetMinimumOfRating">
          <div class='text-success'
               style="display: flex!important;align-items: center;justify-content: center;align-content: center;flex-direction: row;"
               v-if="MinRating>0">
            <div style="color: black;">More than</div> &nbsp;{{ MinRating }}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                 class="bi bi-chevron-double-up" viewBox="0 0 16 16">
              <path fill-rule="evenodd"
                    d="M7.646 2.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 3.707 2.354 9.354a.5.5 0 1 1-.708-.708l6-6z"/>
              <path fill-rule="evenodd"
                    d="M7.646 6.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 7.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z"/>
            </svg>&nbsp;of rating
          </div>

          <div class='text-danger '
               style="display: flex!important;align-items: center;justify-content: center;align-content: center;flex-direction: row;"
               v-else-if="MinRating<0">
            <div style="color: black;">More than</div>
            &nbsp;{{ MinRating }}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                 class="bi bi-chevron-double-down" viewBox="0 0 16 16">
              <path fill-rule="evenodd"
                    d="M1.646 6.646a.5.5 0 0 1 .708 0L8 12.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
              <path fill-rule="evenodd"
                    d="M1.646 2.646a.5.5 0 0 1 .708 0L8 8.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
            </svg>&nbsp;of rating
          </div>
          <div v-else style="display: flex!important;
    align-items: center;
    justify-content: center;
    align-content: center;
    flex-direction: row;">Any Rating
          </div>
        </div>
      </div>

      <div class="col-sm-6">
        <div class="input-group m-3" style="width: auto;">
          <input type="text" id="keywords_input" class="form-control" placeholder="Some keywords"
                 aria-label="Recipient's username" aria-describedby="basic-addon3" @change="SetKeyword"
                 @keyup.enter="GetTips" autocomplete="off">
          <button class="input-group-text btn btn-primary" id="basic-addon3" @click="GetTips">Go!</button>
        </div>

        <div class="card m-3" v-for="tip in Tips">
          <h5 class="card-header">{{ tip.heading }}</h5>
          <div class="card-body">
            <!--<h5 class="card-title">Special title treatment</h5> -->
            <p class="card-text">{{ tip.description }}</p>
            <div class="container" style="font-size: 12px;">
              <div class="row justify-content-end">
                <div v-if="tip.tags.length>0" class='text-secondary col col-lg-2'
                     style="margin: 10px 0 10px 0; display: flex;">
                  Tags:&nbsp;
                  <div v-for="index in 5" :key="index">
                    <div v-if="tip.tags[index-1]">
                      {{ tip.tags[index - 1].name }}&nbsp;
                    </div>
                  </div>
                </div>

                <div v-if="tip.dateCreated" style="margin: 10px 0 10px 0" class='col col-lg-3 d-flex text-secondary'>
                  Date of creation {{ tip.dateCreated.split('T')[0] }}
                  {{ tip.dateCreated.split('T')[1].split('.')[0].split(':').slice(0, 2).join(':') }}
                </div>

                <div v-if="tip.dateModified" style="margin: 10px 0 10px 0" class='col col-lg-3 d-flex text-secondary'>
                  Modified date {{ tip.dateModified.split('T')[0] }}
                  {{ tip.dateModified.split('T')[1].split('.')[0].split(':').slice(0, 2).join(':') }}
                </div>

              </div>
            </div>
            <button @click="GoToTip(tip.urlHash)" class="btn btn-primary">Go to tip</button>
          </div>
        </div>

      </div>
    </div>
  </div>

  <footer class="text-center bg-dark">
    <div class="container text-white py-4 py-lg-5">
      <ul class="list-inline">
        <li class="list-inline-item me-4"><a class="link-light" href="#">Web design</a></li>
        <li class="list-inline-item me-4"><a class="link-light" href="#">Development</a></li>
        <li class="list-inline-item"><a class="link-light" href="#">Hosting</a></li>
      </ul>
      <ul class="list-inline">
        <li class="list-inline-item me-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
               class="bi bi-facebook text-light">
            <path
                d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"></path>
          </svg>
        </li>
        <li class="list-inline-item me-4">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
               class="bi bi-twitter text-light">
            <path
                d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"></path>
          </svg>
        </li>
        <li class="list-inline-item">
          <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" viewBox="0 0 16 16"
               class="bi bi-instagram text-light">
            <path
                d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"></path>
          </svg>
        </li>
      </ul>
      <p class="text-muted mb-0">Copyright © 2022 Brand</p>
    </div>
  </footer>
  </body>

  </html>
</template>

<script>
import {ref} from "vue";
import ApolloClient, {InMemoryCache} from "apollo-boost";
import {provideApolloClient, useQuery} from "@vue/apollo-composable";
import gql from "graphql-tag";
import {computed, watch} from "vue";

import "../assets/searchpage/bootstrap/css/bootstrap.min.css"
import "../assets/searchpage/css/Navbar-Right-Links-Dark.css"
import "../assets/searchpage/css/styles.css"
import HeaderComp from "../components/HeaderComp.vue";

export default {
  name: "SearchView",
  components: {
    HeaderComp
  },
  data() {
    return {
      preset_keywords: this.$route.params.keywords,
      keywords: '',
      sort_by: '',
      tags: [],
      MinRating: 0,
      Errors: {
        TagsErrorMsg: ''
      },
      Tips: []
    }
  },
  watch: {
    preset_keywords() {
      console.log('Изменился пресет keywords: ' + this.preset_keywords)
      this.GetTips()
    },
    sort_by() {
      console.log('Изменилась сортировка: ' + this.sort_by)
      this.GetTips()
    },
    tags() {
      console.log('Изменились теги: ' + this.tags)
      this.GetTips()
    },
    MinRating() {
      console.log('Изменился мин рейтинг: ' + this.MinRating)
      this.GetTips()
    },
  },
  mounted() {
    let recaptchaScript = document.createElement('script')
    recaptchaScript.setAttribute('src', 'https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js')
    document.head.appendChild(recaptchaScript)
    if (this.preset_keywords !== '' && this.preset_keywords) {
      document.getElementById('keywords_input').value = this.preset_keywords
      this.keywords = this.preset_keywords
    }
    this.GetTips()
  },
  methods: {
    SetMinimumOfRating(event) {
      this.MinRating = event.target.value
    },
    AddTag(event) {
      this.Errors.TagsErrorMsg = ''
      if (this.tags.length >= 10) {
        this.Errors.TagsErrorMsg = 'Max tags length is 10'
        return
      }
      let new_tag = document.getElementById('new_tag_input').value
      if (new_tag !== '' && !this.tags.includes(new_tag)) {
        this.tags.push(new_tag)
        this.tags = this.tags.filter((num, index) => index !== 999)
      }
    },
    PopTag(indexToDelete) {
      this.Errors.TagsErrorMsg = ''
      this.tags = this.tags.filter((num, index) => index !== indexToDelete)
    },
    ChangeSortType(event) {
      this.sort_by = event.target.value
    },
    SetKeyword(event) {
      this.keywords = event.target.value
    },
    GoToTip(tip) {
      this.$router.push({
        name: 'detail',
        params: {
          TipHash: tip,
        }
      });
    },
    GetTips() {
      const cache = new InMemoryCache()
      const apolloClient = new ApolloClient({
        cache,
        uri: 'http://localhost:8000/blog/graphql',
      })
      provideApolloClient(apolloClient);

      const SEARCH_QUERY = gql`
         query tipsByManyConditions{
            tipsByManyConditions(
                keyword: "${this.keywords}"
                sort: "${this.sort_by}"
                tags: ${'["' + this.tags.join('", "') + '"]'}
                rating: ${this.MinRating}
                ) {
            heading
            description
            code
            dateCreated
            dateModified
            tags {
              name
              icon
            }
            urlHash
          }
          }
        `

      const {result, loading, onError, onResult} = useQuery(SEARCH_QUERY)
      this.Tips = computed(() => result.value?.tipsByManyConditions ?? [])
    }
  }
}
</script>

<style scoped>
.no-mouse {
  pointer-events: none;
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome/Safari/Opera */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none;
}

body, html {
  background-color: #f6f6f6;
}

input[type="text"], textarea {
  outline: none;
  box-shadow: none !important;
}

</style>