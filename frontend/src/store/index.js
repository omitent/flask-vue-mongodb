import Vue from 'vue'
import Vuex from 'vuex'
import VueCookie from 'vue-cookie'
import { auth } from './auth.module'

Vue.use(Vuex)
Vue.use(VueCookie)

export const store = new Vuex.Store({
    modules: {
        auth
    }
})