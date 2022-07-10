<template>
  <div v-if="order_info.length">
    <table>
      <colgroup>
        <col style="width: 38%;">
        <col style="width: 10%;">
        <col style="width: 5%;">
        <col style="width: 12px;">
        <col style="width: 12%;">
        <col style="width: 11%;">
        <col style="width: 12%;">
      </colgroup>
      <thead>
        <tr>
          <th>宝贝</th>
          <th>单价</th>
          <th>数量</th>
          <th>商品操作</th>
          <th>实付款</th>
          <th>交易状态</th>
          <th>交易操作</th>
        </tr>
        <tr class="sep-row">
          <td colspan="4">
            <div class="row-left" v-if="name==='payoff'||name==='receiving'">
              <div>
                <input type="checkbox" v-model="select_all" @change="ChoiceShop(1)">
                <strong>全选</strong>
              </div>
              <span @click="FullPayment" v-if="name==='payoff'">合并付款</span>
              <span @click="FullPayment" v-if="name==='payoff'">合并代付</span>
              <span v-if="name==='receiving'" style="margin-right: 54px;" @click="ConfirmReceipt">批量确认收货</span>
            </div>
          </td>
          <td colspan="3">
            <div class="row-right">
              <span style="margin-right: 15px;">上一页</span>
              <span>下一页</span>
            </div>
          </td>
        </tr>
      </thead>
      <tbody v-for="(item,index) in order_info">
        <tr>
          <td colspan="7" class="interval"></td>
        </tr>
        <tr class="title">
          <td>
            <div class="bought-wrapper">
              <div>
                <input type="checkbox" v-model="item.content[0].selected" @change="ChoiceShop(0)" v-if="name==='payoff'||name==='receiving'">
                <span>{{item.content[0].time}}</span>
              </div>
              <span>订单号: <i>2646139393277811146</i></span>
            </div>
          </td>
          <td colspan="2">
            <span class="store-name">{{item.store}}</span>
          </td>
          <td colspan="4"></td>
        </tr>
        <tr class="container">
          <td style="border-left: 1px solid #DAF3FF;" class="bottom-out">
            <div class="ml-mod">
              <img :src="item.content[0].goods_image" alt="" class="image"/>
              <div class="shop-container">
                <span class="shop-title">{{item.content[0].title}}</span>
                <div class="shop-opt">
                  <span v-for="value in item.content[0].opts">{{value.type}}：{{value.content}}</span>
                </div>
                <img src="@/assets/verygoods/baozhang.png" alt="" />
              </div>
            </div>
          </td>
          <td class="bottom-out">
            <div class="unit-price">
              ¥ {{item.content[0].price}}.00
            </div>
          </td>
          <td class="bottom-out">
            <div class="unit-price">
              {{item.content[0].num}}
            </div>
          </td>
          <td class="bottom-out">
            <!-- 已签收 -->
            <div class="shop-operation" v-if="name==='sign'">
              <span>申请售后</span>
              <span>退运保险</span>
            </div>
            <!-- 待付款 -->
            <div class="shop-operation" v-if="name==='payoff'">
              <span>违规举报</span>
              <span>退运保险</span>
            </div>
            <!-- 待发货 -->
            <div class="shop-operation" v-if="name==='delivery'">
              <span>退款/退货</span>
              <span>投诉商家</span>
              <span>退运保险</span>
            </div>
            <!-- 待收货 -->
            <div class="shop-operation" v-if="name==='receiving'">
              <span>退款/退换货</span>
              <span>投诉商家</span>
              <span>运费险已出单</span>
            </div>
          </td>
          <td class="undecided">
            <div class="total-price">
              <i>¥ {{item.content[0].price*item.content[0].num}}.00</i>
              <span>(包含运费：¥0.00)</span>
            </div>
          </td>
          <td class="undecided">
            <!-- 已签收 -->
            <div class="shop-operation" v-if="name==='sign'">
              <span>交易成功</span>
              <span>订单详情</span>
            </div>
            <!-- 待付款 -->
            <div class="shop-operation" v-if="name==='payoff'">
              <span>等待卖家付款</span>
              <span>订单详情</span>
            </div>
            <!-- 待发货 -->
            <div class="shop-operation" v-if="name==='delivery'">
              <span>买家已付款</span>
              <span>订单详情</span>
            </div>
            <!-- 待收货 -->
            <div class="shop-operation" v-if="name==='receiving'">
              <span>卖家已发货</span>
              <span>订单详情</span>
              <span>查看物流</span>
            </div>
          </td>
          <td class="undecided">
            <!-- 已签收 -->
            <div class="transaction-operation" v-if="name==='sign'">
              <span>申请开票</span>
            </div>
            <!-- 待付款 -->
            <div class="transaction-operation" v-if="name==='payoff'">
              <el-button type="success" @click="ImmediatePayment(item.content[0].id)">立即付款</el-button>
              <span>找朋友帮忙付</span>
              <span @click="CancellationOrder(item.content[0].id)">取消订单</span>
              <span @click="ModifyOrder(item.content[0].id, item.content[0].num)">修改订单</span>
            </div>
            <!-- 待发货 -->
            <div class="transaction-operation" v-if="name==='delivery'">
              <span>修改订单</span>
              <span>申请开票</span>
            </div>
            <!-- 待收货 -->
            <div class="transaction-operation" v-if="name==='receiving'">
              <span><i class="iconfont">&#xe6b5;</i>还剩3天2时</span>
              <el-button type="success" @click="ConfirmReceipt(item.content[0].id)">确认收货</el-button>
              <span>申请开票</span>
            </div>
          </td>
        </tr>
        <tr class="insurance">
          <td style="border-left: 1px solid #DAF3FF;" class="bottom-out">
            保险服务
          </td>
          <td class="bottom-out">
            ¥ 0.00
          </td>
          <td class="bottom-out"></td>
          <td class="bottom-out"></td>
          <td class="head-less"></td>
          <td class="head-less"></td>
          <td class="head-less"></td>
        </tr>
      </tbody>
    </table>
    <el-pagination background layout="prev, pager, next" :page-count="page_count" @current-change="SwitchPages" :current-page="index" :hide-on-single-page="true"/>
  </div>
  <div v-else>
    <el-empty description="暂无数据" />
  </div>
</template>

<script>
export default {
  name: 'test',
  data () {
    return {
      // 全选按钮
      select_all: false,
      info: {
        payoff: 2,
        delivery: 3,
        receiving: 6,
        sign: 5
      },
      name: '',
      order_info: '',
      page_count: 0,
      index: 1
    }
  },
  methods: {
    SwitchPages (index) {
      this.index = index
      this.$router.push({
        query: {
          index: this.index
        }
      })
    },
    // 批量确认收货
    ConfirmReceipt (shopcart) {
      let idlist = ''
      for (let i = 0; i < this.order_info.length; i++) {
        if (this.order_info[i].content[0].selected === true) {
          let id = this.order_info[i].content[0].id
          idlist += id + '.'
          idlist = idlist.substr(0, idlist.length - 1)
        }
      }
      if (typeof shopcart === 'number') {
        idlist = shopcart + ''
      }
      if (idlist !== '') {
        this.$https.post('user/confirm_receipt/', { id: idlist }).then(res => {
          if (res.data.code === 200) {
            this.getOrderInformation()
          }
        }).catch(err => {
          console.log(err)
        })
      } else {
        this.$message({
          type: 'info',
          message: '请选择商品'
        })
      }
    },
    // 批量付款
    FullPayment () {
      let idlist = ''
      for (let i = 0; i < this.order_info.length; i++) {
        if (this.order_info[i].content[0].selected === true) {
          let id = this.order_info[i].content[0].id
          idlist += id + '.'
        }
      }
      if (idlist !== '') {
        this.$router.push({
          path: '/sure/payment',
          query: {
            id: idlist.substr(0, idlist.length - 1)
          }
        })
      } else {
        this.$message({
          type: 'info',
          message: '请选择商品'
        })
      }
    },
    // 商品选择
    ChoiceShop (type) {
      if (type) {
        if (this.select_all) {
          for (let i = 0; i < this.order_info.length; i++) {
            this.order_info[i].content[0].selected = true
          }
        } else {
          for (let i = 0; i < this.order_info.length; i++) {
            this.order_info[i].content[0].selected = false
          }
        }
      } else {
        for (let i = 0; i < this.order_info.length; i++) {
          if (this.order_info[i].content[0].selected === true) {
            this.select_all = true
          } else {
            this.select_all = false
            break
          }
        }
      }
    },
    // 修改订单
    ModifyOrder (id, num) {
      this.$router.push({
        path: '/payment',
        query: {
          id: id,
          num: num,
          type: 1
        }
      })
    },
    // 取消订单
    CancellationOrder (id) {
      this.$confirm('你确定要取消该订单吗？, 是否继续?', '提示', {
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
            this.getOrderInformation()
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
    // 立即付款
    ImmediatePayment (id) {
      this.$router.push({
        path: '/sure/payment',
        query: {
          id: id
        }
      })
    },
    getOrderInformation () {
      let type = this.info[this.$route.name]
      if (type !== undefined) {
        this.$https.post('user/shopcart/', { type: type, index: this.index }).then(res => {
          if (res.data.code === 200) {
            this.$emit('childClick')
            this.timeConversion(res.data.data.shop_cart_info)
            this.order_info = res.data.data.shop_cart_info
            this.page_count = res.data.data.page_count
          }
        }).catch(err => {
          console.log(err)
        })
      }
    },
    timeConversion (data) {
      for (let i = 0; i < data.length; i++) {
        let time = data[i].content[0].time.split('T')
        let day = time[0]
        let date = time[1].split(':')
        let hour = date[0] + ':' + date[1]
        data[i].content[0].time = day + ' ' + hour
      }
    }
  },
  created () {
    this.name = this.$route.name
  },
  watch: {
    '$route.name': {
      handler (newVal, oldVal) {
        this.name = newVal
        this.index = 1
        this.getOrderInformation()
      },
      // 深度观察监听
      immediate: true
    },
    '$route.query.index': {
      handler (newVal, oldVal) {
        this.name = this.$route.name
        if (newVal) {
          this.index = parseInt(newVal)
          this.getOrderInformation()
        }
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style scoped lang="less">
table {
  width: 100%;
}
thead {
  tr {
    border-top: 1px solid #e0e0e0;
  }
}
.interval {
  height: 15px;
  background: #fff;
  border: 0;
}
th,td {
  font-size: 12px;
  height: 39px;
  text-align: center;
  background: #f5f5f5;
  color: #666;
  font-weight: 400;
  border-left: 1px solid #e0e0e0;
  border-right: 1px solid #e0e0e0;
}
.sep-row {
  height: 39px;
  td {
    background: #fff;
    border-left: 0;
    border-right: 0;
    height: 15px;
    padding: 0;
  }
  div {
    display: flex;
    align-items: center;
    input {
      margin-right: 7px;
    }
  }
  .row-left {
    justify-content: space-between;
    width: 32%;
    padding-left: 25px;
  }
  span {
    padding: 0 12px;
    border: 1px solid #DCDCDC;
    border-radius: 2px;
    height: 24px;
    line-height: 22px;
    cursor: pointer;
    color: #3c3c3c;
  }
  .row-right {
    justify-content: flex-end;
  }
}
.title {
  height: 43px;
  border: 1px solid #DAF3FF;
  border-bottom: 0;
  td {
    border-left: 0;
    border-right: 0;
    background-color: #EBF8FF;
  }
  .bought-wrapper {
    padding-left: 28px;
    display: flex;
    div {
      display: flex;
      align-items: center;
      span {
        margin-left: 7px;
        color: #000;
        font-weight: 600;
      }
    }
    span {
      margin-left: 25px;
      color: #3c3c3c;
      font-size: 12px;
      i {
        font-style: normal;
        font-weight: 500;
      }
    }
  }
}
.store-name {
  width: 100%;
  display: inline-block;
  text-align: left;
}
.container {
  height: 135px;
  td {
    background-color: #fff;
    border: 1px solid #DAF3FF;
  }
  .undecided {
    border-bottom: 0;
  }
  .bottom-out {
    border: 0;
    border-bottom: 1px solid #DAF3FF;
  }
  .ml-mod {
    padding-left: 20px;
    width: 100%;
    display: flex;
    .image {
      width: 80px;
      height: 80px;
    }
    .shop-container {
      width: 275px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      text-align: left;
      padding-left: 7px;
      font-weight: bold;
      img {
        width: 52px;
        height: 16px;
      }
      .shop-title {
        overflow:hidden;
        text-overflow:ellipsis;
        display:-webkit-box;
        -webkit-line-clamp:2;
        height: 39px;
        color: #3c3c3c;
      }
      .shop-opt {
        color: #9e9e9e;
        span {
          padding-right: 9px;
        }
      }
    }
  }
  .unit-price {
    display: flex;
    height: 80px;
    width: 100%;
    justify-content: center;
    color: black;
    font-weight: bold;
  }
  .shop-operation {
    height: 80px;
    width: 100%;
    display: flex;
    flex-direction: column;
    color: #3c3c3c;
    span {
      padding: 2px 0;
      &:hover {
        cursor: pointer;
        color: #FF4401;
        text-decoration: underline;
      }
    }
  }
  .total-price {
    display: flex;
    flex-direction: column;
    height: 80px;
    i {
      font-weight: bold;
      color: black;
      font-style: normal;
    }
    span {
      color: #6c6c6c;
      font-weight: 400;
    }
  }
  .transaction-operation {
    display: flex;
    flex-direction: column;
    height: 80px;
    align-items: center;
    span {
      margin: 2px 0;
      cursor: pointer;
      &:hover {
        cursor: pointer;
        color: #FF4401;
        text-decoration: underline;
      }
    }
  }
}
.insurance {
  height: 53px;
  td {
    background-color: #fff;
    &:first-child {
      text-align: left;
      padding-left: 20px;
    }
  }
}
:deep(.el-button) {
  width: 78px;
  height: 32px;
}
.head-less {
  border: 1px solid #DAF3FF;
  border-top: 0;
}
.bottom-out {
  border: 0;
  border-bottom: 1px solid #DAF3FF;
}
:deep(.el-pagination) {
  justify-content: center;
  margin: 95px 0 45px;
}
</style>
