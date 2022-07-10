<!-- 购物车 -->
<template>
  <div>
    <div id="shop-cart" v-if="shop_cart.length">
    <div class="title">
      <h4>购物车（全部{{shop_num}}）</h4>
      <div class="all-price">
        <span>已选商品（不含运费）</span>
        <i>{{total_price}}.00 ¥</i>
        <div class="settlement" :style="[total_price === 0?'':'backgroundColor: #FF5001;cursor: pointer']" @click="balance">结算</div>
      </div>
    </div>
    <div class="cart-table-th">
      <div class="thm-1 box">
        <el-checkbox v-model="checked" style="font-weight: 700;color: #3c3c3c;" @change="changeSelect(1)">全选</el-checkbox>
        <span>商品信息</span>
      </div>
      <div style="width: 170px;"></div>
      <div class="thm-2 box">
        <span>单价</span>
        <span>数量</span>
        <span>金额</span>
        <span>操作</span>
      </div>
    </div>
    <ul class="shop-list">
      <li v-for="(item, index) in shop_cart">
        <div class="store-title">
          <el-checkbox v-model="item.select" text-color="#fff" fill="#fff" @change="changeSelect(2, index)">店铺：<i>{{item.shop}}</i></el-checkbox>
        </div>
        <ul class="store-shop" style="flex-direction: column;">
          <li v-for="(value,h) in item.content" class="shop">
            <div class="container-1">
              <div class="shop-img">
                <el-checkbox v-model="value.selected" @change="changeSelect(3, index, value.id)"></el-checkbox>
                <img :src="value.goods_image" alt=""/>
              </div>
              <div class="shop-present">
                <span>{{value.title}}</span>
                <div class="shop-promise">
                  <img src="@/assets/verygoods/xcard.png" alt="" />
                  <img src="@/assets/verygoods/sun.png" alt="" />
                  <img src="@/assets/verygoods/seven.png" alt="" />
                </div>
              </div>
            </div>
            <div class="opt">
              <span v-for="i in value.opts" style="padding-right: 12px;">{{i.type}}：{{i.content}}</span>
              <span v-if="!value.opts[0]">无</span>
            </div>
            <div class="container-2">
              <span class="price">¥{{value.price}}.00</span>
              <div class="num">
                <button class="iconfont" @click="value.num++,totalPrice()">&#xe654;</button>
                <!--<input type="text" alt="" v-model="value.num"/>-->
                <input v-model="value.num" type="number" autocomplete="off" @blur="value.num=value.num===0?1:value.num, totalPrice()" onkeypress="return (/[\d]/.test(String.fromCharCode(event.keyCode)))" style="ime-mode:Disabled">
                <button class="iconfont" @click="reduce(index, h)">&#xe656;</button>
              </div>
              <span class="all-price">¥{{value.price * value.num}}.00</span>
              <div class="handle">
                <span>移入收藏夹</span>
                <span @click="deleteShopCart(value.id)">删除</span>
              </div>
            </div>
          </li>
        </ul>
      </li>
    </ul>
  </div>
    <div v-else>
      <el-empty description="description" />
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShopCart',
  data () {
    return {
      shop_cart: [],
      checked: false,
      total_price: 0,
      shop_num: 0
    }
  },
  // 请求购物车信息
  methods: {
    // 购物车结算
    balance () {
      // 筛选出选择结算的商品有哪些
      let idlist = ''
      let numlist = ''
      for (let i = 0; i < this.shop_cart.length; i++) {
        for (let j = 0; j < this.shop_cart[i].content.length; j++) {
          if (this.shop_cart[i].content[j].selected === true) {
            let id = this.shop_cart[i].content[j].id
            let num = this.shop_cart[i].content[j].num
            idlist += id + '.'
            numlist += num + '.'
          }
        }
      }
      if (idlist !== '') {
        this.BuyNow(idlist.substr(0, idlist.length - 1), numlist.substr(0, numlist.length - 1))
      }
    },
    BuyNow (idlist, numlist) {
      this.$router.push({
        path: '/payment',
        query: {
          id: idlist,
          num: numlist,
          type: 1
        }
      })
    },
    totalPrice () {
      this.total_price = 0
      this.shop_num = 0
      for (let store of this.shop_cart) {
        for (let shop of store.content) {
          this.shop_num++
          if (shop.selected === true) {
            this.total_price = shop.num * shop.price + this.total_price
          }
        }
      }
    },
    deleteShopCart (id) {
      this.$confirm('此操作将删除该商品, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
        // 删除数据请求
        this.$https.post('user/delete_shop_cart/', { id: id }).then(res => {
          if (res.data.code === 200) {
            this.getShopCart()
          }
        }).catch(err => {
          console.log(err)
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    // 商品数量减少
    reduce (index, i) {
      this.totalPrice()
      let num = this.shop_cart[index].content[i].num
      if (num > 1) {
        this.shop_cart[index].content[i].num--
      }
    },
    // 共有单选多选操作
    changeAll () {
      let length = this.shop_cart.length
      for (let i = 0; i < length; i++) {
        if (this.shop_cart[i].select === true) {
          this.checked = true
        } else {
          this.checked = false
          break
        }
      }
    },
    // 单选多选操作
    changeSelect (type, index, id) {
      if (type === 1) {
        let length = this.shop_cart.length
        for (let i = 0; i < length; i++) {
          this.shop_cart[i].select = this.checked
          for (let h of this.shop_cart[i].content) {
            h.selected = this.checked
          }
        }
      }
      if (type === 2) {
        let judge = this.shop_cart[index].select
        for (let i of this.shop_cart[index].content) {
          i.selected = judge
        }
        this.changeAll()
      }
      if (type === 3) {
        for (let i of this.shop_cart[index].content) {
          if (i.selected === true) {
            this.shop_cart[index].select = true
          } else {
            this.shop_cart[index].select = false
            break
          }
        }
        this.changeAll()
      }
      this.totalPrice()
    },
    getShopCart () {
      this.$https.post('user/shopcart/', { type: 1 }).then(res => {
        if (res.data.code === 200) {
          this.shop_cart = res.data.data.shop_cart_info
          this.totalPrice()
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.getShopCart()
  }
}
</script>

<style scoped lang="less">
#shop-cart {
  width: 100%;
  box-shadow:0 15px 35px rgba(255,255,255,0.2),0 2px 5px rgba(0,0,0,0.2);
  border: 1px solid #ccc;
  padding-bottom: 45px;
  border-radius: 25px;
  overflow: hidden;
  .shop-list {
    margin: 0;
    padding: 0;
  }
  .title {
    width: 100%;
    padding: 0 18px;
    height: 73px;
    display: flex;
    background-color: #fff;
    border-top-right-radius: 25px;
    border-top-left-radius: 25px;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #ccc;
    h4 {
      font-size: 18px;
      color: #000;
      font-weight: 800;
      margin: 0;
    }
    .all-price {
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      span {
        font-size: 14px;
        color: #000;
        font-weight: 450;
      }
      i {
        font-style: normal;
        font-family: Verdana,Arial,serif;
        font-weight: 500;
        font-size: 22px;
        color: #ff5000;
        margin: 0 10px;
      }
      .settlement {
        width: 74px;
        height: 42px;
        line-height: 42px;
        background: #aaa;
        color: #fff;
        cursor: not-allowed;
        border-radius: 21px;
      }
    }
  }
  .cart-table-th {
    height: 50px;
    width: 100%;
    display: flex;
    align-items: center;
    font-size: 13px;
    font-weight: 700;
    color: #3c3c3c;
    justify-content: space-between;
    padding: 0 28px 0 28px;
    span {
      width: 130px;
      height: 50px;
      line-height: 50px;
    }
    .thm-1 {
      width: 334px;
      justify-content: space-between;
      span {
        width: 215px;
        text-align: left;
      }
    }
    .thm-2 {
      width: 490px;
      justify-content: space-around;
    }
    .box {
      display: flex;
      align-items: center;
    }
  }
  .store-title {
    display: flex;
    padding-left: 15px;
    :deep(.el-checkbox__label) {
      font-size: 12px;
      color: black;
      font-weight: 400;
      i {
        font-style: normal;
        color: #3c3c3c;
        font-weight: 400;
      }
    }
  }
  .store-shop {
    margin: 0 28px;
    border-radius: 15px;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #F5F5F5;
    .shop {
      width: 100%;
      display: flex;
      justify-content:space-between;
      margin: 20px 0;
    }
    .container-1 {
      height: 82px;
      width: 335px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      .shop-img {
        width: 116px;
        padding-left: 15px;
        img {
          margin-left: 7px;
          width: 80px;
          height: 80px;
        }
      }
      .shop-present {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 100%;
        span {
          font-size: 12px;
          max-height: 36px;
          overflow: hidden;
          text-overflow: ellipsis;
          width: 215px;
          text-align: left;
        }
        .shop-promise {
          display: flex;
          width: 50px;
          justify-content: space-between;
          margin-left: 7px;
          img {
            margin-right: 7px;
          }
        }
      }
    }
    .opt {
      height: 84px;
      width: 170px;
      color: #9c9c9c;
      padding: 0 5px 0 15px;
      overflow: hidden;
      text-overflow: ellipsis;
      font-size: 12px;
      text-align: left;
    }
    .container-2 {
      display: flex;
      width: 490px;
      justify-content: space-around;
      align-items: flex-start;
      height: 84px;
      .price {
        width: 130px;
        font-size: 12px;
        color: #3c3c3c;
        font-weight: 700;
        font-family: Verdana,Tahoma,arial,serif;
      }
      .num {
        display: flex;
        align-items: flex-start;
        justify-content:center;
        width: 130px;
        button {
          color: #444;
          background: #f0f0f0;
          border: 1px solid #e5e5e5;
          height: 23px;
          width: 17px;
          line-height: 23px;
        }
        input {
          width: 39px;
          height: 23px;
          border: 1px solid #aaa;
          outline: none;
          padding: 4px 0;
          font-size: 12px;
          text-align: center;
          color: #343434;
          background-color: #fff;
        }
      }
      .all-price {
        font-size: 12px;
        width: 130px;
        color: #ff4400;
        font-weight: 700;
        font-family: Verdana,Tahoma,arial,serif;
      }
      .handle {
        width: 130px;
        height: 45px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        span {
          color: #3c3c3c;
          font-size: 12px;
          cursor: pointer;
          &:hover {
            color: #FF4401;
          }
        }
      }
    }
  }
  :deep(.el-checkbox__input.is-checked+.el-checkbox__label) {
    color: black;
  }
}
:deep(.el-divider--horizontal) {
  margin: 25px 0 0 0;
}
:deep(.ant-affix) {
  width: 100%;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
}
input[type="number"] {
    -moz-appearance: textfield;
}
</style>
