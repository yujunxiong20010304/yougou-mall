<template>
  <all-header></all-header>
  <all-search></all-search>
  <user-evaluate :shop_info="shop_info"></user-evaluate>
  <all-tail></all-tail>
</template>

<script>
import userEvaluate from '@/components/evaluate/userEvaluate'
export default {
  name: 'Evaluate',
  components: {
    'user-evaluate': userEvaluate
  },
  data () {
    return {
      shop_info: ''
    }
  },
  methods: {
    // 验证当前的评价id是否正确
    idJudge () {
      this.$https.get('user/comment', { params: { id: this.$route.query.id } }).then(res => {
        if (res.data.code === 404) {
          this.$router.replace('/home')
        } else {
          this.shop_info = res.data.data
        }
      }).catch(err => {
        console.log(err)
        this.$router.replace('/home')
      })
    }
  },
  created () {
    this.idJudge()
  }
}
</script>

<style scoped lang="less">

</style>
