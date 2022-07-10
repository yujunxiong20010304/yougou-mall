<template>
  <div id="register">
    <div class="title">优购</div>
    <article id="content">
      <h2>用户注册</h2>
      <el-form :rules="RegisterRules" ref="register_info" :model="register_info" class="demo-ruleForm" status-icon :hide-required-asterisk="true">
        <el-form-item prop="username" label="用户名">
          <el-input type="text" auto-complete="false" v-model="register_info.username" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="设置密码">
          <el-input type="text" auto-complete="false" v-model="register_info.password" placeholder="password"></el-input>
        </el-form-item>
        <el-form-item prop="surePassword" label="确认密码">
          <el-input type="text" auto-complete="false" v-model="register_info.surePassword" placeholder="confirm password"></el-input>
        </el-form-item>
        <el-form-item prop="email" label="邮箱">
          <el-input type="text" auto-complete="false" v-model="register_info.email" placeholder="email"></el-input>
        </el-form-item>
        <div class="login">
          <router-link to="/oauth/login/">已有账户？登录</router-link>
        </div>
        <el-button type="primary" @click="submitRegister">提交</el-button>
      </el-form>
    </article>
  </div>
</template>
<script>
import { ElMessageBox } from 'element-plus'
export default {
  name: 'register',
  data () {
    return {
      register_info: {
        username: '',
        password: '',
        surePassword: '',
        email: ''
      },
      RegisterRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 4, max: 20, message: '用户名长度为4～20位字符', trigger: 'blur' },
          { validator: this.UsernameVerification, message: '当前用户名已存在', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 6, max: 20, message: '密码长度为6～20个字符' }
        ],
        surePassword: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { validator: this.passwordAgreement, message: '两次输入密码不一致', trigger: 'blur' }
        ],
        email: [
          { required: true, message: '请输入邮箱账号', trigger: 'blur' },
          { validator: this.EmailStandard, message: '请输入正确的邮箱', trigger: 'blur' },
          { validator: this.EmailRepeatVerification, message: '当前邮箱已存在', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitRegister () {
      this.$refs.register_info.validate((valid) => {
        if (valid) {
          this.$http.post('oauth/register/',
            {
              username: this.register_info.username,
              password: this.$jsEncrypt(this.register_info.password, this.$store.state.publicKey),
              surePassword: this.register_info.surePassword,
              email: this.register_info.email
            }
          ).then(res => {
            if (res.data.msg === 'success') {
              ElMessageBox.confirm(
                '立即前往邮箱完成账号激活',
                '注册成功',
                {
                  confirmButtonText: 'OK',
                  cancelButtonText: 'Cancel',
                  type: 'success'
                }
              )
                .then(() => {
                  window.location.href = 'https://mail.qq.com/'
                })
                .catch(() => {
                  this.$refs.register_info.resetFields()
                })
            } else {
            }
          }).catch(err => {
            console.log(err)
          })
        } else {
          console.log('失败')
        }
      })
    },
    // 判断用户名是否已有
    UsernameVerification (rule, value, callback) {
      this.$https.post('user/user_repeat/', { value: value, only: 0 }).then(res => {
        if (res.data.code === 200) {
          if (res.data.state) {
            callback()
          } else {
            callback(new Error('当前用户名已存在'))
          }
        } else {
          callback(new Error('当前用户名已存在'))
        }
      }).catch(err => {
        console.log(err)
      })
    },
    // 确认密码是否正确
    passwordAgreement (rule, value, callback) {
      if (value === this.register_info.password) {
        callback()
      } else {
        callback(new Error('两次输入密码不一致'))
      }
    },
    // 邮箱规范验证
    EmailStandard (rule, value, callback) {
      if (
        !/^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/.test(
          value
        ) || value.length > 225
      ) {
        callback(new Error('请输入正确的邮箱'))
      } else {
        callback()
      }
    },
    // 邮箱重复验证
    EmailRepeatVerification (rule, value, callback) {
      this.$https.post('user/user_repeat/', { value: value, only: 2 }).then(res => {
        if (res.data.code === 200) {
          if (res.data.state) {
            callback()
          } else {
            callback(new Error('当前邮箱已存在'))
          }
        } else {
          callback(new Error('当前邮箱已存在'))
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
}
</script>
<style scoped lang="less">
#register {
  width: 100%;
  background-position: center;
  background-size: cover;
  background-repeat: no-repeat;
  overflow: hidden;
  background-image: url('../../assets/backImage/register.jpeg');
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
  #content {
    width: 435px;
    height: 395px;
    background-color: rgba(255, 255, 255, 0.7);
    margin: 75px auto 100px;
    display: flex;
    flex-direction: column;
    padding: 45px 55px;
    border-radius: 5px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1), 0 3px 10px rgba(0, 0, 0, 0.07);
    box-sizing: content-box;
    :deep(.el-form-item__label) {
      width: 68px;
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
    }
    :deep(.el-button) {
      width: 169px;
      height: 43px;
    }
    h2 {
      color: #fff;
      font-weight: 700;
      font-size: 25px;
      text-align: center;
      margin-bottom: 15px;
    }
    .login {
      text-align: right;
      font-size: 12px;
      margin-bottom: 5px;
      a{
        text-decoration: none;
      }

    }
  }
}
</style>
