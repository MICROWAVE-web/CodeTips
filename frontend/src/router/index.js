import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SearchView from "../views/SearchView.vue"
import DetailView from "../views/DetailView.vue";


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/home',
            name: 'home',
            component: HomeView,
            meta: {
                title: 'Home'
            }
        },
        {
            path: '/search',
            name: 'search',
            component: SearchView,
            meta: {
                title: 'Search'
            }
        },
        {
            path: '/tip/:TipHash',
            name: 'detail',
            component: DetailView,
            meta: {
                title: 'Detail'
            }
        },
    ]
})
router.beforeEach((to, from, next) => {
    document.title = to.meta.title;
    next();
})


export default router
