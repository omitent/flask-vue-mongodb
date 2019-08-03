import Vue from 'vue'
import VueCookie from 'vue-cookie'
import Vuetify from 'vuetify'

Vue.use(VueCookie)
Vue.use(Vuetify)

import App from './App.vue'
import { store } from './store'
import router from './router'
import Axios from 'axios'

import 'vuetify/dist/vuetify.min.css'

const axios = Axios.create({
  baseURL: process.env.VUE_APP_API_URL || '/'
})
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify: new Vuetify(),
  render: h => h(App),
}).$mount('#app')
