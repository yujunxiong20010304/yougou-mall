<template>
  <div id="commodity-category">
    <div class="brand">
      <span>品牌</span>
      <div class="content">
        <ul ref="brand">
          <li v-for="(item, index) in brand_list" :key="index" @click="choiceBrand(index)" :class="[brand===index?'brand-aim':'']">{{item}}</li>
        </ul>
      </div>
      <span class="more" @click="ShowAll" v-if="show">更多<i class="iconfont">&#xe62b;</i></span>
      <span class="more" @click="HideAll" v-else>收起<i class="iconfont">&#xeb9c;</i></span>
    </div>
    <div class="range">
      <div class="section">
        <div :class="[aim===1?'active':'', 'r1']" @click="changeSort(1)">
          <span>价格</span>
          <div>
            <i class="iconfont" v-if="increase_decrease.price===1||aim===0">&#xeb9c;</i>
            <i class="iconfont" v-if="increase_decrease.price===0||aim===0">&#xe62b;</i>
          </div>
        </div>
        <div :class="[aim===0?'active':'', 'r1']" @click="changeSort(0)">
          <span>销量</span>
          <div>
            <i class="iconfont" v-if="increase_decrease.sales===1||aim===1">&#xeb9c;</i>
            <i class="iconfont" v-if="increase_decrease.sales===0||aim===1">&#xe62b;</i>
          </div>
        </div>
        <span class="price-range" ref="price">
          <input type="text" v-model="min_price" placeholder="¥" @focus="obtain" @blur="lose"/> - <input type="text" v-model="max_price" placeholder="¥" @focus="obtain" @blur="lose"/>
          <span ref="sure" @mousedown="PriceRange">确定</span>
        </span>
      </div>
      <div class="page-turn">
        <div><i>1</i>/<span>19</span></div>
        <div><span class="iconfont">&#xeb9b;</span><span class="iconfont">下一页&#xe62e;</span></div>
      </div>
    </div>
  </div>
</template>

<script>

import emitter from '@/utils/event'

export default {
  name: 'CommodityCategory',
  data () {
    return {
      aim: 1, // 价格或是销量
      show: 1, // 展开与收起
      increase_decrease: {
        price: 0,
        sales: 0
      },
      brand_list: [],
      brand: '',
      min_price: '',
      max_price: ''
    }
  },
  methods: {
    // 品排选择
    choiceBrand (index) {
      if (this.brand === index) {
        this.brand = ''
        this.$router.push({
          path: '/search',
          query: {
            search: this.$route.query.search,
            rule: this.aim,
            price: this.increase_decrease.price,
            sales: this.increase_decrease.sales,
            index: 1,
            min_price: this.$route.query.min_price,
            max_price: this.$route.query.max_price
          }
        })
      } else {
        this.brand = index
        this.$router.push({
          path: '/search',
          query: {
            search: this.$route.query.search,
            brand: this.brand_list[index],
            rule: this.aim,
            price: this.increase_decrease.price,
            sales: this.increase_decrease.sales,
            index: 1,
            min_price: this.$route.query.min_price,
            max_price: this.$route.query.max_price
          }
        })
      }
    },
    async getSearchShop () {
      const { data: res } = await this.$http.post('store/brands/', { search: this.$route.query.search })
      console.log(res)
      if (res.code === 200) {
        emitter.emit('err', { aim: 1 })
        this.brand_list = res.data
        if (this.$route.query.brand) {
          for (let i = 0; this.brand_list.length > i; i++) {
            if (this.$route.query.brand === this.brand_list[i]) {
              this.brand = i
            }
          }
        }
      } else {
        // 返回错误信息
        emitter.emit('err', { aim: 0 })
      }
    },
    changeSort (aim) {
      if (aim === this.aim) {
        if (this.increase_decrease.price === 0) {
          this.increase_decrease.price = 1
        } else {
          this.increase_decrease.price = 0
        }
        if (this.increase_decrease.sales === 0) {
          this.increase_decrease.sales = 1
        } else {
          this.increase_decrease.sales = 0
        }
      }
      this.aim = aim
      this.$router.push({
        path: '/search',
        query: {
          search: this.$route.query.search,
          brand: this.brand_list[this.brand],
          rule: this.aim,
          price: this.increase_decrease.price,
          sales: this.increase_decrease.sales,
          index: 1,
          min_price: this.$route.query.min_price,
          max_price: this.$route.query.max_price
        }
      })
    },
    obtain () {
      this.$refs.price.style = 'background-color: #fff;box-shadow:0 15px 35px rgba(0,0,0,0.02),0 3px 10px rgba(0,0,0,0.02);'
      this.$refs.sure.style = 'display: inline-block;'
    },
    PriceRange () {
      this.$router.push({
        path: '/search',
        query: {
          search: this.$route.query.search,
          brand: this.brand_list[this.brand],
          rule: this.aim,
          price: this.increase_decrease.price,
          sales: this.increase_decrease.sales,
          index: 1,
          min_price: this.min_price,
          max_price: this.max_price
        }
      })
    },
    lose () {
      this.$refs.price.style = 'background-color: #F5F5F5;box-shadow: none;'
      this.$refs.sure.style = 'display: none;'
    },
    ShowAll () {
      this.show = 0
      this.$refs.brand.style = 'height: auto;'
    },
    HideAll () {
      this.show = 1
      this.$refs.brand.style = 'height: 94px;'
    }
  },
  watch: {
    '$route.query.search': {
      handler (newVal, oldVal) {
        this.getSearchShop()
        this.brand = ''
      }
    }
  },
  created () {
    this.aim = parseInt(this.$route.query.rule)
    this.increase_decrease.price = parseInt(this.$route.query.price)
    this.increase_decrease.sales = parseInt(this.$route.query.sales)

    if (parseInt(this.$route.query.max_price)) {
      this.max_price = parseInt(this.$route.query.max_price)
    }
    if (parseInt(this.$route.query.min_price)) {
      this.min_price = parseInt(this.$route.query.min_price)
    }
    this.getSearchShop()
  }
}
</script>

<style scoped lang="less">
#commodity-category {
  width: 1190px;
  margin: 0 auto;
  user-select: none;
  .brand {
    display: flex;
    justify-content: flex-start;
    border: 1px solid #D8D8D8;
    span {
      width: 118px;
      text-align: left;
      padding: 16px 0 16px 20px;
      font-size: 14px;
      font-weight: 400;
      color: #666;
    }
    .more {
      cursor: pointer;
      i {
        font-size: 12px;
        margin-left: 5px;
      }
    }
    .content {
      max-height: 397px;
      overflow-y: auto;
    }
    ul {
      display: flex;
      padding: 16px 0;
      margin-bottom: 0;
      width: 951px;
      flex-wrap: wrap;
      justify-content: flex-start;
      height: 94px;
      overflow: hidden;
      li {
        width: 155px;
        text-align: center;
        border: 1px solid #DFDFDF;
        height: 60px;
        margin: 7px 1.7px;
        cursor: pointer;
        font-weight: bold;
        line-height: 60px;
        color: #666;
        font-size: 12px;
        &:hover {
          color: #409EFF;
          border: 1px solid #409EFF;
        }
      }
      .brand-aim {
        color: #409EFF;
        border: 1px solid #409EFF;
        text-align: center;
      }
    }
  }
  .range {
    width: 100%;
    display: flex;
    justify-content: space-between;
    height: 48px;
    margin: 15px 0 25px 0;
    background-color: #F5F5F5;
    border: 1px solid #DFDFDF;
    .section {
      display: flex;
      height: 46px;
      align-items: center;
      .r1 {
        padding: 0 18px;
        font-size: 12px;
        display: flex;
        border: 1px solid #DFDFDF;
        cursor: pointer;
        span {
          height: 46px;
          line-height: 46px;
          margin-right: 7px;
        }
        div {
          display: flex;
          flex-direction: column;
          height: 46px;
          align-items: center;
          justify-content: center;
          i {
            font-size: 12px;
            height: 12px;
            line-height: 12px;
          }
        }
      }
      .active {
        border: 1px solid #409EFF;
        transition: all .7s;
        color: #409EFF;
        background-color: #F2F8FF;
      }
      .price-range {
        padding-left: 15px;
        height: 100%;
        width: 212px; // 148
        display: flex;
        align-items: center;
        input {
          width: 50px;
          height: 4px;
          padding: 9px 5px;
          border: 1px solid #e5e5e5;
          outline: none;
          font-size: 12px;
          line-height: 4px;
          box-sizing: content-box;
        }
        span {
          font-size: 12px;
          color: #fff;
          background-color: #A77BC9;
          padding: 2px 7px;
          // display: inline-block;
          border-radius: 2px;
          margin-left: 15px;
          cursor: pointer;
          display: none;
        }
      }
    }
    .page-turn{
      display: flex;
      align-items: center;
      div:first-child {
        font-size: 12px;
        color: #424141;
        margin-right: 7px;
        i {
          font-style: normal;
          color: #E0468D;
        }
      }
      div:last-child {
        .iconfont {
          font-size: 13px;
          color: #848585;
        }
        span {
          width: 54px;
          border-radius: 3px;
          padding: 5px 8px;
          border: 1px solid #DFDFDF;
          margin: 0 5px;
          cursor: pointer;
        }
      }
    }
  }
}
</style>
