<template>
  <div id="evaluate">
    <div class="title">
      <h3>追加评价</h3>
      <span>快乐的你分享完美的使用心得</span>
    </div>
    <div class="container">
      <div class="shop">
        <img :src="shop_info.image" alt="" />
        <span>{{shop_info.title}}</span>
        <strong>¥{{shop_info.price}}.00</strong>
      </div>
      <div class="content">
        <span style="color: #999;">2022-06-25 03:01</span>
        <el-rate
          v-model="score"
          :texts="['1分', '2分', '3分', '4分', '5分']"
          show-text
        />
        <span>您没有填写评价内容</span>
        <el-input
          v-model="textarea"
          maxlength="500"
          placeholder="写写你的感受吧，一不小心就成了评论高手"
          show-word-limit
          rows="4"
          type="textarea"
        />
        <div class="img-upload">
          <div></div>
          <div style="background-position: 100% 0"></div>
          <span>共<i> 0 </i>张,还能上传<i> 9 </i>张</span>
        </div>
      </div>
    </div>
    <div class="submit">
      <el-button type="primary" @click="postComments">发 表</el-button>
    </div>
  </div>
</template>

<script>
import store from '@/store'

export default {
  name: 'userEvaluate',
  props: ['shop_info'],
  data () {
    return {
      score: 0,
      textarea: ''
    }
  },
  methods: {
    postComments () {
      this.$https.post('user/comment/', { id: this.$route.query.id, score: this.score, textarea: this.textarea, goods_id: this.shop_info.id }).then(res => {
        if (res.data.code === 200) {
          this.$router.replace({
            path: '/home'
          })
        } else {
          this.$message({
            type: 'info',
            message: '请输入评论内容'
          })
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped lang="less">
#evaluate {
  background-color: #E8E7E7;
  padding: 25px 0;
}
.title {
  width: 1210px;
  margin: 0 auto 25px;
  h3 {
    font: 700 16px/26px "Microsoft YaHei";
    color: #333;
    margin-bottom: 0;
  }
  span {
    color: #666;
    font-size: 12px;
  }
}
.container {
  width: 1140px;
  height: 346px;
  display: flex;
  background-color: #fff;
  padding: 0;
  .shop {
    padding: 55px 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    border-right: 1px solid #f5f5f5;
    img {
      width: 100px;
      height: 100px;
      margin-bottom: 10px;
    }
    span {
      width: 220px;
      text-align: center;
      color: #666;
      font-size: 12px;
      margin-bottom: 10px;
    }
    strong {
      color: #666;
      font-size: 14px;
      margin-bottom: 10px;
      font-weight: bold;
    }
  }
  .content {
    width: 100%;
    text-align: left;
    padding: 30px 40px 0 40px;
    display: flex;
    flex-direction: column;
    font-size: 12px;
    justify-content: space-around;
    .img-upload {
      display: flex;
      align-items: center;
      margin-bottom: 25px;
      div {
        width: 50px;
        height: 50px;
        margin-right: 10px;
        background-image: url("../../assets/channel/bg-upload.png");
        background-repeat: no-repeat;
        cursor: pointer;
      }
      i {
        font-style: normal;
        color: #EA3636;
      }
    }
  }
}
.submit {
  width: 1140px;
  padding: 30px 0;
  margin: 10px auto 25px;
  background-color: #fff;
}
:deep(.el-textarea__inner) {
  font-size: 12px;
  resize: none;
  padding: 10px 5px 10px 15px;
}
:deep(.el-rate .el-rate__icon.is-active) {
  color: #EA3636;
}
:deep(.el-rate__text) {
  color: #EA3636;
  font-weight: bold;
}
:deep(.el-button) {
  width: 220px;
  height: 48px;
  font-size: 16px;
}
</style>
