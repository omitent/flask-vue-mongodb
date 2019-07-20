import Vue from 'vue'
import VueCookie from 'vue-cookie'
import Axios from 'axios'

Vue.use(VueCookie)

const axios = Axios.create({
    baseURL: process.env.VUE_APP_API_URL || '/'
})

export const userServices = {
    register,
    login,
    logout
}

function register(username, password) {
    return axios.post(
        '/api/register',
        {
            username: username,
            password: password
        },
        {
            headers: { 'Content-Type': 'application/json' }
        }
    )
    .then(resp => {
        if (resp.status === 202) {
            return Promise.reject('Username already exists!')
        }
        if (resp.data.user) {
            Vue.cookie.set('user', JSON.stringify(resp.data.user))
        }
        return resp.data.user
    })
    .catch(error => {
        return Promise.reject(error)
    })
}

function login(username, password) {
    return axios.post(
        '/api/auth', 
        {
            username: username,
            password: password
        },
        {
            headers: { 'Content-Type': 'application/json' }
        }
    )
    .then(resp => {
        if (resp.data.user) {
            Vue.cookie.set('user', JSON.stringify(resp.data.user))
        }
        return resp.data.user
    })
    .catch(error => {
        return Promise.reject(error)
    })
}

function logout() {
    Vue.cookie.delete('user')
}