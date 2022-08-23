import Vue from 'vue'
import App from './App.vue'

import router from './router/index.js'
/* eslint-disable no-new */
let app = new Vue({
  el: '#app',
  router,
  render: h => h(App), 
  components: { App },
  template: '<App/>'
})