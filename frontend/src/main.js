import { createApp, provide, h } from "vue"
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
import ApolloClient, {InMemoryCache} from 'apollo-boost'
import VueApollo from 'vue-apollo'
import { DefaultApolloClient } from "@vue/apollo-composable"
import "./assets/detailpage/highlight.js/styles/solarized_dark.css"

const cache = new InMemoryCache()


const apolloClient = new ApolloClient({
  cache,
  uri: 'http://localhost:8000/blog/graphql',
})


 const app = createApp({
     setup() {
         provide(DefaultApolloClient, apolloClient)
     },
     render: () => h(App),
 })

app.use(router)
app.mount('#app')
