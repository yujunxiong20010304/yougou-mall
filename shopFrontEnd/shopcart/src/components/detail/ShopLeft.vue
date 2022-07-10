<template>
  <!-- 商品图片展示 -->
  <div class="preview-wrap">

    <div id="spec-img" @mouseover="showCover" @mouseout="hideCover" @mousemove="moveCover" ref="specImage">
      <div class="move-cover" ref="cover"></div>
      <img v-if="show_images" :src="show_images[0]" alt="" class="s-i-img" ref="showImage"/>
      <div class="box-img" ref="container" @mousemove="moveImg">
        <img v-if="show_images" :src="show_images[0]" alt="" class="big-img" ref="hideImage"/>
      </div>
    </div>

    <div class="select-display">
      <i class="iconfont sd" @click="leftBtn">&#xeb9d;</i>
      <div class="lh-box" ref="box">
        <ul class="lh" ref="images">
          <li v-for="(item,index) in show_images" :key="index">
            <img :src="item" alt="" @mouseover="pictureSwitching($event,index)" :class="[index === aim?'choice':'']"/>
          </li>
        </ul>
      </div>
      <i class="iconfont sd" @click="rightBtn">&#xe642;</i>
    </div>

    <div class="preview-info">
      <div class="left-btns">
          <span><i class="iconfont btn-ic">&#xe65d;</i>关注</span>
          <span><i class="iconfont btn-ic">&#xe647;</i>分享</span>
      </div>
      <span>举报</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'shopLeft',
  data () {
    return {
      aim: '0'
    }
  },
  props: ['show_images'],
  methods: {
    pictureSwitching (e, n) {
      let src = e.target.src
      this.$refs.showImage.src = src
      this.$refs.hideImage.src = src
      this.aim = n
    },
    showCover () {
      this.$refs.cover.style.display = 'block'
      this.$refs.container.style.display = 'block'
      // 少了一个东西处理
    },
    hideCover () {
      this.$refs.cover.style.display = 'none'
      this.$refs.container.style.display = 'none'
      // 少了一个东西处理
    },
    moveCover (e) {
      let box = this.$refs.specImage
      let cover = this.$refs.cover
      let mouseX = e.pageX - box.offsetLeft
      let mouseY = e.pageY - box.offsetTop
      cover.style.left = mouseX - cover.clientHeight / 2 + 'px'
      cover.style.top = mouseY - cover.clientHeight / 2 + 'px'
      // 限制左右遮照层不会跑出去
      if (cover.offsetLeft < 0) {
        cover.style.left = 0
      } else if (cover.offsetLeft > box.clientWidth - cover.clientWidth) {
        cover.style.left = box.clientWidth - cover.clientWidth + 'px'
      }
      // 限制遮照层上下不会跑出去
      if (cover.offsetTop < 0) {
        cover.style.top = 0
      } else if (cover.offsetTop > box.clientHeight - cover.clientHeight) {
        cover.style.top = box.clientHeight - cover.clientHeight + 'px'
      }
      this.$refs.hideImage.style.left = -cover.offsetLeft * 2.5 + 'px'
      this.$refs.hideImage.style.top = -cover.offsetTop * 2.5 + 'px'
    },
    moveImg () {
      this.$refs.container.style.display = 'none'
    },
    leftBtn () {
      if (this.show_images.length > 5) {
        let box = this.$refs.box
        let ul = this.$refs.images
        if (ul.offsetLeft - box.offsetLeft) {
        // 判断进行长距离跳跃
          ul.style = 'left: 0; transition: all .7s'
        }
      }
    },
    rightBtn () {
      if (this.show_images.length > 5) {
        let box = this.$refs.box
        let ul = this.$refs.images
        let x = ul.clientWidth - box.clientWidth
        if (box.offsetLeft - ul.offsetLeft - x) {
        // 单次移动长度
          ul.style.left = -x + 'px'
          ul.style.transition = 'all .7s'
        }
      }
    }
  }
}
</script>

<style scoped lang="less">
.preview-wrap {
  width: 352px;
  height: 464px;
  #spec-img {
    width: 350px;
    height: 350px;
    margin-bottom: 20px;
    border: 1px solid #eee;
    cursor: move;
    position: relative;
    .move-cover {
      width: 200px;
      height: 200px;
      background-color: springgreen;
      opacity: 0.5;
      position: absolute;
      display: none;
    }
    .s-i-img {
      width: 348px;
      height: 348px;
    }
    .box-img {
      width: 500px;
      height: 500px;
      position: absolute;
      overflow: hidden;
      top: 0;
      left: 355px;
      display: none;
      z-index: 2;
      border: 1px solid #ccc;
      .big-img {
        width: 875px;
        position: relative;
      }
    }
  }

  .select-display {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 18px;
    .sd {
      font-size: 35px;
      color: #dfdfdf;
      width: 22px;
      height: 32px;
      line-height: 32px;
      cursor: pointer;
      font-weight: bold;
      display: flex;
      align-items: center;
      justify-content: center;
      &:hover {
        color: #ccc;
      }
    }
    .lh-box {
      position: relative;
      width: 290px;
      height: 54px;
      overflow: hidden;
      .lh {
        top: 0;
        left: 0;
        display: flex;
        padding-left: 0;
        margin-bottom: 0;
        position: absolute;
        .choice {
          border: 2px solid red;
        }
        li {
          margin: 0 2px;
          cursor: pointer;
          img {
            width: 54px;
            height: 54px;
            border: 2px solid #fafafa;
          }
        }
      }
    }
  }

  .preview-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 20px;
    span {
      color: #666;
      font-size: 12px;
      &:hover {
        color: #F30113;
        cursor: pointer;
      }
    }
    .left-btns {
      display: flex;
      width: 100px;
      justify-content: space-between;
      span {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 43px;
      }
      .btn-ic {
        color: #E3393C;
        font-size: 16px;
      }
    }
  }

}
</style>
