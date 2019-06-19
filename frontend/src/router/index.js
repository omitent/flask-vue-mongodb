import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Logout from '@/components/Logout'
import Register from '@/components/Register'
import UserProfile from '@/components/UserProfile'

Vue.use(Router)

let router = new Router({
    mode: 'history',
    routes: [
        { path: '/', name: 'home', component: Home },
        { path: '/login', name: 'login', component: Login },
        { path: '/logout', name: 'logout', component: Logout },
        { path: '/register', name: 'register', component: Register },
        { path: '/user', name: 'user', component: UserProfile },
        { path: '*', component: Home}
    ]
})

router.beforeEach((to, from, next) => {
    const publicPages = ['/', '/login', '/register']
    const authRequired = !publicPages.includes(to.path)
    const loggedIn = localStorage.getItem('user')

    if (authRequired && !loggedIn) {
        return next('/login')
    }

    next()
})

export default router