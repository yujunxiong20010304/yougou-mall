<template>
  <div>
    <div class="guarantee">
      <div class="guarantee-title">售后保障</div>
      <div class="guarantee-class">
        <i class="goods"></i>
        <span>京东承诺</span>
      </div>
      <span class="guarantee-content">
        京东平台卖家销售并发货的商品，由平台卖家提供发票和相应的售后服务。请您放心购买！
        <p>注：因厂家会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，
        本司不能确保客户收到的货物与商城图片、产地、附件说明完全一致。只能确保为原厂正货！
            并且保证与当时市场上同样主流新品一致。若本商城没有及时更新，请大家谅解！</p>
      </span>
      <div class="guarantee-class">
        <i class="goods"></i>
        <span>正品行货</span>
      </div>
      <span class="guarantee-content">
        京东商城向您保证所售商品均为正品行货，京东自营商品开具机打发票或电子发票。
      </span>
      <div class="guarantee-class">
        <i class="no-worries"></i>
        <span>无忧退货</span>
      </div>
      <span class="guarantee-content">
        客户购买京东自营商品7日内（含7日，自客户收到商品之日起计算），在保证商品完好的前提下，可无理由退货。（部分商品除外，详情请见各商品细则）
      </span>
    </div>
    <div class="state">
        <span class="state-title">权利声明</span>
        <div>京东上的所有商品信息、客户评价、商品咨询、网友讨论等内容，是京东重要的经营资源，未经许可，禁止非法转载使用。
        <br>
        <strong>注：</strong>本站商品信息均来自于合作方，其真实性、准确性和合法性由信息拥有者（合作方）负责。本站不提供任何保证，并不承担任何法律责任。</div>
        <span class="state-title">价格说明</span>
        <div style="margin: 0;"><strong>京东价：</strong>京东价为商品的销售价，是您最终决定是否购买商品的依据。
        <br><strong>划线价：</strong>商品展示的划横线价格为参考价，并非原价，该价格可能是品牌专柜标价、商品吊牌价或由品牌供应商提供的正品零售价（如厂商指导价、建议零售价等）或其他真实有依据的价格；由于地区、时间的差异性和市场行情波动，品牌专柜标价、商品吊牌价等可能会与您购物时展示的不一致，该价格仅供您参考。
        <br><strong>折扣：</strong>如无特殊说明，折扣指销售商在原价、或划线价（如品牌专柜标价、商品吊牌价、厂商指导价、厂商建议零售价）等某一价格基础上计算出的优惠比例或优惠金额；如有疑问，您可在购买前联系销售商进行咨询。
        <br><strong>异常问题：</strong>商品促销信息以商品详情页“促销”栏中的信息为准；商品的具体售价以订单结算页价格为准；如您发现活动商品售价或促销信息有异常，建议购买前先联系销售商咨询。</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'guarantee'
}
</script>

<style scoped lang="less">
.guarantee {
  margin-top: 20px;
  text-align: left;
}

.guarantee-title {
    width: 968px;
    height: 20px;
    padding: 10px;
    box-sizing: content-box;
    background-color: #f7f7f7;
    border: 1px solid #eee;
    font: 700 14px "microsoft yahei";
    margin-top: 20px;
}
.goods {
    background-position: -32px -75px;
}
.no-worries {
    background-position: 0 -75px;
}
.guarantee-class {
  display: flex;
  align-items: center;
  span {
    font-size: 16px;
    color: #e4393c;
    font-family: "microsoft yahei";
    font-weight: bold;
    margin-left: 15px;
  }
  i {
    background-image: url('../../assets/test/promise.png');
    display: inline-block;
    height: 32px;
    width: 32px;
    background-repeat: no-repeat;
    margin-left: 25px;
  }
}
.guarantee-content {
    color: #666;
    font: 12px/150% tahoma,arial,Microsoft YaHei,Hiragino Sans GB,"\u5b8b\u4f53",sans-serif;
    display: inline-block;
    padding-left: 75px;
    margin-bottom: 25px;
}
.state {
  font-size: 12px;
  color: #666;
  text-align: left;
  div {
    margin-bottom: 45px;
  }
  .state-title {
    color: #e4393c;
    font-weight: bold;
    font-size: 12px;
  }
}
</style>
