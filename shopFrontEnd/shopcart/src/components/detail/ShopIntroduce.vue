<template>
  <div id="left-container">
    <!--芊禧礼品专营店-->
    <div id="popbox-inner">
      <div class="p-i-title">{{shop}}</div>
      <div class="score-parts">
        <span>商品评价<i>9.94 高</i></span>
        <span>物流履约<i>9.26 高</i></span>
        <span>售后服务<i>9.45 高</i></span>
      </div>
      <div class="p-i-btns">
        <div>进店逛逛</div>
        <div>关注店铺</div>
      </div>
    </div>
    <!--店内搜索-->
    <div id="sp-search">
      <div class="p-i-title">店内搜索</div>
      <div class="s-container">
        <div class="sp-form-item">
          <span>关键字：</span><input type="text" style="width: 110px;"/>
        </div>
        <div class="sp-form-item">
          <span style="letter-spacing:3px;">价 格：</span>
          <input type="text" style="width: 46px;margin-right: 5px;"/>
          到
          <input type="text" style="width: 46px;margin-left: 5px;"/>
        </div>
        <button>搜索</button>
      </div>
    </div>
      <!--店门热销-->
      <div id="pop-hot">
        <div class="p-h-title">
          <span @click="changeShow(0)" :class="[0 === aim?'current':'']">店铺热销</span>
          <span @click="changeShow(1)" :class="[1 === aim?'current':'']">热门关注</span>
        </div>
        <!--店铺热销-->
        <ul class="plist-pop" :style="[0 === aim?'display:none':'display:block']">
          <li v-for="(item,index) in shop_list" :key="item.id" @click="enterDetail(item.id)">
            <div class="w-i-container">
              <img :src="item.goods_image" alt="" />
              <span class="w-i-introduce">{{ item.title }}</span>
            </div>
            <div class="w-container">
              <div>
                  <i> {{index+1}} </i>
                  <span style="color: #999;">热销3</span>
              </div>
              <span class="money">¥ {{item.min_price}}.00 </span>
            </div>
          </li>
        </ul>
        <!--热门关注-->
        <ul class="plist-pop" :style="[1 === aim?'display:none':'display:block']">
          <li v-for="(item,index) in recommended" :key="item.id" @click="enterDetail(item.id)">
            <div class="w-i-container">
              <img :src="item.goods_image" alt="" />
              <span class="w-i-introduce">{{ item.title }}</span>
            </div>
            <div class="w-container">
              <div>
                <i> {{index+1}} </i>
                <span style="color: #999;">热销333件</span>
              </div>
              <span class="money">¥ {{item.min_price}}.00</span>
            </div>
          </li>
        </ul>
      </div>
  </div>
</template>

<script>
export default {
  name: 'ShopIntroduce',
  props: ['recommended', 'shop'],
  data () {
    return {
      aim: 0,
      shop_list: ''
    }
  },
  methods: {
    enterDetail (id) {
      const newpage = this.$router.resolve({
        path: '/detail', // 跳转的页面路由
        query: { // 要传的参数
          id: id
        }
      })
      window.open(newpage.href, '_blank')
    },
    async FindGoods () {
      const { data: res } = await this.$http.post('store/goods/', { theme: '鲜花', number: 30, interval: 5 })
      this.shop_list = res.data
    },
    changeShow (value) {
      this.aim = value
    }
  },
  created () {
    this.FindGoods()
  }
}
</script>

<style scoped lang="less">
#left-container {
  width: 210px;
  text-align: left;
}
#popbox-inner {
  width: 210px;
  height: 190.5px;
  border: 1px solid #eee;
  margin-bottom: 15px;
  background-color: #fff;
}
.p-i-title {
  color: #666;
  font: 700 14px "microsoft yahei";
  background-color: #f7f7f7;
  width: 208px;
  height: 40px;
  line-height: 40px;
  padding-left: 15px;
}
.score-parts {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 188px;
  height: 92.5px;
  padding-top: 10px;
  margin: 0 auto;
  border-bottom: 1px solid #eee;
}
.score-parts span {
  font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
  color: #999;
}
.score-parts span i {
  font-style: normal;
  color: #e2231a!important;
  padding-left: 10px;
}
.p-i-btns {
  width: 188px;
  height: 36px;
  margin: 10px;
  display: flex;
}
.p-i-btns div {
  width: 88px;
  height: 34px;
  line-height: 34px;
  padding: 0;
  margin-right: 8px;
  font-size: 12px;
  background-color: #f8f8f8;
  color: #666;
  text-align: center;
  border: 1px solid #eee;
  cursor: pointer;
}
.p-i-btns div:hover {
  color: black;
}
#sp-search {
  width: 210px;
  height: 140.5px;
  border: 1px solid #eee;
  background-color: #fff;
}
.s-container {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 100%;
  height: 100.5px;
}
.sp-form-item {
  display: flex;
  outline: none;
  font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
  color: #666;
  margin-left: 10px;
  align-items: center;
}
.sp-form-item span {
  width: 60px;
  text-align: center;
  height: 18px;
  line-height: 18px;
}
.sp-form-item input {
  height: 21.5px;
}
#sp-search button {
  width: 48px;
  height: 26px;
  margin-left: 70px;
  font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
  border: 1px solid #ddd;
  background-color: white;
}
#pop-hot {
  width: 210px;
  height: 1294px;
  border: 1px solid #eee;
  margin-top: 15px;
}
.p-h-title {
  width: 208px;
  height: 37px;
  border-bottom: 1px solid #e4393c;
  background-color: #f7f7f7;
  display: flex;
}
.p-h-title span {
  width: 104px;
  height: 36px;
  line-height: 36px;
  text-align: center;
  font-size: 14px;
  font-family: "microsoft yahei";
  cursor: pointer;
  color: #666;
}
.p-h-title .current {
  background-color: #e4393c;
  color: #fff;
  cursor: default;
}
.plist-pop {
  padding-left: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 15px 0 0;
}
.plist-pop li {
  width: 188px;
  height: 184px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5px 0;
  margin-bottom: 22px;
  cursor: pointer;
}
.plist-pop li:hover .w-i-introduce{
    display: block;
}
.w-i-container {
    width: 160px;
    height: 160px;
    position: relative;
}
.w-i-container img {
    width: 160px;
    height: 160px;
}
.w-i-introduce {
  position: absolute;
  color: #fff;
  font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
  background: rgba(0,0,0,.7);
  bottom: 0;
  overflow: hidden;
  padding: 0 12px;
  height: 36px;
  display: none;
}
.w-container {
  display: flex;
  width: 188px;
  height: 20px;
  justify-content: space-between;
  font-size: 12px;
  font-family: tahoma, arial, Microsoft, YaHei, Hiragino, Sans, GB, "\u5b8b\u4f53", sans-serif;
  margin-top: 5px;
}
.w-container div i{
  display: inline-block;
  background-color: #E4393C;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  text-align: center;
  line-height: 20px;
  font-style: normal;
  color: #fff;
}
.money {
  font-size: 14px;
  color: #e4393c;
  font-family: Verdana, serif;
  font-weight: bold;
}

</style>
