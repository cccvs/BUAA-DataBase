<template>
  <div>
    <v-app style="height: 80px;overflow-y: hidden;overflow-x: hidden">
      <!--      <v-row style="margin-left: 15px;margin-top: 10px">-->
      <!--        <v-icon color="blue">mdi-clipboard-text-multiple-outline</v-icon>-->
      <!--      </v-row>-->
      <v-row style="margin-left: 15px;margin-top: 10px">
        <v-container style="width: 50%;height: 100%">
          <v-row>
            <v-icon color="blue" style="margin-right: 10px;">mdi-file-document-edit</v-icon>
            <h4>管理您的账号</h4>
          </v-row>
          <div style="margin-top: 20px;">
            <v-btn color="deep-purple accent-1"
                   elevation="5"
                   @click="dialogFormVisible = true">
              修改密码
            </v-btn>
            <v-btn color="deep-purple accent-1"
                   elevation="5"
                   style="margin-left: 10px">
              上传头像
            </v-btn>
          </div>
        </v-container>
        <v-spacer></v-spacer>
        <v-avatar style="margin-right: 20px">
          <img :src="avatar" alt="头像">
        </v-avatar>
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
    </v-app>
  </div>
</template>

<script>
export default {
  name: "MyUserCenterHeader",
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
    submitForm(formName) {
      console.log("验证密码正确性")
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!');
        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
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