<template>
  <div class="comment">
    <div class="guarantee-title">商品评价</div>
    <div class="comment-sum">
      <div class="comment-grade">
        <span>好评度</span>
        <i>{{goods_score}}%</i>
      </div>
      <span>此商品暂时还没有买家印象哦~</span>
    </div>
    <ul class="comment-choice">
      <li @click="changeJudge(1)">全部评价({{comment_all}}+)</li>
      <li @click="changeJudge(2)" v-if="good_score">好评({{good_score}}+)</li>
      <li @click="changeJudge(3)" v-if="medium_score">中评({{medium_score}})</li>
      <li @click="changeJudge(4)" v-if="difference_score">差评({{difference_score}})</li>
      <li class="iconfont comment-sort">默认排序&#xe610;</li>
    </ul>
    <div class="no-comment" v-if="!comments">「暂无评价」</div>
    <comment v-else :comments="comments"></comment>
    <el-pagination background layout="prev, pager, next" :page-count="page_count" @current-change="SwitchPages" :current-page="index" :hide-on-single-page="true"/>
  </div>
</template>

<script>
import comment from '@/components/detail/comment'
export default {
  name: 'discuss',
  components: {
    comment: comment
  },
  data () {
    return {
      comments: '',
      page_count: 1,
      index: 1,
      comment_all: 0,
      good_score: 0,
      medium_score: 0,
      difference_score: 0,
      goods_score: 100,
      judge: 1
    }
  },
  methods: {
    changeJudge (judge) {
      this.judge = judge
    },
    SwitchPages (index) {
      this.index = index
      this.getComments()
    },
    // 获取用户评论
    async getComments () {
      const { data: res } = await this.$http.post('store/show_comment/',
        { id: this.$route.query.id, index: this.index, judge: this.judge }
      )
      if (res.code === 200) {
        this.comments = res.data.result
        this.timeConversion(res.data.result)
        this.page_count = res.data.page_count
        this.comment_all = res.data.comment_all
        this.good_score = res.data.good_score
        this.medium_score = res.data.medium_score
        this.difference_score = res.data.difference_score
        this.goods_score = res.data.goods_score
      }
    },
    timeConversion (data) {
      for (let i = 0; i < data.length; i++) {
        let time = data[i].create_date.split('T')
        let day = time[0]
        let date = time[1].split(':')
        let hour = date[0] + ':' + date[1]
        data[i].create_date = day + ' ' + hour
      }
    }
  },
  created () {
    this.getComments()
  },
  watch: {
    judge: {
      handler (newVal, oldVal) {
        this.index = 1
        this.getComments()
      },
      deep: true
    }
  }
}
</script>

<style scoped lang="less">
.comment {
  margin-top: 20px;
  .guarantee-title {
    margin-bottom: 15px;
    text-align: left;
    width: 968px;
    height: 20px;
    padding: 10px;
    box-sizing: content-box;
    background-color: #f7f7f7;
    border: 1px solid #eee;
    font: 700 14px "microsoft yahei";
    margin-top: 20px;
  }
}
.comment-grade {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 200px;
  justify-content: center;
  margin-left: 75px;
  span {
    font-size: 12px;
    color: #666;
  }
  i {
    font-style: normal;
    font-size: 45px;
    color: #e4393c;
    font-family: arial;
  }
}
.comment-sum {
  display: flex;
  align-items: center;
  span {
    font-size: 12px;
    color: #666;
  }
}
.comment-choice {
  display: flex;
  font-size: 12px;
  color: #666;
  background-color: #F7F7F7;
  height: 31px;
  width: 988px;
  align-items: center;
  padding: 0;
  margin: 0;
  position: relative;
  li {
    margin: 0 15px;
    cursor: pointer;
    &:hover {
      color: #e4393c;
    }
  }
}
.comment-sort {
  position: absolute;
  right: 10px;
}
.no-comment {
  text-align: center;
  font-size: 12px;
  color: #666;
  height: 55px;
  margin-top: 15px;
}
:deep(.el-pagination) {
  justify-content: center;
  margin: 31px 0;
}
</style>
