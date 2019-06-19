import Axios from 'axios'

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
            alert('Username already exists!')
            return Promise.reject()
        }
        if (resp.data.user) {
            localStorage.setItem('user', JSON.stringify(resp.data.user))
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
            localStorage.setItem('user', JSON.stringify(resp.data.user))
        }
        return resp.data.user
    })
    .catch(error => {
        return Promise.reject(error)
    })
}

function logout() {
    localStorage.removeItem('user')
}

function handleResponse(response) {
    return response.json().then(data => {
        console.log(data)
        if (!response.ok) {
            if (response.status === 401) {
                logout()
                location.reload(true)
            }
            const error = (data && data.message) || response.statusText
            return Promise.reject(error)
        }
        return data
    })
}