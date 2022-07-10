<template>
  <div id="account-information">
    <div class="head-image">
      <div class="image" :style="{backgroundImage: 'url('+head_image+')'}"></div>
      <div class="back-image" @click="upload_avatar"><img src="@/assets/verygoods/upload.png" alt=""/></div>
      <span>{{BasicsForm.username}}</span>
    </div>
    <el-tabs style="height: 200px" class="demo-tabs" @tab-change="switchInformation">
      <el-tab-pane label="基础信息修改">
        <el-form :rules="basicRules" ref="BasicsForm" :model="BasicsForm" class="demo-ruleForm" status-icon :hide-required-asterisk="true">
          <el-form-item prop="username" label="用户名">
            <el-input type="text" auto-complete="false" :disabled="modify" v-model="BasicsForm.username" placeholder="请输入用户名"></el-input>
          </el-form-item>
          <el-form-item prop="description" label="个人描述">
            <el-input
              :disabled="modify"
              v-model="BasicsForm.description"
              :rows="5"
              type="textarea"
              placeholder="请输入个人描述"
            />
          </el-form-item>
          <el-form-item prop="payment" label="支付密码">
            <el-input type="password" auto-complete="false" :disabled="modify" v-model="BasicsForm.payment" placeholder="请输入支付密码"></el-input>
          </el-form-item>
          <el-button type="primary" @click="this.modify = false" v-if="modify">修改</el-button>
          <el-button type="success" v-else @click="preservationBasicInformation">保存</el-button>
          <el-button plain v-if="!modify" @click="cancelModify">取消</el-button>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="密码修改">
        <el-form :rules="passwordRules" ref="PassWord" :model="PassWord" class="demo-ruleForm" status-icon>
          <el-form-item prop="InitialPassword" label="原始密码">
            <el-input type="text" auto-complete="false" v-model="PassWord.InitialPassword" placeholder="请输入密码"></el-input>
          </el-form-item>
          <el-form-item prop="NewPassword" label="新密码">
            <el-input type="text" auto-complete="false" v-model="PassWord.NewPassword" placeholder="请输入新密码"></el-input>
          </el-form-item>
          <el-form-item prop="SurePassword" label="确认密码">
            <el-input type="password" auto-complete="false" v-model="PassWord.SurePassword" placeholder="请再次输入新密码"></el-input>
          </el-form-item>
          <el-button type="primary" @click="modifyPassword">提交</el-button>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="邮箱账号修改">
        <el-form :rules="emailRules" ref="Email" :model="Email" class="demo-ruleForm" status-icon>
          <el-form-item prop="email" label="邮箱账号">
            <el-input type="text" auto-complete="false" v-model="Email.email" placeholder="请输入用户名"></el-input>
          </el-form-item>
          <div class="verification">
            <el-form-item prop="verification" label="验证码">
              <el-input type="text" auto-complete="false" v-model="Email.verification" placeholder="请输入用户名"></el-input>
            </el-form-item>
            <el-button @click="GetVerificationCode">获取验证码</el-button>
          </div>
          <el-button type="primary" @click="MailboxModification">提交</el-button>
        </el-form>
      </el-tab-pane>
    </el-tabs>
    <transition name="el-zoom-in-top">
      <headportrait v-show="show" class="transition-box"></headportrait>
    </transition>
  </div>
</template>

<script>
import headportrait from '@/components/user/HeadPortrait'
import emitter from '@/utils/event'
export default {
  name: 'AccountInformation',
  components: {
    headportrait: headportrait
  },
  data () {
    return {
      show: false,
      user_info: '',
      head_image: '',
      verification_code: '',
      BasicsForm: {
        username: '',
        description: '',
        payment: ''
      },
      modify: true,
      PassWord: {
        InitialPassword: '',
        NewPassword: '',
        SurePassword: ''
      },
      Email: {
        email: '',
        verification: ''
      },
      // 2.我们把要进行验证的字段都放进rules对象里
      basicRules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 4, max: 20, message: '用户名长度为4～20位字符', trigger: 'blur' },
          { validator: this.UsernameVerification, message: '当前用户名已存在', trigger: 'blur' }
        ],
        description: [
          { required: true, message: '请输入简介', trigger: 'blur' },
          { max: 225, message: '字符长度不超过255', trigger: 'blur' }
        ],
        payment: [
          { required: true, message: '请输入支付密码', trigger: 'blur' },
          { min: 4, max: 11, message: '支付密码长度为2～11位字符', trigger: 'blur' }
        ]
      },
      passwordRules: {
        InitialPassword: [
          { required: true, message: '请输入原始密码', trigger: 'blur' },
          { min: 6, max: 20, message: '密码长度为6～20个字符' },
          { validator: this.verificationPassword, message: '密码错误', trigger: 'blur' }
        ],
        NewPassword: [
          { required: true, message: '请输入新密码', trigger: 'blur' },
          { min: 6, max: 20, message: '密码长度为6～20个字符' },
          { validator: this.OldNewPassword, message: '新密码与原始密码不能相同', trigger: 'blur' }
        ],
        SurePassword: [
          { required: true, message: '请再次输入新密码', trigger: 'blur' },
          { min: 6, max: 20, message: '密码长度为6～20个字符' },
          { validator: this.passwordAgreement, message: '两次输入密码不一致', trigger: 'blur' }
        ]
      },
      emailRules: {
        email: [
          { required: true, message: '请输入邮箱账号', trigger: 'blur' },
          { validator: this.EmailStandard, message: '请输入正确的邮箱', trigger: 'blur' },
          { validator: this.EmailRepeatVerification, message: '当前邮箱已存在', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 修改邮箱
    MailboxModification () {
      if (this.verification_code) {
        if (this.verification_code !== this.Email.verification) {
          this.Email.verification = ''
          this.$message({
            type: 'error',
            message: '邮箱验证码错误'
          })
        } else {
          this.$refs.Email.validate((valid) => {
            if (valid) {
              this.$https.post('user/update_user_info/', { email: this.Email }).then(res => {
                if (res.data.code === 200) {
                  this.user_info = res.data.data.user_info
                  this.verification_code = ''
                  this.Email.verification = ''
                  this.assignment()
                  this.$message({
                    type: 'success',
                    message: '修改成功'
                  })
                }
              }).catch(err => {
                console.log(err)
              })
            } else {
              console.log('失败')
            }
          })
        }
      } else {
        this.$message({
          type: 'error',
          message: '请获取邮箱验证码'
        })
      }
    },
    // 获取验证码
    GetVerificationCode () {
      this.$refs.Email.validate((valid) => {
        if (valid) {
          this.$https.post('user/send_email/', { email: this.Email.email }).then(res => {
            if (res.data.msg === 'success') {
              this.verification_code = res.data.data.verification_code
              this.$message({
                type: 'success',
                message: '邮箱发送成功'
              })
            } else {
              this.$message({
                type: 'error',
                message: '邮箱发送失败'
              })
            }
          }).catch(err => {
            console.log(err)
          })
        } else {
          console.log('失败', valid)
        }
      })
    },
    // 邮箱规范验证
    EmailStandard (rule, value, callback) {
      this.verification_code = ''
      this.Email.verification = ''
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
      this.verification_code = ''
      this.Email.verification = ''
      this.$https.post('user/user_repeat/', { value: value, only: 2 }).then(res => {
        if (res.data.code === 200) {
          if (res.data.state) {
            callback()
          } else {
            callback(new Error('当前邮箱已存在'))
          }
        }
      }).catch(err => {
        console.log(err)
      })
    },
    // 密码修改
    modifyPassword () {
      this.$refs.PassWord.validate((valid) => {
        if (valid) {
          this.$https.post('user/update_user_info/', { password: this.$jsEncrypt(this.PassWord, this.$store.state.publicKey) }).then(res => {
            if (res.data.code === 200) {
              this.$refs.PassWord.resetFields()
              this.$message({
                type: 'success',
                message: '修改完成'
              })
            }
          }).catch(err => {
            console.log(err)
          })
        } else {
          console.log('失败')
        }
      })
    },
    // 验证密码是否正确
    verificationPassword (rule, value, callback) {
      this.$https.post('user/user_repeat/', { value: value, only: 1 }).then(res => {
        if (res.data.code === 200) {
          if (res.data.state) {
            callback()
          } else {
            callback(new Error('密码错误'))
          }
        }
      }).catch(err => {
        console.log(err)
      })
    },
    // 密码一致性检验
    passwordAgreement (rule, value, callback) {
      if (value === this.PassWord.NewPassword) {
        callback()
      } else {
        callback(new Error('两次输入密码不一致'))
      }
    },
    // 新密码与原始密码不能一致
    OldNewPassword (rule, value, callback) {
      if (value === this.PassWord.InitialPassword) {
        callback(new Error('新密码与原始密码不能相同'))
      } else {
        callback()
      }
    },
    // 信息切换
    switchInformation (TabPanelName) {
      if (TabPanelName === '1') {
        this.$refs.PassWord.clearValidate()
        this.$refs.PassWord.resetFields()
      }
      if (TabPanelName === '0') {
        this.modify = true
        this.$refs.BasicsForm.clearValidate()
        this.assignment()
      }
      if (TabPanelName === '2') {
        this.$refs.Email.clearValidate()
      }
    },
    // 保存基本信息的修改
    preservationBasicInformation () {
      this.$refs.BasicsForm.validate((valid) => {
        if (valid) {
          this.$https.post('user/update_user_info/', { basic: this.BasicsForm }).then(res => {
            if (res.data.code === 200) {
              this.user_info = res.data.data.user_info
              this.assignment()
              this.modify = true
              this.$refs.BasicsForm.clearValidate()
            }
          }).catch(err => {
            console.log(err)
          })
        } else {
          console.log('失败')
        }
      })
    },
    // 取消修改信息
    cancelModify () {
      this.modify = true
      this.assignment()
      this.$refs.BasicsForm.clearValidate()
    },
    // 赋值
    assignment () {
      this.BasicsForm.description = this.user_info.introduce
      this.BasicsForm.payment = this.user_info.payPassword
      this.BasicsForm.username = this.user_info.username
      this.Email.email = this.user_info.email
      this.head_image = this.user_info.head_portrait
    },
    // 用户名规范效验
    UsernameVerification (rule, value, callback) {
      this.$https.post('user/user_repeat/', { value: value, only: 0 }).then(res => {
        if (this.BasicsForm.username !== this.user_info.username) {
          if (res.data.code === 200) {
            if (res.data.state) {
              callback()
            } else {
              callback(new Error('当前用户名已存在'))
            }
          }
        } else {
          callback()
        }
      }).catch(err => {
        console.log(err)
      })
    },
    // 获取用户的数据进行展示
    getUserInfo () {
      this.$https.post('user/user_information/').then(res => {
        this.user_info = res.data.data.user_info
        this.assignment()
      }).catch(err => {
        console.log(err)
      })
    },
    // 上传头像
    upload_avatar () {
      this.getUserInfo()
      this.show = true
      emitter.on('show', (e) => {
        this.show = e.aim
      })
      emitter.on('image', (e) => {
        this.head_image = e.aim.url
      })
    }
  },
  created () {
    this.getUserInfo()
  }
}
</script>

<style scoped lang="less">
#account-information {
  position: relative;
  display: flex;
  padding-left: 60px;
  padding-top: 30px;
  .head-image {
    width: 150px;
    height: 150px;
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    margin-top: 15px;
    .image {
      width: 120px;
      height: 120px;
      background-image: url('https://w.wallhaven.cc/full/q2/wallhaven-q2qypq.png');
      background-size: cover;
      background-position: center;
      cursor: pointer;
    }
    .back-image {
      background-color: rgba(0, 0, 0, .3);
      opacity: 0;
      position: absolute;
      width: 120px;
      height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      &:hover {
        opacity: 1;
        transition: all .5s;
      }
    }
    span {
      font-size: 14px;
      color: #666;
      font-weight: bold;
      margin-top: 7px;
    }
  }
  .demo-ruleForm {
    width: 80%;
    :deep(.el-form-item__label) {
      width: 100px;
      line-height: 45px;
      font-size: 14px;
    }
    :deep(.el-input) {
      height: 45px;
    }
    :deep(.el-form-item) {
      margin-bottom: 35px;
    }
    :deep(.el-form-item__error) {
      margin-top: 7px;
    }
    :deep(.el-button) {
      width: 150px;
      height: 45px;
    }
    .verification {
      display: flex;
      :deep(.el-button) {
        width: 120px;
        height: 45px;
        margin-left: 25px;
      }
      :deep(.el-form-item) {
        width: 79%;
      }
    }
  }
}
.demo-tabs > .el-tabs__content {
  padding: 32px;
  color: #6b778c;
  font-size: 32px;
  font-weight: 600;
}

.el-tabs--right .el-tabs__content,
.el-tabs--left .el-tabs__content {
  height: 100%;
}
:deep(.el-tabs) {
  height: 100%;
  width: 74%;
  margin-left: 45px;
}
:deep(.el-tabs__nav-wrap) {
  margin-bottom: 35px;
  &:after {
    width: 85%;
  }
}
</style>
