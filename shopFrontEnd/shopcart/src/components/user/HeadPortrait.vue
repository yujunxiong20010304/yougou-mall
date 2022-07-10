<template>
  <div id="head-portrait">
    <div class="title">
      <div>自定义头像</div>
      <span class="iconfont" @click="close_head_portrait">&#xeca0;</span>
    </div>
    <div class="tips">
      <el-upload
        ref="upload"
        action="http://localhost:8000/user/upimage/"
        :headers="config"
        :on-progress="upLoad"
        :before-upload="beforeAvatarUpload"
        :file-list="fileList"
        list-type="picture-card"
        :on-success="handleAvatarSuccess"
        :auto-upload="false">
        <div class="upImage">上传头像</div>
      </el-upload>
      <span>支持大小不超过 5M 的jpg，png的图片</span>
    </div>
    <div id="content">
      <div class="show">
        <img :src="fileList[0]?.url" alt="" />
      </div>
      <div class="preview">
        <span>预览</span>
        <div :style="{backgroundImage: 'url('+fileList[0]?.url+')'}"></div>
        <el-progress type="circle" v-show="progressFlag" :percentage="loadProgress" :status="transmission" class="progress"></el-progress>
      </div>
    </div>
    <div class="operation">
      <span @click="submitUpload">保存</span>
      <span @click="close_head_portrait">取消</span>
    </div>
  </div>
</template>

<script>
import emitter from '@/utils/event'
export default {
  name: 'HeadPortrait',
  data () {
    return {
      fileList: [],
      token: '',
      progressFlag: false,
      loadProgress: 0,
      timer: null,
      timer2: null,
      transmission: 'success'
    }
  },
  computed: {
    config () {
      return { Authorization: `JWT ${this.token}` }
    }
  },
  methods: {
    // 头像上传成功
    handleAvatarSuccess (response, file, fileList) {
      if (response.code === 200) {
        emitter.emit('image', { aim: response.data })
        this.timer = setInterval(() => {
          if (this.loadProgress < 100) {
            this.loadProgress++
            if (this.loadProgress === 100) {
              clearInterval(this.timer)
              this.timer = null
              clearInterval(this.timer2)
              this.timer2 = null
              this.$message({ message: '上传成功', type: 'success' })
            }
          }
        }, 10)
      } else {
        this.transmission = 'exception'
        this.$message.error('上传失败请稍后重试')
      }
    },
    upLoad (event, file, fileList) {
      this.progressFlag = true
      this.timer2 = setInterval(() => {
        this.loadProgress++
        if (this.loadProgress > 72) {
          clearInterval(this.timer2)
          // 这里必须使用this.timer = null，否则清除定时器无效
          this.timer2 = null
        }
      }, 100)
    },
    // 点击上传头像
    submitUpload () {
      this.token = this.$store.state.token
      this.loadProgress = 0
      this.$refs.upload.submit()
    },
    // 关闭头像选择
    close_head_portrait () {
      emitter.emit('show', { aim: false })
      this.progressFlag = false
      this.loadProgress = 0
      this.fileList = []
    },
    // 上传文件的限制
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/png' || 'image/jpeg'
      const isLt5M = file.size / 1024 / 1024 < 5

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG/PNG 格式!')
      }
      if (!isLt5M) {
        this.$message.error('上传头像图片大小不能超过 5MB!')
      }
      return isJPG && isLt5M
    }
  },
  watch: {
    fileList: {
      handler (newVal, oldVal) {
        if (newVal.length > 1) {
          newVal.splice(0, 1)
          this.progressFlag = false
          this.loadProgress = 0
        }
      },
      deep: true
    }
  }
}
</script>

<style scoped lang="less">
#head-portrait {
  width: 500px;
  height: 400px;
  z-index: 2;
  border: 4px solid #BF809F;
  background-color: #fff;
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, 20px);
  .title {
    width: 90%;
    height: 48px;
    border-bottom: 1px solid #ddd;
    margin: 0 auto;
    position: relative;
    div {
      border-bottom: 2px solid black;
      width: 90px;
      height: 48px;
      line-height: 48px;
      text-align: center;
      font-size: 12px;
    }
    span {
      position: absolute;
      right: -19px;
      top: 5px;
      cursor: pointer;
    }
  }
}
.tips {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  font-size: 12px;
  height: 52px;
  width: 444px;
  margin: 0 auto;
  .upImage {
    width: 100px;
    height: 32px;
    border: 1px solid #C2C2C2;
    background-color: #fafafa;
    text-align: center;
    line-height: 32px;
    cursor: pointer;
  }
}
#content {
  width: 442px;
  border: 1px solid #DDDDDD;
  height: 237px;
  margin: 0 auto;
  display: flex;
  .show {
    width: 260px;
    border-right: 1px solid #DDD;
    display: flex;
    justify-content: center;
    overflow: hidden;
    img {
      height: 237px;
    }
  }
  .preview {
    width: 179px;
    display: flex;
    flex-direction: column;
    position: relative;
    span {
      margin: 30px 0 10px 30px;
      font-size: 12px;
      font-weight: bold;
    }
    div {
      width: 108px;
      height: 108px;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      margin-left: 45px;
      border-radius: 50%;
    }
    .progress {
      position: absolute;
      z-index: -1;
      top: 50px;
      left: -9px;
      width: 125px;
      height: 125px;
    }
  }
}
.operation {
  width: 235px;
  height: 50px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  span {
    width: 100px;
    height: 32px;
    text-align: center;
    line-height: 32px;
    border: 1px solid #C2C2C2;
    cursor: pointer;
    border-radius: 5px;
    &:first-child {
      background-color: #6C9AE1;
      color: #fff;
      border: 0;
    }
  }
}
:deep(.el-upload-list__item) {
  display: none;
}
:deep(.el-upload--picture-card) {
  width: 100px;
  height: 32px;
  margin-right: 15px;
  border: 0;
}
</style>
