<template>
  <v-container fluid>
    <v-row>
      <v-icon color="blue" style="margin-left: 10px;margin-top: 10px">mdi-message-bookmark-outline</v-icon>
      <h1 style="margin-left: 10px;margin-top: 10px">组织全新的活动！</h1>
    </v-row>
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
    <v-row style="margin-top: 40px;margin-left: 5px">
      <label>预计活动人数:{{activity.limit}}人</label>
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
      }
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
            applyTime:this.activity.apply_time[0],
            expiredTime:this.activity.apply_time[1],
            beginTime:this.activity.begin_time[0],
            endTime:this.activity.begin_time[1],
            limit:this.activity.limit
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(this.activity.content)
          this.$bus.$emit('showSnackBar', "活动已发布！")
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
    }
  }
}
</script>

<style scoped>

</style>
