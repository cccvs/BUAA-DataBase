<template>
  <div class="main-box">
    <div class="container">
      <el-form :rules="createClubRules" :model="createClubForm">
        <h2 class="title">社团基本信息</h2>
        <h3 style="margin-bottom: 20px;color: #4b70e2;float: left">请依次上传社团logo及风采照片：</h3>
        <el-form-item>
          <el-upload
              :auto-upload="true"
              :before-upload="beforeAvatarUpload"
              :on-success="handleAvatarSuccess"
              :limit=2
              multiple
              accept=".png,.jpg,.jepg"
              action="http://127.0.0.1:8000/upload/img"
              list-type="picture-card"
              ref="upload"
              style="margin-bottom: 20px">
            <i slot="default" class="el-icon-plus"></i>
            <div slot="file" slot-scope="{file}">
              <img
                  class="el-upload-list__item-thumbnail"
                  :src="file.url" alt=""
              >
              <span class="el-upload-list__item-actions">
                    <span
                        class="el-upload-list__item-preview"
                        @click="handlePictureCardPreview(file)"
                    >
                      <i class="el-icon-zoom-in"></i>
                    </span>
                    <span
                        v-if="!disabled"
                        class="el-upload-list__item-delete"
                        @click="handleRemove(file)"
                    >
                      <i class="el-icon-delete"></i>
                      </span>
                  </span>
            </div>
          </el-upload>
          <el-dialog :visible.sync="dialogVisible">
            <img width="100%" :src="dialogImageUrl" alt="">
          </el-dialog>
        </el-form-item>
        <el-form-item prop="clubName">
          <el-input v-model="createClubForm.clubName" class="form__input" type="text" placeholder="社团名称"/>
        </el-form-item>
        <el-form-item prop="clubType">
          <el-select v-model="createClubForm.clubType" class="form__input" placeholder="请选择社团类型"
                     style="display: block;">
            <el-option label="科技" value="科技"></el-option>
            <el-option label="人文" value="人文"></el-option>
            <el-option label="实践" value="实践"></el-option>
            <el-option label="体育" value="体育"></el-option>
            <el-option label="艺术" value="艺术"></el-option>
            <el-option label="其它" value="其它"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="introduction">
          <el-input v-model="createClubForm.introduction" class="form__input" type="text" placeholder="社团简介"/>
        </el-form-item>
        <el-form-item prop="welcome">
          <el-input v-model="createClubForm.welcome" class="form__input" type="text" placeholder="社团欢迎语"/>
        </el-form-item>
        <el-form-item>
          <div class="primary-btn" @click="create" v-show="onCreate">立即注册</div>
          <div class="primary-btn" @click="change" v-show="!onCreate">确认修改</div>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>

<script>

import Qs from "qs";

export default {
  /*
  DO: 社团信息需要额外收集欢迎照片和欢迎语
  welcomeUrl
  welcome
   */
  name: "FindClub2",
  props: ['onCreate'],
  data() {
    return {
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      dialogImageUrl2: '',
      dialogVisible2: false,
      disabled2: false,
      user_id: localStorage.getItem('user_id'),
      createClubForm: {
        imageUrl: '',
        welcomeImage: '',
        clubName: '',
        clubType: '',
        introduction: '',
        welcome: '',
      },
      createClubRules: {
        clubName: [{required: true, message: '请输入社团名称', trigger: 'blur'}],
        clubType: [{required: true, message: '请选择社团类型', trigger: 'blur'}],
        introduction: [{required: true, message: '请输入社团简介', trigger: 'blur'}],
        welcome: [{required: true, message: '请输入社团欢迎语', trigger: 'blur'}],
      }
    }
  },
  methods: {
    change() {
      let con = {};
      con['image_url'] = this.createClubForm.imageUrl;
      con['name'] = this.createClubForm.clubName;
      con['type'] = this.createClubForm.clubType;
      con['intro'] = this.createClubForm.introduction;
      con['welcome_image'] = this.createClubForm.welcomeImage;
      con['welcome'] = this.createClubForm.welcome;
      con['jwt'] = {
        'code': localStorage.getItem('code'),
        'user_id': localStorage.getItem('user_id'),
        'time': localStorage.getItem('time')
      };
      this.$axios({
        url: 'http://127.0.0.1:8000/api/modify_club_info',
        method: 'post',
        data: Qs.stringify(con),
      }).then((ret) => {
        if (ret.data.code === 0) {
          this.$message.success("社团信息修改成功");
          this.$refs.upload.clearFiles();
          this.createClubForm.imageUrl = '';
          this.createClubForm.clubName = '';
          this.createClubForm.clubType = '';
          this.createClubForm.introduction = '';
          this.createClubForm.welcomeImage = '';
          this.createClubForm.welcome = '';
        } else this.$notify.error(ret.data.message + "，修改失败");
      })
    },
    create: function () {
      let con = {};
      con['image_url'] = this.createClubForm.imageUrl;
      con['name'] = this.createClubForm.clubName;
      con['type'] = this.createClubForm.clubType;
      con['intro'] = this.createClubForm.introduction;
      con['welcome_image'] = this.createClubForm.welcomeImage;
      con['welcome'] = this.createClubForm.welcome;
      con['jwt'] = {
        'code': localStorage.getItem('code'),
        'user_id': localStorage.getItem('user_id'),
        'time': localStorage.getItem('time')
      };
      this.$axios({
        url: 'http://127.0.0.1:8000/api/create_club',
        method: 'post',
        data: Qs.stringify(con),
      }).then((ret) => {
        if (ret.data.code === 0) {
          this.$message.success("申请成功，请等待审批");
          this.$refs.upload.clearFiles();
          this.createClubForm.imageUrl = '';
          this.createClubForm.clubName = '';
          this.createClubForm.clubType = '';
          this.createClubForm.introduction = '';
          this.createClubForm.welcomeImage = '';
          this.createClubForm.welcome = '';
        } else this.$notify.error(ret.data.message + "，申请失败");
      })
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    },
    //清除图片缓存
    handleRemove(file) {
      console.log(file)
      this.$refs.upload.clearFiles();
    },
    //展示图片预览图
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    handleAvatarSuccess(res) {
      if (res.code !== 0) {
        this.$message.error(res.message)
        return false
      }
      if (this.createClubForm.imageUrl === '') this.createClubForm.imageUrl = res.image_path
      else this.createClubForm.welcomeImage = res.image_path
      // this.$message.success('上传成功')
    },
  }
}
</script>

<style lang="scss" scoped>
.pic {
  float: left;
  min-width: 500px;
  max-height: 148px;

}

.el-form-item__content {
  max-height: 148px;
}

.main-box {
  position: center;
  width: 100%;
  min-width: 1000px;
  min-height: 300px;
  height: 700px;
  background-color: #ecf0f3;
  box-shadow: 10px 10px 10px #c3d5f3, -10px -10px 10px #f9f9f9;
  border-radius: 12px;
  overflow: hidden;

  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    position: center;
    width: 100%;
    height: 100%;
    background-color: #ecf0f3;

    form {
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
      width: 100%;
      height: 100%;
      color: #ecf0f3;

      .title {
        font-size: 34px;
        font-weight: 700;
        line-height: 3;
        color: #181818;
      }

      .text {
        margin-top: 30px;
        margin-bottom: 12px;
      }

      .form__input {
        width: 700px;
        height: 40px;
        margin: 4px 0;
        padding-left: 25px;
        font-size: 13px;
        letter-spacing: 0.15px;
        border: none;
        outline: none;
        // font-family: 'Montserrat', sans-serif;
        background-color: #ecf0f3;
        transition: 0.25s ease;
        border-radius: 8px;
        box-shadow: inset 2px 2px 4px #d1d9e6, inset -2px -2px 4px #f9f9f9;

        &::placeholder {
          color: #a0a5a8;
        }
      }
    }
  }
}

::v-deep .el-input__inner {
  background-color: #ecf0f3 !important;
  border: none 0 !important;
  padding-left: 0 !important;
  height: 30px !important;
  line-height: 30px !important;
}

.primary-btn {
  transition: all 0.3s;
  width: 180px;
  height: 50px;
  border-radius: 25px;
  margin-top: 25px;
  text-align: center;
  line-height: 50px;
  font-size: 14px;
  letter-spacing: 2px;
  background-color: #4b70e2;
  color: #f9f9f9;
  cursor: pointer;
  box-shadow: 8px 8px 16px #d1d9e6, -8px -8px 16px #f9f9f9;

  &:hover {
    box-shadow: 4px 4px 6px 0 rgb(255 255 255 / 50%),
    -4px -4px 6px 0 rgb(116 125 136 / 50%),
    inset -4px -4px 6px 0 rgb(255 255 255 / 20%),
    inset 4px 4px 6px 0 rgb(0 0 0 / 40%);
  }
}

.avatar {
  margin-top: 10px;
  height: 150px;
  width: 150px;
}

.el-upload-dragger {
  height: 250px;
  width: 250px;
}
</style>
