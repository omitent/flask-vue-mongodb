import router from '../router'
import { userServices } from '../services'

const user = JSON.parse(localStorage.getItem('user'))
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
                    router.push('/')
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
                    router.push('/')
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