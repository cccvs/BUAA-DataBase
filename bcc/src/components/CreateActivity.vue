<template>
  <v-container fluid>
    <v-row>
      <v-icon color="blue" style="margin-left: 10px;margin-top: 10px">mdi-message-bookmark-outline</v-icon>
      <h1 style="margin-left: 10px;margin-top: 10px">组织全新的活动！</h1>
    </v-row>
    <v-row>
      <v-col cols="5">
        <v-text-field label="标题" hide-details="auto"
                      style="padding-bottom: 20px;margin-top: 20px"
                      v-model="activity.title">
        </v-text-field>
        <v-row style="margin-top:10px; margin-left: 5px">
          <div class="block">
            <span class="demonstration">报名起止时间：</span>
            <el-date-picker
                value-format="yyyy-MM-dd HH:mm:ss"
                style="margin-left: 15px"
                v-model="activity.apply_time"
                type="datetimerange"
                align="left"
                start-placeholder="报名开始时间"
                end-placeholder="报名截止时间"
                :default-time="['12:00:00', '08:00:00']">
            </el-date-picker>
          </div>
        </v-row>
        <v-row style="margin-top:20px;margin-left: 5px">
          <div class="block">
            <span class="demonstration">活动起止时间：</span>
            <el-date-picker
                value-format="yyyy-MM-dd HH:mm:ss"
                style="margin-left: 15px"
                v-model="activity.begin_time"
                type="datetimerange"
                align="left"
                start-placeholder="活动开始时间"
                end-placeholder="活动截止时间"
                :default-time="['12:00:00', '08:00:00']">
            </el-date-picker>
          </div>
        </v-row>
      </v-col>
      <v-col cols="5">
        <v-row style="margin-top:30px;margin-left: 100px">
          <label>选择活动封面：</label>
          <el-upload
              :auto-upload="true"
              :before-upload="beforeAvatarUpload"
              :on-success="handleAvatarSuccess"
              :limit=1
              :data="{user_id:this.user_id}"
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
        </v-row>
      </v-col>
    </v-row>
    <v-row style="margin-top: 30px;margin-left: 5px">
      <label>预计活动人数: {{activity.limit}}人</label>
      <v-slider v-model="activity.limit"
                :thumb-size="24"
                thumb-label="always"
                append-icon="mdi-arrow-right-circle"
                prepend-icon="mdi-arrow-left-circle"
                @click:append="zoomIn"
                @click:prepend="zoomOut"
                min="0"
      style="margin-left: 30px">
      </v-slider>
    </v-row>
    <v-textarea
        counter
        auto-grow
        clearable
        clear-icon="mdi-close"
        label="活动内容"
        v-model="activity.content"
        style="margin-top: 10px; margin-left: 5px"
    ></v-textarea>
    <v-btn color="primary" @click="handleApply">
      <v-icon dark style="margin-right: 5px">mdi-checkbox-marked-circle</v-icon>
      发起活动
    </v-btn>
    <MySnackBar>
    </MySnackBar>
  </v-container>
</template>

<script>
import MySnackBar from "@/components/MySnackBar";
import Qs from "qs";
export default {
  name: "CreateActivity",
  components: {MySnackBar},
  props: ['club_id'],
  data() {
    return {
      activity: {
        id: 1,
        title: "",
        content: "",
        user_id: "20373021",
        apply_time: "",
        begin_time: "",
        limit: 24
      },
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false,
      user_id:localStorage.getItem('user_id'),
      createClubForm: {
        imageUrl: '',
        clubName: '',
        clubType: '',
        introduction: '',
      },
    }
  },
  methods: {
    /*
    DO:发布活动的接口，这里是否考虑加入活动封面？
     */
    handleApply() {
      this.$axios.post(
          "http://127.0.0.1:8000/api/create_event",
          Qs.stringify({
            club_id:this.club_id,
            user_id:localStorage.getItem('user_id'),
            title:this.activity.title,
            cover:'',
            content:this.activity.content,
            apply_time:this.activity.apply_time[0],
            expired_time:this.activity.apply_time[1],
            begin_time:this.activity.begin_time[0],
            end_time:this.activity.begin_time[1],
            limit:this.activity.limit
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(this.activity.content)
          this.$bus.$emit('showSnackBar', "活动已发布！")
          this.activity.title = ''
          this.activity.content = ''
          this.activity.apply_time = ''
          this.activity.begin_time = ''
          this.activity.limit = 24
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    zoomIn() {
      this.activity.limit++;
    },
    zoomOut() {
      if (this.activity.limit === 0) {
        this.$bus.emit('showSnackBar', "活动人数最低为0！")
      }
      this.activity.limit--;
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
    handleAvatarSuccess (res) {
      if (res.code !== 0) {
        this.$message.error(res.message)
        return false
      }
      this.createClubForm.imageUrl = res.image_path
      console.log(this.createClubForm.imageUrl)
      this.$message.success('上传成功')
    },
  }
}
</script>

<style scoped>

</style>
