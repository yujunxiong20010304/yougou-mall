<template>
  <div class="shop-center">
    <div class="title">
      {{title}}
    </div>
    <div id="pic">
      <div class="pic_container">
        <span style="padding-left: 10px;">价格</span>
        <i class="pic_num" v-if="price_range">
          <span>￥</span>
          <!--<i class="price">1200.00{{price_range}}</i>-->
          <i class="price" v-if="price">{{price}}.00</i>
          <i class="price" v-else-if="price_range.price__min===price_range.price__max">{{price_range.price__min}}.00</i>
          <i class="price" v-else>{{price_range.price__min}}.00-{{price_range.price__max}}.00</i>
        </i>
        <a href="javascript:">降价通知</a>
      </div>
      <span class="evaluate">
        <span>累计评价</span>
        <i>{{evaluate}}</i>
      </span>
    </div>
    <div class="place">
      <span style="padding-left: 10px;">配送至</span>
      <div @mouseover="moveIn" @mouseout="moveOut" id="address" ref="address">
        {{sureAddress}}<i class="iconfont" style="font-size: 16px;">&#xe611;</i>
      </div>
      <div id="choice-address" @mouseover="moveIn" @mouseout="moveOut" ref="ChoiceAddress">
        <ul id="ui-area-tab">
          <li v-for="item in address" :key="item.id" @click="choiceAddress(item.id)" :class="[item.id===aim?'select-address':'']">{{item.text}}<i class="iconfont">&#xe611;</i></li>
        </ul>
        <ul id="ui-area-content-list" ref="ShowAddress" v-if="reflectAddress">
          <li v-for="item in reflectAddress" :key="item.id">
            <a href="javascript:void(0)" @click="detailAddress(item.id, item.type, item.name)" :data-id="item.id" :class="[aim===item.id?'current-address':'']">{{item.name}}</a>
          </li>
        </ul>
      </div>
      <span style="padding: 0 15px 0 5px;font-weight: bold;">有货</span>
      <span>在线支付免运费<i class="iconfont">&#xe68f;</i></span>
      <span class="dd">由 <i>{{shop}}</i> 发货, 并提供售后服务. 今日16:30前完成下单，预计3月16日19:00前发货</span>
    </div>
    <div class="se_su">
      <div class="se_su_one">
        <span style="margin-left: 10px;">服务支持</span>
        <div class="as_pu"></div>
        <span style="color: #005AA0;">免费上门取退</span>
        <span style="color: #005AA0;">极速审核</span>
      </div>
      <div class="se_su_two">
        <span>可配送港澳特权保障</span>
        <span>退换货运费险</span>
        <span>自提</span>
      </div>
    </div>
    <div class="category" ref="category">
        <span class="tips" ref="tips">
          请选择你要的商品信息
          <span class="close-tips" @click="closeTips">x</span>
        </span>
        <div v-for="(item, index) in opt" :key="index" class="attr1" :ref="`list${index}`">
          <span>{{item.name}}</span>
          <ul class="ca_ch">
            <li v-for="value in item.content"
                :key="value.id"
                class="a-choice"
                @click="getOptPrice(value.id, index, value.type)"
                :ref="`list${value.id}`">
              <img :src="value.image" alt="" v-show="value.image!=='None'"/>
              <i>{{value.content}}</i>
            </li>
          </ul>
        </div>
    </div>
    <div class="quantity">
        <span>数量</span>
        <span class="calculation">
            <button @click="subNumber">-</button>
            <!--<input type="text" v-model="number" @keyup="changeNumber" @blur="sureChange"/>-->
            <input v-model="number" type="number" autocomplete="off" @blur="sureChange" onkeypress="return (/[\d]/.test(String.fromCharCode(event.keyCode)))" style="ime-mode:Disabled">
            <button @click="this.number++">+</button>
        </span>
    </div>
    <div class="satis">
        <a class="purchase" href="javascript:void(0)" @click="addTo(0)">立即购买</a>
        <button class="collection" @click="addTo(1)"><i class="iconfont" style="margin-right: 10px;">&#xe63f;</i>加入购物车</button>
    </div>
    <!-- 成功加入购物车提示 -->
    <div class="success-prompt" ref="SuccessPrompt">
      <img src="@/assets/verygoods/sucess.png" alt="" />
      <div>
          <h5>成功加入购物车</h5>
          <span>你可以去购物车结算，或先使用 天猫APP 领取新用户福利礼包立即下载天猫APP</span>
      </div>
      <span class="close-s-p" @click="closeSuccess">X</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'shopCenter',
  data () {
    return {
      choices: {},
      priceId: undefined,
      price: '',
      shop_cart_id: '',
      address: {
        0: { text: '四川省', id: 51 },
        1: { text: '成都市', id: 5101 },
        2: { text: '双流区', id: 510116 },
        3: { text: '万安街道', id: 510116018 }
      },
      aim: 510116018,
      reflectAddress: '',
      sureAddress: '四川省成都市双流区万安街道',
      number: 1
    }
  },
  props: ['opt', 'title', 'price_range', 'evaluate', 'shop'],
  methods: {
    closeSuccess () {
      this.$refs.SuccessPrompt.style = 'display: none'
    },
    // 关闭提示
    closeTips () {
      this.$refs.category.style = 'border: 0'
      this.$refs.tips.style = 'display: none'
    },
    // 立即购买和收藏
    addTo (type) {
      let select = document.querySelectorAll('.ch-re').length
      let selected = document.querySelectorAll('.attr1').length
      if (select === selected) {
        // 加入购物车
        if (type) {
          this.judgeToken(1)
        } else {
          // 购买
          this.judgeToken(0)
        }
      } else {
        this.$refs.category.style = 'border: 1px solid red'
        this.$refs.tips.style = 'display: inline-block'
      }
    },
    // 验证token的有效性 并进行购买或收藏, // 需要验证该账号是否有支付密码
    judgeToken (type) {
      this.$https.post('store/obtainShop/', { type: type, goodsId: this.$route.query.id, number: this.number, priceId: this.priceId }).then(res => {
        // 加入购物车
        if (res.data.code === 200) {
          // 加入购物车
          if (type) {
            this.$refs.SuccessPrompt.style = 'display: flex'
            this.$refs.SuccessPrompt.style.top = window.innerHeight / 2 + document.documentElement.scrollTop + 'px'
            setTimeout(() => {
              this.$refs.SuccessPrompt.style = 'display: none'
            }, 3000)
            // 跳转去购买页
          } else {
            this.$router.push({
              path: '/payment',
              query: {
                id: this.$route.query.id,
                priceId: this.priceId,
                num: this.number
              }
            })
          }
          // 登录提示或者请求失败提示
        } else if (res.data.code === 404) {
          this.$message({
            type: 'info',
            message: '该类商品已售空'
          })
        } else {
          // 请登录
          window.open('/oauth/login/', '_blank')
        }
      }).catch(err => {
        console.log(err)
      })
    },
    subNumber () {
      if (this.number > 1) {
        this.number--
      }
    },
    sureChange () {
      if (!this.number) {
        this.number = 1
      }
    },
    // 移入
    moveIn () {
      this.$refs.address.className = 'address-hover'
      this.$refs.ChoiceAddress.style = 'display: table'
      if (!this.reflectAddress) {
        this.getAddress(this.address[3].id)
      }
    },
    // 移出
    moveOut () {
      this.$refs.address.className = ''
      this.$refs.ChoiceAddress.style = 'none'
    },
    // 选择 省， 市， 区， 街
    choiceAddress (id) {
      this.aim = id
      // 发送 axios 请求
      this.getAddress(id)
    },
    // 详细地址请求
    detailAddress (id, type, name) {
      this.address[parseInt(type)] = { text: name, id: id }
      if (type !== 3) {
        for (let i of [0, 1, 2, 3]) {
          if (i > parseInt(type)) {
            delete this.address[i]
          }
        }
        this.address[parseInt(type) + 1] = { text: '请选择', id: 0 }
        this.aim = 0
        this.getAddress(id, 1)
      } else {
        this.aim = id
        this.moveOut()
        // 将选择好的值赋值给选择框
        this.sureAddress = ''
        for (let i of [0, 1, 2, 3]) {
          this.sureAddress += this.address[i].text
        }
      }
    },
    // 发送axios请求获取地址选择数据数据
    getAddress (id, type) {
      this.$https.post('store/address/', { id: id, type: type }).then(res => {
        this.reflectAddress = res.data.data.address
      }).catch(err => {
        console.log(err)
      })
    },
    getOptPrice (id, index, type) {
      let lis = this.$refs[`list${index}`][0].childNodes[1].childNodes
      for (let i of lis) {
        if (i.classList) {
          if (i.classList.length === 2) {
            i.className = 'a-choice'
          }
        }
      }
      this.$refs[`list${id}`][0].className = 'ch-re a-choice'
      this.choices[type] = id
      // 需要判断当前商品是否有多个价格
      let select = document.querySelectorAll('.ch-re').length
      let selected = document.querySelectorAll('.attr1').length
      if (select === selected) {
        this.closeTips()
        if (this.price_range.price__min !== this.price_range.price__max) {
          this.getPrice()
        }
      }
    },
    async getPrice () {
      const { data: res } = await this.$http.post('store/update/', { choices: this.choices })
      this.price = res.data.price
      this.priceId = res.data.id
    }
  }
}
</script>

<style scoped lang="less">
.shop-center {
  width: 665px;
  .title {
    font: 700 16px Arial,"microsoft yahei";
    color: #666;
    overflow: hidden;
    width: 590px;
    line-height: 28px;
    padding-top: 10px;
    margin-bottom: 10px;
    box-sizing: content-box;
    text-align: left;
  }
}
#pic {
  width: 590px;
  height: 35px;
  padding-top: 10px;
  box-sizing: content-box;
  font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
  color: #999;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  background-color: rgba(255,255,255,.5);
  border-radius: 2px;
  a {
    text-decoration: none;
    color: #005AA0;
  }
  i {
    font-style: normal;
  }
}
.pic_num {
  color: #E4393C;
  font-size: 22px;
  margin: 0 25px 0 15px;
  span {
    font-size: 16px;
  }
}

.evaluate {
  display: flex;
  flex-direction: column;
  border-left: 1px solid #E6E6E6;
  width: 48px;
  height: 32px;
  box-sizing: content-box;
  padding: 0 10px;
  align-items: center;
  justify-content: center;
  i {
    font: 14px verdana;
    color: #005ea7;
  }
}

.pic_container {
    display: flex;
    align-items: center;
    justify-content: flex-start;
}

.place {
  display: flex;
  font-size: 12px;
  color: #999;
  align-items: center;
  margin-top: 10px;
  flex-wrap: wrap;
  position: relative;
  z-index: 1;
  cursor: pointer;
  .address-hover {
    position: relative;
    z-index: 3;
    border-bottom: 1px solid white;
  }
}

#choice-address {
    width: 485px;
    position: absolute;
    top: 25px;
    left: 56px;
    padding: 12px;
    margin: 0;
    display: none;
    background-color: white;
}
#ui-area-tab {
  padding: 0;
  margin: 0;
  display: flex;
  width: 423px;
  height: 27px;
  border-bottom: 2px solid #E4393C;
  li {
    color: #005aa0;
    height: 25px;
    border: 1px solid #DDDDDD;
    border-bottom: 0;
    display: flex;
    padding: 0 7px;
    align-items: center;
    justify-content: center;
    margin-right: 5px;
    cursor: pointer;
    font-size: 12px;
  }
  .select-address {
    border:2px solid #E4393C;
    border-bottom:2px solid white;
    height:27px;
  }
}

#ui-area-content-list {
  width: 423px;
  display: flex;
  flex-wrap: wrap;
  padding: 0;
  margin-top: 7px;
  li {
    width: 125px;
    line-height: 20px;
    text-align: left;
    padding: 2px 5px;
    a {
      text-decoration:none;
      font-weight: 400;
    }
  }
  .current-address {
    color: #E64549;
  }
}
.place div {
    border: 1px solid #CECBCE;
    margin-left: 10px;
    height: 26px;
    line-height: 26px;
    padding: 0 5px;
    color: #666;
    display: flex;
    align-items: center;
    justify-content: center;
}
.dd {
  margin-left: 55px;
  margin-top: 10px;
  i {
    font-style: normal;
    color: #E6474A;
  }
}

.se_su {
    margin: 15px 0;
    color: #999;
    font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
    display: flex;
    flex-direction: column;
    border-bottom: 1px dashed #DFDFDF;
    height: 60px;

}
.as_pu {
  background-image: url('../../assets/backImage/small-icons.png');
  width: 84px;
  height: 16px;
  background-repeat: no-repeat;
  background-position: 50% 26%;
  margin-left: 10px;
}
.se_su_one {
  display: flex;
  span {
    margin: 0 5px;
  }
}

.se_su_two {
  margin-left: 65px;
  margin-top: 10px;
  text-align: left;
  span {
    margin: 0 2px;
  }
}
.category {
    margin-bottom: 10px;
}
.tips {
  width: 100%;
  background: #fff8f7;
  border-bottom: 1px solid #f3e9e7;
  height: 24px;
  line-height: 24px;
  padding-left: 8px;
  color: #666;
  font-family: tahoma,arial,\5FAE\8F6F\96C5\9ED1,sans-serif;
  font-size: 12px;
  margin-bottom: 10px;
  position: relative;
  display: none;
  text-align: left;
}
.close-tips {
  position: absolute;
  right: 10px;
  top: -2px;
  font-size: 14px;
  color: red;
  font-weight: bold;
  cursor: pointer;
}
.attr1{
  color: #999;
  font-size: 12px;
  margin-left: 10px;
  display: flex;
  margin-bottom: 10px;
  span {
    min-width: 48px;
    margin-right: 10px;
  }
}

.ca_ch {
  display: flex;
  flex-wrap: wrap;
  padding-left: 0;
  margin-bottom: 0;
  img {
    width: 40px;
    height: 40px;
  }
  i {
    color: #666;
    font-weight: 400;
    font-style: normal;
    padding: 0 13px;
  }
}

.a-choice {
  border: 1px solid #ccc;
  margin: 0 7px 4px 0;
  background-color: #f7f7f7;
  line-height: 36px;
  cursor: pointer;
  padding: 1px;
}
.ch-re {
  border: 2px solid red;
  box-sizing: border-box;
  padding: 0;
}
.quantity {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 198px;
  margin-bottom: 15px;
  span {
    font-size: 12px;
    color: #999;
    margin-left: 10px;
  }
  button {
    width: 40px;
    height: 35px;
    line-height: 24px;
    border: 0;
    font-size: 18px;
    color: #eee;
    background-color: #409EFF;
  }
  input {
    width: 50px;
    border-left: 0;
    border-right: 0;
    outline: none;
    border-bottom: 1px solid #ccc;
    border-top: 1px solid #ccc;
    height: 35px;
    text-align: center;
    font-size: 16px;
  }
}

.calculation {
    display: flex;
    justify-content: center;
    align-items: center;
}
.satis {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-left: 67px;
  button {
    width: 134px;
    height: 38px;
    border: 0;
  }
  .collection {
    background-color: #FF4401;
    color: #fff;
    width: 180px;
  }
}
.purchase {
  background-color: #FFE4D0;
  color: #FF4401;
  margin-right: 25px;
  width: 134px;
  height: 38px;
  border: 0;
  text-align: center;
  line-height: 38px;
  text-decoration: none;
  &:hover {
    color: #FF4401;
  }
}

.success-prompt {
  position: absolute;
  left: 50%;
  border: 1px solid #d6d6d6;
  transform: translate(-50%, -50%);
  width: 378px;
  height: 118px;
  /*display: flex;*/
  align-items: center;
  font: 12px/1.5 tahoma, arial, 'Hiragino Sans GB', '\5b8b\4f53', sans-serif;
  justify-content: space-around;
  display: none;
  background-color: white;
  text-align: left;
  z-index: 100;
  img {
    width: 30px;
    height: 30px;
  }
  div {
    width: 308px;
    height: 74px;
    h5 {
      font-size: 16px;
      font-weight: 400;
      color: #666;
    }
  }
}
.close-s-p {
  position: absolute;
  top: 3px;
  right: 9px;
  font-size: 16px;
  color: #d6d6d6;
  cursor: pointer;
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
}

input[type="number"] {
    -moz-appearance: textfield;
}
</style>
