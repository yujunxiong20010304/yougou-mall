import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import insinstance from '@/utils/request'
import JSEncrypt from 'jsencrypt'
import '@/assets/css/public.css'
// 引入自定义方法
// 引入element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css' // 创建app 实例子
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
// 引入jquery
// const $ = require('jquery')
// window.$ = $
import allHeader from '@/components/public/header' // 公共头部
import allSearch from '@/components/public/search' // 公共搜索
import allTail from '@/components/public/tail'
/* const $ = require('jquery')
window.$ = $ */
const app = createApp(App)
// 注册全局组件
app.component('all-header', allHeader)
app.component('all-search', allSearch)
app.component('all-tail', allTail)
app.config.globalProperties.$http = axios
app.config.globalProperties.$https = insinstance
app.config.globalProperties.$jsEncrypt = function (data, pubkey) {
  let encrypt = new JSEncrypt()
  encrypt.setPublicKey(pubkey)
  return encrypt.encrypt(data.toString())
}
app.config.productionTip = false
app.config.withCredentials = true
axios.defaults.baseURL = 'http://localhost:8000' // 指向后端的请求端口
// axios.defaults.xsrfCookieName = 'csrftoken'
// axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8' // 编码
app.use(store).use(router).use(ElementPlus).mount('#app')
