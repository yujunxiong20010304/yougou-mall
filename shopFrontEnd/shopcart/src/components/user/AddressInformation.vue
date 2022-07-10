<template>
  <div class="address" @click.self="closeSelectAddress">
    <div class="title">收货地址</div>
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
        <div class="storage">
          <span @click="addUserAddress()">添加</span>
          <span @click="addUserAddress(1,ID)">修改</span>
        </div>
      </div>
    <div class="notice"><i class="iconfont">&#xe6aa;</i>已保存了{{address_info.length}}条地址，还能保存14条地址</div>
    <table>
      <colgroup>
        <col style="width: 8%;">
        <col style="width: 20%;">
        <col style="width: 20%;">
        <col style="width: 12%;">
        <col style="width: 13%;">
        <col style="width: 11%;">
      </colgroup>
      <thead>
        <tr>
          <th>收货人</th>
          <th>所在地区</th>
          <th>详细地址</th>
          <th>邮编</th>
          <th>电话/手机</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody v-for="(item,index) in address_info" :key="item.id">
        <tr>
          <td>{{item.name}}</td>
          <td><span v-for="value in item.city_address" :key="value[1]" style="margin-right: 7px;">{{value[0]}}</span></td>
          <td>{{item.detailed_address}}</td>
          <td>{{item.postal_code}}</td>
          <td>86-{{item.phone}}</td>
          <td>
            <div class="address-operation">
              <span @click="updateAddress(index)">修改</span>
              <span @click="deleteAddress(item.id)">删除</span>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  name: 'AddressInformation',
  data () {
    return {
      address_info: '', // 用户收货的全部地址
      explicit_address: '', // 详细地址
      postal_code: '', // 邮政编码
      receiving: '', // 收货人的姓名
      phone: '', // 手机号码
      goal: '0', // 标注选中的省/市/区列表中的地址
      sign: '',
      ID: '', // 需要修改的地址的id
      detail_address: '', // 详细地址
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
    // 关闭地址选择
    closeSelectAddress () {
      this.$refs.choice.style = 'display: none'
    },
    // 删除收货地址
    deleteAddress (id) {
      this.$https.post('user/delete_address/', { id: id }).then(res => {
        if (res.data.code === 200) {
          this.getUserAddress()
        }
      }).catch(err => {
        console.log(err)
      })
    },
    getUserAddress () {
      // 请求用户的收货地址(新)
      this.$https.post('user/address/').then(res => {
        if (res.data.code === 200) {
          this.address_info = res.data.data.city_address
        }
      }).catch(err => {
        console.log(err)
      })
    },
    updateAddress (aim) {
      this.ID = this.address_info[aim].id
      this.receiving = this.address_info[aim].name
      this.explicit_address = this.address_info[aim].detailed_address
      this.address = JSON.parse(JSON.stringify(this.address_info[aim].city_address)) // 深拷贝
      this.phone = this.address_info[aim].phone
      this.postal_code = this.address_info[aim].postal_code
      for (let i = 0; i < this.address.length; i++) {
        this.$refs[`address${i}`][0].setAttribute('data-id', this.address[i][1])
      }
      this.$refs[`address${0}`][0].className = 'aim'
      this.goal = '0'
      this.sign = this.address[0][1]
      this.$emit('childClick')
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
    addUserAddress (type, id) { // 收货信息id， 用于修改
      let text = '恭喜你，修改成功'
      if (type) { // 修改
        if (!id) {
          this.$message({
            message: '警告哦，请选择要修改的地址',
            type: 'warning'
          })
          return
        }
      } else { // 添加
        id = ''
        text = '恭喜你，添加成功'
      }
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
          this.clearInput()
          this.ID = ''
          this.$message({
            message: text,
            type: 'success'
          })
        }
      }).catch(err => {
        console.log(err)
      })
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
    // 请求收货地址
    getAddress (id, type) {
      this.$https.post('store/address/', { id: id, type: type }).then(res => {
        this.detail_address = res.data.data.address
      }).catch(err => {
        console.log(err)
      })
    }
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
  },
  created () {
    this.getUserAddress()
  }
}
</script>

<style scoped lang="less">
.address {
  text-align: left;
  font-size: 12px;
}
.title {
  width: 100%;
  height: 30px;
  background-color: #409EFF;
  text-align: left;
  line-height: 30px;
  color: #fff;
  padding-left: 25px;
  font-size: 12px;
  border-radius: 2px;
}
.page-buy {
  width: 425px;
  height: 390px;
  margin-top: 15px;
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
  width: 100%;
  height: 28px;
  padding: 0 12px;
  line-height: 28px;
  margin-top: 35px;
  color: white;
  border-radius: 2px;
  cursor: pointer;
  display: flex;
  justify-content: center;
  span {
    display: inline-block;
    width: 50px;
    height: 28px;
    background-color: slateblue;
    padding: 0 12px;
    cursor: pointer;
    margin: 0 9px;
  }
}
.notice {
  height: 52px;
  width: 100%;
  background-color: #E4F2FE;
  color: #666;
  border-color: #e3f2fd;
  border-style: solid;
  border-radius: 3px;
  display: flex;
  align-items: center;
  padding-left: 25px;
  margin-bottom: 20px;
  i {
    font-size: 18px;
    color: #4495F9;
    margin-right: 5px;
  }
}
table {
  width: 100%;
  margin-bottom: 45px;
  tbody {
    &:hover tr{
      background-color: #F2F3F7;
      cursor: pointer;
      transition: all .5s;
    }
  }
}
thead {
  border: 1px solid #e0e0e0;
  background: #EBECF0;
}
th,td {
  font-size: 12px;
  height: 39px;
  color: #666;
  font-weight: 400;
  border-left: 1px solid #e0e0e0;
  border-right: 1px solid #e0e0e0;
  border-bottom: 1px solid #e0e0e0;
  text-align: left;
  padding-left: 16px;
}
.address-operation {
  display: flex;
  justify-content: center;
  padding-right: 16px;
  span {
    margin: 0 5px;
    cursor: pointer;
    &:hover {
      color: #409EFF;
    }
  }
}
</style>
