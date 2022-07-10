<template>
  <div id="mutual-evaluate">
    <div class="evaluate-info">
      <div class="comments" :style="{'width':(988-0*50+'px')}">
        <div class="user">
        <img src="https://s3.bmp.ovh/imgs/2022/06/26/40ed460764ac49ba.png" alt="" />
        <div class="name">  ****5</div>
      </div>
        <div class="content">
          <el-rate v-model="score" disabled/>
          <span class="comment">很不错，物流很快，第二天货就到了，内容很全面，可以帮助我做一些针对性复习</span>
          <div class="operation">
            <span>2022-06-07 17:12</span>
            <div>
              <span>举报</span>
              <span>分享</span>
              <span><img src="@/assets/backImage/give_the_thumbs_up.png" alt=""/>1</span>
              <span><img src="@/assets/backImage/comment.png" alt=""/>0</span>
            </div>
          </div>
          <el-divider />
        </div>
      </div>
      <div class="comments" :style="{'width':(988-type*25+'px')}">
        <div class="user">
        <img src="https://s3.bmp.ovh/imgs/2022/06/26/40ed460764ac49ba.png" alt="" />
        <div class="name">  ****5</div>
      </div>
        <div class="content">
          <el-rate v-model="score" disabled/>
          <span class="comment">很不错，物流很快，第二天货就到了，内容很全面，可以帮助我做一些针对性复习</span>
          <div class="operation">
            <span>2022-06-07 17:12</span>
            <div>
              <span>举报</span>
              <span>分享</span>
              <span><img src="@/assets/backImage/give_the_thumbs_up.png" alt=""/>1</span>
              <span><img src="@/assets/backImage/comment.png" alt=""/>0</span>
            </div>
          </div>
          <el-divider />
        </div>
      </div>
    </div>
    <div class="shop-info">
      <div class="title">商品信息</div>
      <div class="info">
        <img src="@/assets/backImage/tests.jpeg" alt="" />
        <span>商品名称：<i>2022版万唯中考真题分类卷精选1200题初中英语试卷 万唯教育初三历年真题全国卷试题精选九年级专项训练真题卷分类万维</i></span>
        <span>价格：<i style="color:#E4393C;">¥ 47.90</i></span>
        <span>
          评价得分：<i style="color:#E4393C;">5分</i>
        </span>
        <span>评论数：<i style="color:#E4393C;">0条</i></span>
        <el-button type="primary">加入购物车</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'mutualEvaluate',
  data () {
    return {
      score: 5,
      type: 1
    }
  }
}
</script>

<style scoped lang="less">
#mutual-evaluate {
  display: flex;
  width: 1210px;
  margin: 0 auto;
  justify-content: space-between;
  .evaluate-info {
    width: 988px;
    height: 998px;
    border: 1px solid #F2F2F2;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    .comments {
      display: flex;
      width: 988px;
    }
    .user {
      width: 127px;
      height: 25px;
      margin: 18px 0 0 22px;
      display: flex;
      align-items: center;
      color: #666;
      font-size: 12px;
      word-break: break-all;
      img {
        width: 25px;
        height: 25px;
        border-radius: 50%;
      }
      .name {
        margin-left: 7px;
      }
    }
    .content {
      display: flex;
      flex-direction: column;
      text-align: left;
      width: 100%;
      padding-right: 15px;
      font-size: 12px;
      padding-top: 15px;
      .comment {
        padding: 7px 0 15px;
      }
      .operation {
        display: flex;
        justify-content: space-between;
        color: #666;
        div {
          display: flex;
          span {
            display: flex;
            line-height: 18px;
            margin-left: 15px;
            cursor: pointer;
            &:hover {
              color: #00b3ee;
            }
            img {
              width: 15px;
              height: 15px;
              margin-right: 4px;
            }
          }
        }
      }
    }
  }
  .shop-info {
    width: 210px;
    height: 430px;
    text-align: left;
    border: 1px solid #F2F2F2;
    .title {
      width: 210px;
      height: 30px;
      line-height: 30px;
      padding-left: 10px;
      text-align: left;
      background-color: #F7F7F7;
      color: #333;
      font-size: 14px;
      margin-bottom: 15px;
    }
    .info {
      display: flex;
      flex-direction: column;
      align-items: center;
      font-size: 12px;
      text-align: left;
      img {
        width: 130px;
        height: 130px;
        margin-bottom: 15px;
      }
      span {
        width: 100%;
        margin-bottom: 10px;
        padding: 0 7px;
        color: #666;
        i {
          font-style: normal;
        }
      }
    }
  }
}
:deep(.el-button) {
  width: 130px;
  height: 40px;
  margin-top: 7px;
}
:deep(.el-rate .el-rate__icon.is-active) {
  color: #E4393C;
}
:deep(.el-rate) {
  height: 16px;
}
</style>
