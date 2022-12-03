import Vue from 'vue'
import App from './App.vue'
import Router from "@/router";
//引入vuex
// import store from "@/store"
//引入vue-router
import VueRouter from "vue-router";
import ElementUI from 'element-ui';
import Vuetify from "vuetify";
import 'element-ui/lib/theme-chalk/index.css';
import axios from "axios";
import vuetify from './plugins/vuetify'
Vue.use(ElementUI)
Vue.use(Vuetify)

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.prototype.$axios = axios;

new Vue({
  el: "#app",
  render: h => h(App),
  router: Router,
  vuetify,
  beforeCreate() {
    Vue.prototype.$bus = this //安装全局事件总线（任意组件间通信）
  }
})
