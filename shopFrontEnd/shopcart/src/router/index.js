import { createRouter, createWebHistory } from 'vue-router'
import insinstance from '@/utils/request'
import store from '@/store/index'
import axios from 'axios'
import { setItem, getItem } from '@/utils/storage'
const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/success',
    name: 'success',
    component: () => import('@/views/state/success')
  },
  {
    path: '/payment',
    name: 'SureOrder',
    component: () => import('@/views/payment/SureOrder')
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('@/views/search/Search')
  },
  {
    path: '/user',
    name: 'user',
    redirect: '/user/yougou',
    component: () => import('@/views/user/User'),
    children: [
      { path: 'yougou', name: 'yougou', component: () => import('@/components/user/YouGou') },
      { path: 'shopcart', name: 'shopcart', component: () => import('@/components/user/ShopCart') },
      { path: 'evaluate', name: 'evaluate', component: () => import('@/components/user/ToEvaluated') },
      { path: 'payoff', name: 'payoff', component: () => import('@/components/user/OrderInformation') },
      { path: 'delivery', name: 'delivery', component: () => import('@/components/user/OrderInformation') },
      { path: 'receiving', name: 'receiving', component: () => import('@/components/user/OrderInformation') },
      { path: 'sign', name: 'sign', component: () => import('@/components/user/OrderInformation') },
      { path: 'account', name: 'account', component: () => import('@/components/user/AccountInformation') },
      { path: 'address', name: 'address', component: () => import('@/components/user/AddressInformation') }
    ]
  },
  {
    path: '/sure/payment',
    name: 'payment',
    component: () => import('@/views/payment/payment')
  },
  {
    path: '/detail',
    name: 'Detail',
    component: () => import('@/views/detail/Detail')
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('@/views/shop/Home')
  },
  {
    path: '/oauth/login',
    name: 'Login',
    component: () => import('@/views/oauth/Login')
  },
  {
    path: '/oauth/register',
    name: 'Register',
    component: () => import('@/views/oauth/Register')
  },
  {
    path: '/evaluate',
    name: 'Evaluate',
    component: () => import('@/views/evaluate/Evaluate')
  },
  {
    path: '/mutual',
    name: 'Mutual',
    component: () => import('@/views/evaluate/Mutual')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  // 页面切换后滚动到顶部
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})
router.beforeEach(async (to, from) => {
  const path = ['SureOrder', 'yougou', 'shopcart',
    'evaluate', 'payoff', 'delivery', 'sign', 'account',
    'address', 'receiving', 'payment']
  if (path.indexOf(to.name) !== -1) {
    if (typeof store.state.token !== 'string') {
      return { name: 'Login' }
    } else {
      const { data: res } = await axios.post('oauth/api/token/verify/', { token: store.state.token })
      console.log(res)
      if (res.code) {
        // token过期
        // const refreshToken = getItem('refresh')
        // const { data: res } = await axios.post('oauth/api/refresh/', { refresh: refreshToken })
        return { name: 'Login' }
        /* if (res.code) {
          return { name: 'Login' }
        } else {
          store.commit('mSetTokenInfo', res.access)
        } */
      }
    }
  }
})

export default router
