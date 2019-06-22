import Vue from 'vue'
import VueCookie from 'vue-cookie'
import router from '../router'
import { userServices } from '../services'

Vue.use(VueCookie)

const user = JSON.parse(Vue.cookie.get('user'))
const initialState = user 
    ? { userStatus: { loggedIn: true}, user }
    : { userStatus: {}, user: { username: null }}

export const auth = {
    namespaced: true,
    state: initialState,
    mutations: {
        loginRequest: (state, user) => {
            state.userStatus = { loggingIn: true }
            state.user = user
        },
        loginSuccess: (state, user) => {
            state.userStatus = { loggedIn: true }
            state.user = user
        },
        loginFailure: (state) => {
            state.userStatus = {}
            state.user = null
        },
        logout: (state) => {
            state.userStatus = {}
            state.user = null
        }
    },
    actions: {
        register: ({ dispatch, commit }, { username, password}) => {
            commit('loginRequest', { username })
            userServices.register(username, password)
            .then(
                user => {
                    commit('loginSuccess', user)
                    router.push('/profile')
                },
                error => {
                    commit('loginFailure', error)
                    alert('Login failed!')
                }
            )
        },
        login: ({ dispatch, commit }, { username, password }) => {
            commit('loginRequest', { username })
            userServices.login(username, password)
            .then(
                user => {
                    commit('loginSuccess', user)
                    router.push('/profile')
                },
                error => {
                    commit('loginFailure', error)
                    alert('Invalid username and/or password!')
                }
            )
        },
        logout: ({ commit }) => {
            commit('logout')
            userServices.logout()
        }
    }
}