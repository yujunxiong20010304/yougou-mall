<template>
  <div id="main">
    <div class="title">优购</div>
    <div class="content">
      <div id="container">
      <div class="header">
        <span>用户登录</span>
        <router-link to="/oauth/register/">注册账户</router-link>
      </div>
      <el-form :rules="LoginRules" ref="login_info" :model="login_info" class="demo-ruleForm" status-icon :hide-required-asterisk="true">
        <el-form-item prop="username" label="用户名">
          <el-input type="text" auto-complete="false" v-model="login_info.username" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="密码">
          <el-input type="text" auto-complete="false" v-model="login_info.password" placeholder="password"></el-input>
        </el-form-item>
        <el-form-item prop="key" label="验证码">
          <el-input type="text" auto-complete="false" v-model="login_info.key" placeholder="verification code"></el-input>
          <img :src="imageUrl" alt="" id="verification" @click="getVerificationCode" v-if="imageUrl"/>
          <input v-model="login_info.hashKey" type="hidden"/>
        </el-form-item>
      </el-form>
      <div class="password">
        <label for="memory" style="display: flex; align-items: center">
          <input type="checkbox" id="memory" style="margin-right: 5px"/>
          <a class="password-choice">记住密码</a>
        </label>
        <a href="javascript:" class="password-choice">忘记密码</a>
      </div>
      <el-button type="primary" @click="userLogin" class="login">登录</el-button>
    </div>
      <div class="division">
        <div>
          or
        </div>
      </div>
      <div id="other">
        <h5>Log in with a third-party account</h5>
        <ul>
          <li style="background-color: #409EFF;">
            <div class="iconfont" style="background-color: #398DE3;">&#xe882;</div>
            <span>Sign In with QQ</span>
          </li>
          <li style="background-color: #67C33A;">
            <div class="iconfont" style="background-color: #5BAC33;">&#xe600;</div>
            <span>Sign In with WeChat</span>
          </li>
          <li style="background-color: #F56C6C;">
            <div class="iconfont" style="background-color: #D95F5F;">&#xe65a;</div>
            <span>Sign In with MicroBlog</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { setItem } from '@/utils/storage'
export default {
  name: 'login',
  data () {
    return {
      imageUrl: '', // 验证码图片
      login_info: {
        username: 'admin',
        password: '123456',
        key: '', // 用户提交的验证码
        hashKey: ''// 加密验证码
      },
      LoginRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 4, max: 20, message: '用户名长度为4～20位字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '密码长度为6～20个字符' }
        ],
        key: [
          { required: true, message: '请输入验证码', trigger: 'blur' },
          { len: 4, message: '请输入正确的验证码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 验证码
    async getVerificationCode () {
      const { data: res } = await this.$http.get('oauth/refresh_captcha/')
      this.login_info.hashKey = res.hashkey
      this.imageUrl = 'http://127.0.0.1:8000' + res.image_url
    },
    // 用户登录
    userLogin () {
      this.$refs.login_info.validate((valid) => {
        if (valid) {
          this.$https.post('oauth/login/',
            { username: this.login_info.username, password: this.$jsEncrypt(this.login_info.password, this.$store.state.publicKey), key: this.login_info.key, hashKey: this.login_info.hashKey })
            .then(res => {
              if (res.data.code !== 404) {
                // setItem('refresh', res.data.refresh)
                this.$store.commit('mSetTokenInfo', res.data.access)
                this.$router.push('/home')
              } else {
                if (res.data.status === 0) {
                  this.$message({
                    message: '账号或密码错误',
                    type: 'warning'
                  })
                  this.login_info.key = ''
                } else if (res.data.status === 1) {
                  this.$message({
                    message: '验证码错误',
                    type: 'warning'
                  })
                  // 清空验证码输入栏
                  this.login_info.key = ''
                }
                this.getVerificationCode()
              }
            }).catch(error => {
              console.log(error)
            })
        } else {
          console.log('失败')
        }
      })
    }
  },
  created () {
    this.getVerificationCode()
  }
}
</script>

<style scoped lang="less">
#main {
  width: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  overflow: hidden;
  background-image: url('../../assets/backImage/login.jpeg');
  .title {
    height: 88px;
    margin: 0 auto;
    text-align: left;
    line-height: 88px;
    padding-left: 50px;
    font-size: 40px;
    color: white;
    border-bottom: 1px solid white;
  }
  .content {
    width: 873px;
    height: 434px;
    margin: 120px auto 120px;
    display: flex;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1), 0 3px 10px rgba(0, 0, 0, 0.07);
  }
  #container {
    width: 432px;
    height: 364px;
    display: flex;
    flex-direction: column;
    padding: 35px 40px;
    border-bottom-left-radius: 5px;
    border-top-left-radius: 5px;
    background-color: rgba(255, 255, 255, .8);
    box-sizing: content-box;
    :deep(.el-form-item__label) {
      width: 61px;
      text-align: justify;
      height: 40px;
      line-height: 40px;
      &:after {
        display: inline-block;
        width: 100%;
        content: "";
      }
    }
    :deep(.el-form-item) {
      margin-bottom: 31px;
    }
    :deep(.el-form-item__error) {
      margin-top: 5px;
    }
    :deep(.el-input) {
      height: 40px;
      width: 100%;
    }
    :deep(.el-button) {
      width: 169px;
      height: 43px;
    }
    :deep(.el-form-item__content) {
      flex-flow: nowrap;
      width: 371px;
    }
    .login {
      width: 55%;
      height: 37px;
      border: 0;
      border-radius: 5px;
      font-size: 16px;
      color: #fff;
      box-sizing: content-box;
      margin: 0 auto;
    }
    .header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      color: #3c3c3c;
      font-size: 25px;
      font-weight: 700;
      margin-bottom: 25px;
      a {
        text-decoration: none;
        font-size: 14px;
        font-weight: 400;
        color: #3c3c3c;
        &:hover {
          color: red;
        }
      }
    }
    #verification {
      height: 40px;
      width: 125px;
      margin-left: 15px;
    }
    .password {
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #999;
      font: 12px Arial, Helvetica, sans-serif;
      font-weight: 500;
      height: 35px;
      input {
        width: 15px;
        vertical-align: middle;
      }
      .password-choice {
        text-decoration: none; color: #999;
        cursor: pointer;
        &:hover {
          color: #409EFF;
        }
      }
    }
  }
  .division {
    color: #999;
    line-height: 434px;
    height: 434px;
    background-color: rgba(255,255,255,.8);
    display: flex;
    align-items: center;
    div {
      height: 20px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      position: relative;
      &:after {
        content: '';
        display: block;
        height: 72px;
        border-left: 1px solid #999;
        width: 0;
        position: absolute;
        top: 35px;
      }
      &:before {
        content: '';
        display: block;
        height: 72px;
        border-left: 1px solid #999;
        width: 0;
        position: absolute;
        top: -85px;
      }
    }
  }
  #other {
    width: 347px;
    text-align: center;
    background-color: rgba(255, 255, 255, .8);
    border-bottom-right-radius: 5px;
    border-top-right-radius: 5px;
    height: 434px;
    padding: 35px 0;
    h5 {
      color: #999;
    }
    ul {
      height: 195px;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: space-between;
      flex-direction: column;
      align-items: center;
      margin-top: 35px;
      li {
        width: 265px;
        height: 45px;
        display: flex;
        align-items: center;
        justify-content: flex-start;
        cursor: pointer;
        border-radius: 3px;
        overflow: hidden;
        .iconfont {
          font-size: 24px;
          color: #fff;
          height: 100%;
          line-height: 45px;
          text-align: center;
          width: 45px;
        }
        span {
          font-size: 14px;
          color: #fff;
          margin-left: 15px;
        }
      }
    }
  }
}
</style>
