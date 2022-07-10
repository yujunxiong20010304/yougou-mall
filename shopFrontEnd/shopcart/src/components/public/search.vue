<template>
  <div id="main">
    <div id="content">
      <ul class="logo">
        <li>
          <router-link :to="{name: 'Home'}">
            <span>优购</span>
            <span>yougou</span>
          </router-link>
        </li>
        <li><i class="iconfont icon">&#xeba1;</i>100% 正品</li>
        <li><i class="iconfont icon">&#xe673;</i>免邮</li>
        <li><i class="iconfont icon">&#xe71f;</i>退换无忧</li>
      </ul>

      <div class="search">
        <div>
          <span class="iconfont" style="font-size: 25px;color: #DBDADA;font-weight: bold;">&#xe64e;</span>
          <input type="text" name="search" placeholder="搜索商品" autocomplete="off" v-model="value"/>
          <button @click="SearchShop">搜索</button>
        </div>
        <ul>
          <li>潮洪激</li>
          <li>伏肤套装</li>
          <li>女式T袖</li>
          <li>耐克Nike</li>
        </ul>
      </div>
      <el-badge :value="num" class="item" :max="10">
        <el-button @click="showCart">
          <div class="shop-cart">
            <span class="iconfont one">&#xe899;</span>
            <span>购物车</span>
          </div>
        </el-button>
      </el-badge>
    </div>
  </div>
</template>

<script>
export default {
  name: 'search',
  data () {
    return {
      value: '',
      num: 0
    }
  },
  methods: {
    showCart () {
      this.$router.push({
        path: '/user/shopcart'
      })
    },
    SearchShop () {
      this.$router.push({
        path: '/search',
        query: {
          search: this.value,
          rule: 1,
          price: 0,
          sales: 0,
          index: 1
        }
      })
    },
    getShoppingInfo () {
      this.$https.post('store/shopping/').then(res => {
        if (res.data.code === 200) {
          this.num = res.data.data.shop_info[0].num
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.value = this.$route.query.search
    this.getShoppingInfo()
  }
}
</script>

<style scoped lang="less">
#main {
  width: 100%;
  height: 100px;
  #content {
    max-width: 1000px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    height: 100px;
    align-items: center;
    .logo {
      display: flex;
      align-items: center;
      li:first-child {
        display: flex;
        flex-direction: column;
        height: 70px;
        justify-content: space-between;
        align-items: center;
        a {
          display: flex;
          flex-direction: column;
          height: 70px;
          justify-content: space-between;
          align-items: center;
          text-decoration: none;
          color: #01BEFF;
          span:first-child {
          font-size: 42px;
          }
          span {
            font-size: 12px;
            height: 20px;
          }
        }
      }
      li {
        font-size: 14px;
        display: flex;
        align-items: center;
        margin-right: 20px;
        .icon {
          font-size: 20px;
        }
      }
    }
    .search {
      div {
        display: flex;
        justify-content: center;
        input {
          width: 270px;
          height: 38px;
          border: 1px solid #FF3701;
          border-left: 0;
          outline: none;
          font-style: normal;
          font-weight: normal;
          font-stretch: normal;
          font-size: 14px;
          line-height: 38px;
          background-color: #fff;
        }
        span {
          border: 1px solid #FF3701;
          border-right: 0;
          height: 38px;
          width: 45px;
          text-align: center;
          line-height: 38px;
          border-bottom-left-radius: 3px;
          border-top-left-radius: 3px;
        }
        button {
          border: 0;
          width: 100px;
          height: 38px;
          background: linear-gradient(to right, #FF3701, #FF0B01);
          color: white;
          border-bottom-right-radius: 3px;
          border-top-right-radius: 3px;
        }
      }
      ul {
        display: flex;
        font-size: 12px;
        color: #999;
        padding: 0;
        margin: 5px 0 0 0;
        li {
          position: relative;
          padding: 0 7px;
          cursor: pointer;
          &:hover {
            color: #409EFF;
          }
          &:after {
            content: '|';
            position: absolute;
            right: 0;
          }
        }
      }
    }
  }
}
:deep(.el-button) {
  width: 115px;
  height: 38px;
  margin-bottom: 26px;
}
.shop-cart {
  display: flex;
  align-items: center;
  .one {
    font-size: 21px;
    margin-right: 4px;
  }
}
:deep(.el-badge__content.is-fixed) {
  right: calc(5px + var(--el-badge-size)/ 2);
}
</style>
