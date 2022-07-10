import { createStore } from 'vuex'
import { setItem, getItem } from '@/utils/storage'

export default createStore({
  state: {
    // 保存公共数据 在设置vuex中的初值时，先从本地存储中取，如果取不到，则初始为空
    token: getItem('token') || {},
    publicKey: {}
  },
  mutations: {
    mSetTokenInfo (state, tokenObj) {
      state.token = tokenObj // 刷新会丢失所以进行持久化 调用上面storage.js文件里setItem方法保存token
      setItem('token', tokenObj)
    },
    GetPublicKey (state, KeyObj) {
      state.publicKey = KeyObj
    }
  },
  actions: {
  },
  modules: {
  }
})
