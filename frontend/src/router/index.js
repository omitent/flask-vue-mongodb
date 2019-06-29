import Vue from 'vue'
import Router from 'vue-router'
import VueCookie from 'vue-cookie'
import Home from '@/components/Home'
import NotFound from '@/components/NotFound'
import Login from '@/components/Login'
import Logout from '@/components/Logout'
import Register from '@/components/Register'
import Profile from '@/components/Profile'
import Count from '@/components/Count'
import Results from '@/components/Results'
import About from '@/components/About'
import Contact from '@/components/Contact'

Vue.use(Router)
Vue.use(VueCookie)

let router = new Router({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: Home },
        { path: '/login', name: 'login', component: Login },
        { path: '/logout', name: 'logout', component: Logout },
        { path: '/register', name: 'register', component: Register },
        { path: '/profile', name: 'profile', component: Profile },
        { path: '/count', name: 'count', component: Count },
        { path: '/results', name: 'results', component: Results },
        { path: '/about', name: 'about', component: About },
        { path: '/contact', name: 'contact', component: Contact },
        { path: '*', component: NotFound}
    ]
})

router.beforeEach((to, from, next) => {
    const authPages = ['/profile', '/count', '/results']
    const authRequired = authPages.includes(to.path)
    const loggedIn = Vue.cookie.get('user')

    if (authRequired && !loggedIn) {
        return next('/login')
    }

    next()
})

export default router