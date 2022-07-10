// request.js
/*
 对axios进行二次封装 请求拦截器增加token 响应拦截器处理大数据
*/
import store from '@/store/index'
import axios from 'axios'
import { setItem, getItem, removeitem } from '@/utils/storage'
/*
自定义写法：const xxx = axios.create({}) 一个项目中可能有不同的服务器基础地址 就要用自定义写法设置不同的服务器基础地址
*/
const instance = axios.create({ baseURL: 'http://127.0.0.1:8000' })
// 在instance(这是上面定义的自定义axios请求名称)上添加请求拦截器 补充请求头token信息
// 请求拦截器
instance.interceptors.request.use(
  config => {
    const token = store.state.token
    if (token) {
      config.headers.Authorization = `JWT ${token}`
      return config
    }
  },
  err => {
    return Promise.reject(err)
  }
)
// 响应拦截器
/* instance.interceptors.request.use(
  response => {
  // 删除token
    if (response.data.code === 404) {
      removeitem('token')
      window.open('/oauth/login', '_blank')
    } else if (response.data.token) {
      getItem('token', response.data.token)
    }
    return response
  }, err => {
    return Promise.reject(err)
  }
) */
export default instance
