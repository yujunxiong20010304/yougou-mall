<template>
  <div>
    <figure id="receive-selection">
        <h6>选择收货地址</h6>
        <div class="address-list">
          <div
            :class="[aim===index?'inner-infos sa':'inner-infos']"
            v-for="(item, index) in address_info"
            :key="item.id"
            @click="selectAddress(index)"
            @mouseover="moveIn(index)"
            @mouseout="moveOut"
            :style="[index>truncation?'display:none':'display:block']"
          >
            <div class="addr-hd">
              <span>{{item.city_address[0][0]}}</span>
              <span>{{item.city_address[1][0]}}</span>
              <span>({{item.name}})</span>
            </div>
            <div class="addr-bd">
              <span>{{item.city_address[2][0]}}</span>
              <span>{{item.city_address[3][0]}}</span>
              <span>{{item.detailed_address}}</span>
              <span>{{item.phone}}</span>
            </div>
            <a href="javascript:" @click="updateAddress">修改</a>
            <img src="@/assets/verygoods/fencec.png" alt="" v-if="aim===index||plan===index"/>
            <img src="@/assets/verygoods/fence.png" alt="" v-else/>
            <span class="dt" v-if="index===0">默认地址</span>
            <div class="selected">
              <span class="iconfont">&#xe650;</span>
            </div>
          </div>
        </div>
        <div class="operations">
            <button :style="[address_quantity>4?'display:none':'display:block']" @click="addAddress">使用新地址</button>
            <a href="javascript:" :style="[address_quantity>4?'display:block':'display:none']" @click="showAllAddress">显示全部地址</a>
            <a href="javascript:">管理收货地址</a>
        </div>
    </figure>
    <!-- 可丢弃 -->
    <main class="add-address" ref="addAddress">
      <div class="next-dialog-header">
        <span>新建地址</span>
        <i style="cursor: pointer;" class="iconfont" @click="closeAddAddress">&#xe740;</i>
      </div>
      <div class="address-container" @click.self="cancelAddress">
        <div class="page-buy">
          <span class="headTips">新增收货地址</span>
          <div class="region">
              <span>当前配送至</span>
              <span>中国大陆</span>
              <span>切换<i class="iconfont">&#xe62e;</i></span>
          </div>
          <div class="address-choices">
            <span class="currency-head"><i>*</i>地址信息：</span>
            <div class="tips" @click="choiceAddress">
              <span class="address" v-if="text" style="color: black;">{{text}}</span>
              <span class="address" v-else>请选择省/市/区/街道</span>
              <i class="iconfont">&#xe62b;</i>
            </div>
            <!-- 地址选择 -->
            <div class="choice" ref="choice">
              <ul>
                <li
                  v-for="(item, index)
                  in choice_address"
                  @click="choices(index)"
                  :ref="`address${index}`"
                  :class="[index===goal?'aim':'']"
                >{{item}}</li>
              </ul>
              <ul class="address-pack">
                <li v-for="item in detail_address" :data-id="item.id" @click="detailAddress(item.id, item.name)" :class="[item.id===parseInt(sign)?'yj':'']">{{item.name}}</li>
              </ul>
            </div>
          </div>
          <div class="detail-address">
              <span class="currency-head"><i>*</i>详细地址：</span>
              <textarea v-model="explicit_address" placeholder="请输入详细地址信息，如道路、门牌号、小区、楼栋号、单元等信息" rows="2" cols="2"></textarea>
          </div>
          <div class="postal-code">
              <span class="currency-head"><i style="opacity: 0;">*</i>邮政编码：</span>
              <input class="currency-into" v-model="postal_code" type="text" placeholder="请填写邮编"/>
          </div>
          <div class="username">
              <span class="currency-head"><i>*</i>收货人姓名：</span>
              <input class="currency-into" type="text" v-model="receiving" placeholder="长度不超过25个字符"/>
          </div>
          <div class="phone">
              <span class="currency-head"><i>*</i>手机号：</span>
              <div>中国大陆 +86<i class="iconfont">&#xe62b;</i></div>
              <input type="text" v-model="phone" placeholder="电话号码、手机号码必须填一项"/>
          </div>
          <div class="storage" @click="addUserAddress()" v-if="change_add===1">添加</div>
          <div class="storage" @click="addUserAddress(this.address_info[aim].id)" v-if="change_add===0">修改</div>
        </div>
      </div>
    </main>
    <div class="mask" ref="mask" @click.self="cancelAddress"></div>
  </div>
</template>

<script>
import emitter from '@/utils/event'
export default {
  name: 'place',
  data () {
    return {
      address_info: '',
      explicit_address: '', // 详细地址
      postal_code: '', // 邮政编码
      receiving: '', // 收货人的姓名
      phone: '', // 手机号码
      change_add: '', // 更改按钮或者增加按钮
      aim: 0,
      plan: '',
      goal: '0',
      sign: '',
      truncation: 3,
      address_quantity: 6, // 6
      detail_address: '',
      choice_address: {
        0: '省',
        1: '市',
        2: '区',
        3: '街道'
      },
      address: [],
      text: ''
    }
  },
  methods: {
    updateAddress () {
      this.receiving = this.address_info[this.aim].name
      this.explicit_address = this.address_info[this.aim].detailed_address
      this.address = JSON.parse(JSON.stringify(this.address_info[this.aim].city_address)) // 深拷贝
      this.phone = this.address_info[this.aim].phone
      for (let i = 0; i < this.address.length; i++) {
        this.$refs[`address${i}`][0].setAttribute('data-id', this.address[i][1])
      }
      this.$refs[`address${0}`][0].className = 'aim'
      this.goal = '0'
      this.sign = this.address[0][1]
      this.change_add = 0
      this.$refs.addAddress.style = 'display: block'
      this.$refs.mask.style = 'display: block'
    },
    // 清空输入框中的内容
    clearInput () {
      this.explicit_address = ''
      this.postal_code = ''
      this.receiving = ''
      this.phone = ''
      this.address = []
      this.text = ''
      for (let i = 0; i < 4; i++) {
        this.$refs[`address${i}`][0].removeAttribute('data-id')
      }
      this.$refs[`address${0}`][0].className = 'aim'
      this.sign = ''
      this.goal = '0'
      this.detail_address = ''
    },
    // 添加保存新的地址信息
    addUserAddress (id) { // 收货信息id， 用于修改
      this.$https.post('payment/addAddress/', {
        id: id,
        address: this.address,
        explicit_address: this.explicit_address,
        postal_code: this.postal_code,
        receiving: this.receiving,
        phone: this.phone
      }).then(res => {
        if (res.data.code === 200) {
          this.address_info = res.data.data.address_info
          this.address_quantity = this.address_info.length
          emitter.emit('address', { aim: this.address_info })
          if (!id) {
            this.aim = this.address_quantity - 1
          }
          emitter.emit('foo', { aim: this.aim })
          this.closeAddAddress()
          this.showAllAddress()
        }
      }).catch(err => {
        console.log(err)
      })
    },
    // 取消地址选择
    cancelAddress () {
      this.$refs.choice.style = 'display: none'
    },
    // 详细地址选择
    detailAddress (id, name) {
      // 把 id 详细地址id标注到所对应的类上
      this.$refs[`address${parseInt(this.goal)}`][0].setAttribute('data-id', id)
      this.address[parseInt(this.goal)] = { 0: name, 1: parseInt(id) }
      // 发起请求获得详细地址id的数据
      if (parseInt(this.goal) < 3) {
        this.getAddress(id, 1)
      }
      // 需要把后面所有省/市/街区的id去掉
      for (let i = 0; i < 4; i++) {
        if (i > parseInt(this.goal)) {
          this.$refs[`address${i}`][0].removeAttribute('data-id')
          delete this.address[i]
        }
      }
      if (parseInt(this.goal) >= 3) {
        this.$refs.choice.style = 'display: none'
        this.sign = id
      } else {
        this.goal = String(parseInt(this.goal) + 1)
      }
    },
    // 省/市/区/街道选择
    choices (index) {
      let id = this.$refs[`address${index}`][0].getAttribute('data-id')
      // 如果当前点击元素的 id 是空的
      if (id) {
        this.goal = index
        this.getAddress(id, 0)
        this.sign = id
      } else if (index !== '0') {
        let fatherId = this.$refs[`address${index - 1}`][0].getAttribute('data-id') // 点击元素的上级id
        if (fatherId) {
          this.goal = index
          this.getAddress(fatherId, 1)
        }
      }
    },
    // 点击选择地址
    choiceAddress () {
      this.$refs.choice.style = 'display: block'
      if (!this.detail_address) {
        this.getAddress(0, 1)
      }
    },
    // 新增地址
    addAddress () {
      this.$refs.addAddress.style = 'display: block'
      this.$refs.mask.style = 'display: block'
      this.change_add = 1
    },
    // 关闭新增地址
    closeAddAddress () {
      this.$refs.addAddress.style = 'display: none'
      this.$refs.mask.style = 'display: none'
      this.clearInput()
    },
    // 显示全部收货地址
    showAllAddress () {
      this.truncation = this.address_quantity
      this.address_quantity = 4
    },
    // 选择收货地址
    selectAddress (index) {
      this.aim = index
      // 判断当前地址的存在， 如果不存在则刷新页面
      this.ValidateAddress()
      emitter.emit('foo', { aim: this.aim })
    },
    // 判断地址的有效性
    ValidateAddress () {
      this.$https.post('payment/address_validate/', { id: this.address_info[this.aim].id }).then(res => {
        if (res.data.code === 404) {
          this.$alert('当前页面数据已更新，需要重新请求数据', '提示', {
            confirmButtonText: '确定',
            callback: action => {
              this.aim = 0
              emitter.emit('foo', { aim: this.aim })
              this.$emit('childClick')
            }
          })
        }
      }).catch(err => {
        console.log(err)
      })
    },
    // 从收货地址选择中移入
    moveIn (index) {
      this.plan = index
    },
    // 从收货地址选择中移出
    moveOut () {
      this.plan = ''
    },
    // 请求收货地址
    getAddress (id, type) {
      this.$https.post('store/address/', { id: id, type: type }).then(res => {
        this.detail_address = res.data.data.address
      }).catch(err => {
        console.log(err)
      })
    }
  },
  mounted () {
    emitter.on('address', (e) => {
      this.address_info = e.aim
      this.address_quantity = this.address_info.length
    })
  },
  watch: {
    address: {
      handler (newVal, oldVal) {
        this.text = ''
        for (let i = 0; i < newVal.length; i++) {
          if (newVal[i]) {
            this.text += newVal[i][0] + '/'
          } else {
            break
          }
        }
      },
      deep: true
    }
  }
}
</script>

<style scoped lang="less">
#receive-selection {
  width: 990px;
  margin: 30px auto;
  h6 {
    color: #333;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 7px;
  }
}
.address-list {
  display: flex;
  justify-content: flex-start;
  flex-wrap: wrap;
}
.inner-infos {
  width: 237px;
  height: 106px;
  position: relative;
  padding: 11px 15px;
  margin-right: 10px;
  margin-bottom: 10px;
  cursor: pointer;
  img {
    position: absolute;
    top: 0;
    left: 0;
    z-index: -1;
    width: 237px;
  }
}
.addr-hd {
  width: 207px;
  height: 23px;
  padding-bottom: 5px;
  border-bottom: 1px solid #f2f2f2;
  margin-bottom: 5px;
  span {
    font-weight: 700;
    color: #666;
    margin-right: 5px;
  }
}
.sa {
  .addr-bd {
    height: 36px;
  }
}
.addr-bd {
  width: 207px;
  height: 55px;
  overflow: hidden;
  span {
    font-weight: 400;
    word-break: break-all;
    word-wrap: break-word;
    margin-right: 3px;
  }
}
.inner-infos {
  a {
    color: #CC9977;
    text-decoration: none;
    display: none;
    &:hover {
      color: #FF0036;
    }
  }
}
.sa {
  a {
    display: inline-block;
  }
  .selected {
    display: block;
  }
}
.selected {
  width: 0;
  height: 0;
  border: 14px solid orangered;
  border-left: 14px solid transparent;
  border-top: 14px solid transparent;
  position: absolute;
  bottom: 0;
  right: 0;
  color: white;
  display: none;
  span {
    position: absolute;
    bottom: -14px;
    right: -12px;
    font-weight: bold;
  }
}
.dt {
    position: absolute;
    top: 0;
    right: 0;
    color: #fff;
    background: #ccc;
    opacity: .8;
    padding: 0 2px;
    font-size: 12px;
}
.operations {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  button {
    color: #333;
    background-color: #fff;
    border: 1px solid #c4c6cf;
    height: 28px;
    line-height: 28px;
    width: 86px;
    padding: 0 12px;
    border-radius: 3px;
  }
  a {
    color: #CC9977;
    text-decoration: none;
  }
}

// --------------------------------------------------------------------------------------------可舍去

.add-address {
  width: 890px;
  height: 500px;
  border: 1px solid #dcdee3;
  background: #fff;
  position: fixed;
  left: 50%;
  top: 50%;
  transform: translate(-50% ,-50%);
  z-index: 1000;
  display: none;
}
.next-dialog-header {
  width: 890px;
  height: 48px;
  padding: 12px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  span {
    font-size: 16px;
    color: #333;
  }
  i {
    font-size: 20px;
  }
}
.address-container {
  width: 890px;
  height: 400px;
  padding: 20px;
  overflow-y: scroll;
}
.page-buy {
  width: 425px;
  height: 390px;
  margin: 0 auto;
}
.headTips {
  color: #FF5001;
  font-weight: 500;
}
.region {
  width: 415px;
  height: 29px;
  border: 1px solid #f2f2f2;
  background-color: #f2f2f2;
  line-height: 29px;
  margin: 7px 0 10px 10px;
  position: relative;
  span {
    &:first-child {
      color: #9B9B9B;
      margin: 0 15px;
    }
    &:last-child {
      position: absolute;
      right: 10px;
      top: 50%;
      color: #1470CC;
      transform: translate(0 ,-50%);
    }
  }
}
.currency-head i {
  color: #ff3000;
  margin-right: 3px;
}
.tips {
  color: #999;
  width: 334px;
  height: 29px;
  border: 1px solid #C4C6CF;
  line-height: 29px;
  padding-left: 10px;
  position: relative;
  border-radius: 2px;
  cursor: pointer;
}
.choice {
  position: absolute;
  top: 29px;
  left: 10px;
  border: 1px solid #CCCCCC;
  display: none;
  background-color: white;
  z-index: 1000;
  ul {
    &:first-child {
      display: flex;
      width: 413px;
      height: 30px;
      margin: 0;
      padding: 0;
      justify-content: space-between;
      border-bottom: 1px solid #CCCCCC;
      li {
        flex: 1;
        text-align: center;
        line-height: 30px;
        background-color: #F0F0F0;
        cursor: pointer;
      }
      .aim {
        background-color: #FFF;
      }
    }
  }
}
.address-pack {
  width: 413px;
  height: 330px;
  padding: 5px 10px;
  margin: 0;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
  li {
    color: rgb(0, 0, 0);
    padding: 10px 5px;
    cursor: pointer;
    width: 395px;
    height: 39px;
    &:hover {
      color: #6186D8;
    }
  }
  .yj {
    color: #6186D8;
  }
}
.address-choices {
  width: 415px;
  height: 31px;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  position: relative;
  div {
    i {
      position: absolute;
      right: 7px;
      top: 50%;
      transform: translate(0 ,-50%);
      font-weight: bold;
    }
  }
}
.detail-address {
  width: 415px;
  display: flex;
  align-items: flex-start;
  margin-top: 20px;
  justify-content: flex-end;
  textarea {
    padding: 8px;
    width: 334px;
    height: 54px;
    resize:none;
    outline: none;
    border: 1px solid #C4C6CF;
    border-radius: 2px;
  }
}
.postal-code {
  width: 415px;
  display: flex;
  align-items: center;
  margin-top: 15px;
  justify-content: flex-end;
}
.currency-into {
  outline: none;
  border: 1px solid #C4C6CF;
  border-radius: 2px;
  width: 334px;
  height: 27px;
  padding: 0 8px;
}
.username {
  display: flex;
  align-items: center;
  margin-top: 15px;
}
.phone {
  display: flex;
  align-items: center;
  margin-top: 15px;
  justify-content: flex-end;
  width: 415px;
  div {
    width: 135.8px;
    height: 26px;
    padding: 0 8px;
    border: 1px solid #C4C6CF;
    line-height: 26px;
    position: relative;
    i {
      position: absolute;
      right: 7px;
      top: 50%;
      transform: translate(0 ,-50%);
    }
  }
  input {
    width: 192.5px;
    height: 26px;
    outline: none;
    border: 1px solid #C4C6CF;
    border-radius: 2px;
    padding: 0 8px;
    margin-left: 5px;
  }
}
.storage {
  width: 50px;
  height: 28px;
  padding: 0 12px;
  background-color: slateblue;
  line-height: 28px;
  color: white;
  border-radius: 2px;
  margin: 35px auto 0;
  cursor: pointer;
}
.mask{
    position:fixed;
    left:0;
    right:0;
    top:0;
    bottom:0;
    background-color:#000;
    opacity:0.2;
    display:none;
}
</style>
