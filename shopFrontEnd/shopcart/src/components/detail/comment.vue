<template>
  <div class="comments" v-for="i in comments">
    <div class="user">
    <img :src="i.head_portrait" alt="" />
    <div class="name"> ****{{i.username.slice(-1)}}</div>
  </div>
    <div class="content">
      <el-rate v-model="i.grade" disabled/>
      <span class="comment">{{i.content}}</span>
      <div class="operation">
        <span>{{i.create_date}}</span>
        <div>
          <span>举报</span>
          <span>分享</span>
          <span><img src="@/assets/backImage/give_the_thumbs_up.png" alt=""/>0</span>
          <span><img src="@/assets/backImage/comment.png" alt=""/>0</span>
        </div>
      </div>
      <el-divider />
    </div>
  </div>
</template>

<script>
export default {
  name: 'comment',
  props: ['comments'],
  data () {
    return {
      score: 5
    }
  }
}
</script>

<style scoped lang="less">
.comments {
  display: flex;
  width: 100%;
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
