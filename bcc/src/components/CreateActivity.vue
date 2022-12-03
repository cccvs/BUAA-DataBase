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
            value-format="timestamp"
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
            value-format="timestamp"
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
    <v-textarea
        clearable
        clear-icon="mdi-close"
        label="正文内容"
        :value="activity.content"
        style="margin-top: 20px"
    ></v-textarea>
    <v-slider v-model="activity.limit"
              :thumb-size="24"
              thumb-label
              min="0">
    </v-slider>
  </v-container>
</template>

<script>
export default {
  name: "CreateActivity",
  data() {
    return {
      activity: {
        id: 1,
        title: "",
        content: "",
        user_id: 20373021,
        apply_time: "",
        begin_time: "",
        limit: 24
      }
    }
  }
}
</script>

<style scoped>

</style>