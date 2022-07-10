<template>
  <div>
    <footer id="common_bottom">
        <div>
            <i style="background-position: 0 0;"></i>
            <span>品类齐全，轻松购物</span>
        </div>
        <div>
            <i style="background-position: 50% 0;"></i>
            <span>多仓直发，极速配送</span>
        </div>
        <div>
            <i style="background-position: 100% 0;"></i>
            <span>正品行货，精致服务</span>
        </div>
        <div>
            <i style="background-position: 0 100%;"></i>
            <span>天天低价，畅选无忧</span>
        </div>
    </footer>
    <hr/>
    <div id="tail">
        <ul>
            <li>购物指南</li>
            <li>免费注册</li>
            <li>会员等级</li>
            <li>常见问题</li>
        </ul>
        <ul>
            <li>支付方式</li>
            <li>网银支付</li>
            <li>快捷支付</li>
            <li>分期付款</li>
            <li>货到付款</li>
            <li>任性付支付</li>
        </ul>
        <ul>
            <li>物流配送</li>
            <li>运费政策</li>
            <li>物流配送服务</li>
            <li>签收验货</li>
            <li>物流查询</li>
        </ul>
        <ul>
            <li>售后服务</li>
            <li>退换货政策</li>
            <li>贵就赔</li>
            <li>维修/安装</li>
            <li>订单修改</li>
            <li>退换货申请</li>
            <li>我的发票</li>
        </ul>
        <ul>
            <li>商家服务</li>
            <li>合作招商</li>
            <li>培训中心</li>
            <li>广告服务</li>
            <li>商家帮助</li>
            <li>服务市场</li>
            <li>规则中心</li>
        </ul>
        <ul>
            <li>身边优购</li>
            <li>全国300多个城市，上万个门店和服务终端期待您的光临，为您提供贴心的服务!</li>
        </ul>
    </div>
    <div id="statement">
        <ul>
            <li>关于我们</li>｜
            <li>联系我们</li>｜
            <li>招聘人才</li>｜
            <li>友情链接</li>
        </ul>
        <span>CopyRight © 2022 成都星期天购物信息技术有限公司 All Rights Reserved</span>
        <span>电话：010-****888 京ICP备*******8号</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'tail'
}
</script>

<style scoped lang="less">
  #common_bottom {
      display: flex;
      width: 1155px;
      justify-content: space-between;
      margin: 50px auto 10px;
      div {
        display: flex;
        align-items: center;
      }
      i {
        background-image: url('../../assets/backImage/footer_tips.png');
        width: 36px;
        height: 42px;
        background-repeat: no-repeat;
        background-size: 113px 86.5px;
      }
      span {
        margin-left: 15px;
        font-size: 18px;
        font-weight: 400;
        color: #444;
      }
  }
  #tail {
      width: 1155px;
      height: 200px;
      margin: 15px auto 0;
      display: flex;
      justify-content: space-between;
      ul {
        li {
          width: 158px;
          height: 22px;
          color: #666;
          font-size: 12px;
          font-weight: 400;
          margin-bottom: 5px;
          &:nth-child(1) {
            font-size: 14px;
            line-height: 22px;
            font-weight: 400;
          }
        }
      }
  }
  #statement {
    width: 100%;
    height: 85px;
    background-color: #F4F4F4;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 12px;
    color: #4e4e4e;
    margin-top: 25px;
    ul {
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 0;
      margin: 0;
    }
  }
</style>
