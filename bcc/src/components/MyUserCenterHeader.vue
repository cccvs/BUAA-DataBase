<template>
  <div>
    <v-app style="height: 100%;overflow-y: hidden;overflow-x: hidden">
      <v-row style="max-height: 50px;margin-top: 10px;margin-left: 10px">
        <v-col cols="1">
          <v-icon color="blue">mdi-file-document-edit</v-icon>
        </v-col>
        <v-col cols="9">
          <h1>管理您的账号</h1>
        </v-col>
      </v-row>
      <v-row style="margin-left: 10px;max-height:50px;min-width: 300px">
        <v-btn color="deep-purple accent-1"
               elevation="5"
               @click="dialogFormVisible = true">
          修改密码
        </v-btn>
        <v-btn color="deep-purple accent-1"
               elevation="5"
               style="margin-left: 10px"
               @click="pickPhoto">
          上传头像
        </v-btn>
        <div>
          <el-dialog :visible.sync="dialogFormVisible">
            <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px"
                     class="demo-ruleForm">
              <el-form-item label="密码" prop="pass">
                <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="确认密码" prop="checkPass">
                <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
              </el-form-item>
            </el-form>
          </el-dialog>
        </div>
      </v-row>
      <v-row align-self="center" style="margin-left: 10px;max-height:300px;margin-top: 30px">
        <v-card width="75%" shaped>
          <v-row style="margin-left: 0;margin-top: 0;margin-right: 0;">
            <v-avatar tile width="100%" height="300px">
              <img :src="avatar" alt="头像">
            </v-avatar>
            <v-col cols="8" style="float: left">
              <v-card-title>用户名：{{ real_name }}</v-card-title>
              <v-card-text>关注数：{{ following }}</v-card-text>
              <v-card-text>粉丝数：{{ followers }}</v-card-text>
            </v-col>
          </v-row>
        </v-card>
      </v-row>
      <MySnackBar></MySnackBar>
    </v-app>
  </div>
</template>

<script>
import MySnackBar from "@/components/MySnackBar";

export default {
  name: "MyUserCenterHeader",
  components: {MySnackBar},
  /*
  FIXME: 本来avatar属性应该也是由父组件传递进来的，但是发现url不能跨域传递？
   */
  props: ["real_name", "following", "followers"],
  data() {
    let validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        if (this.ruleForm.checkPass !== '') {
          this.$refs.ruleForm.validateField('checkPass');
        }
        callback();
      }
    };
    let validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.ruleForm.pass) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
      dialogFormVisible: false,
      ruleForm: {
        pass: '',
        checkPass: '',
      },
      rules: {
        pass: [
          {validator: validatePass, trigger: 'blur'}
        ],
        checkPass: [
          {validator: validatePass2, trigger: 'blur'}
        ]
      }
    }
  },
  methods: {
    /*
    TODO: 验证密码正确性的接口
     */
    submitForm(formName) {
      console.log("验证密码正确性")
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.dialogFormVisible = false
          this.$bus.$emit("showSnackBar", "修改密码成功！")
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    /*
    TODO: 上传头像接口，可以复用社团上传图片的接口
     */
    pickPhoto() {

    }
  }
}
</script>

<style scoped>
.flexs {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>