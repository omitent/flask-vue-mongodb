import Vue from 'vue'
import App from './App.vue'
import { store } from './store'
import router from './router'
import Axios from 'axios'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

const axios = Axios.create({
  baseURL: process.env.VUE_APP_API_URL || '/'
})
Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
