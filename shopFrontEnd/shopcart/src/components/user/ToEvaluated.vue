<!-- 待评价 -->
<template>
  <div>
    <table>
      <colgroup>
        <col style="width: 50%;">
        <col style="width: 20%;">
        <col style="width: 16%;">
        <col style="width: 233px;">
      </colgroup>
      <thead>
        <tr>
          <th>订单详情</th>
          <th>收货人</th>
          <th>金额</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody v-for="item in evaluate">
        <tr class="sep-row">
          <td colspan="4"></td>
        </tr>
        <tr>
          <td colspan="4" class="date">
            <span>2022-04-24 16:33:26</span>
            <span>订单号：<i>239846789464</i></span>
          </td>
        </tr>
        <tr class="shop">
          <td>
            <div class="goods-item">
              <img :src="item.img" alt="" style="width: 60px;height: 60px;"/>
              <div>{{item.title}}</div>
              <span>x {{item.num}}</span>
            </div>
          </td>
          <td class="name">
            <span>{{item.name}}</span><i class="iconfont">&#xe64a;</i>
          </td>
          <td>
            支付金额 ￥{{item.price*item.num}}.00
          </td>
          <td>
            <div class="operate">
              <span>订单详情</span>
              <div class="evaluate" @click="goEvaluate(item.id)">评价</div>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'ToEvaluated',
  data () {
    return {
      evaluate: ''
    }
  },
  methods: {
    goEvaluate (id) {
      console.log(id)
      this.$router.push({
        path: '/evaluate',
        query: {
          id: id
        }
      })
    },
    getShop () {
      this.$https.post('user/evaluated/').then(res => {
        console.log(res)
        if (res.data.code === 200) {
          this.evaluate = res.data.data.evaluate
        }
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.getShop()
  }
}
</script>

<style scoped lang="less">
tr {
  border-top: 1px solid #e0e0e0;
}
th,td {
  font-size: 12px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  background: #f5f5f5;
  color: #666;
  font-weight: 400;
  border-left: 1px solid #e0e0e0;
  border-right: 1px solid #e0e0e0;
}
.date {
  text-align: left;
  span:first-child {
    padding: 0 25px 0 20px;
  }
  span {
    color: #aaa;
  }
  i {
    font-style: normal;
    color: black;
  }
}
.sep-row {
  td {
    background: #fff;
    border-left: 0;
    border-right: 0;
    height: 15px;
    padding: 0;
  }
}
.shop {
  td {
    padding: 20px 0;
    background: #fff;
    border-bottom: 1px solid #e0e0e0;
    .goods-item {
      display: flex;
      img {
        width: 60px;
        height: 60px;
        margin-left: 15px;
      }
      div {
        margin-left: 20px;
        height: 36px;
        width: 232px;
        line-height: 18px;
        overflow: hidden;
        color: #333;
        text-align: left;
      }
      span {
        width: 70px;
        margin-left: 131px;
      }
    }
  }
}
.evaluate {
  width: 89px;
  height: 29px;
  border: 1px solid #DDDDDD;
  background-color: #f3f3f3;
  line-height: 29px;
  cursor: pointer;
}
.operate {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.name {
  color: #c1c1c1;
  i {
    font-size: 16px;
    margin-left: 5px;
  }
}
</style>
