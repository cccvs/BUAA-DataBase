<template>
  <v-list>
    <v-row style="margin-left: 10px">
      <v-icon color="blue">mdi-bulletin-board</v-icon>
      <h1 style="margin-left: 10px;margin-top: 10px">{{ text }}</h1>
    </v-row>
    <v-list-item
        v-for="activity in activities"
        :key="activity.event_id"
        style="margin-top: 20px; width: 400px; margin-left:20px; float: left"
    >
      <v-card
          class="mx-auto"
          style="min-width: 400px"
      >
        <v-list-item>
          <v-list-item-avatar color="grey">
            <img :src="activity.cover" alt="头像">
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="headline">{{ activity.title }}</v-list-item-title>
            <v-list-item-subtitle>
              {{ activity.club_name }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-img
            :src="activity.cover"
            height="194"
        ></v-img>
        <!--            src="https://cdn.vuetifyjs.com/images/cards/mountain.jpg"-->
        <div style="float: right">
          {{ activity.real_name }} 发布于：{{ activity.time }}
        </div>
        <div class="desBlock">
          报名时间：{{ activity.apply_time }}
        </div>
        <div v-show="!audit">
          报名人数：{{ activity.member_count }} / {{ activity.member_limit }}
        </div>
        <div v-show="audit">
          活动人数上限：{{ activity.member_limit }}
        </div>
        <div>
          活动时间：{{ activity.begin_time }}
        </div>
<!--        <div v-show="!audit">-->
<!--          评价该活动：（{{ activity.score }}），平均评分：（{{ activity.avg_score }}）-->
<!--          <v-rating v-model="activity.score"-->
<!--                    dense color="yellow"-->
<!--                    style="margin-left: 10px"></v-rating>-->
<!--        </div>-->
        <v-card-actions>
          <v-btn
              text
              color="deep-purple accent-4"
              @click="activity.show = !activity.show"
          >
            查看详情
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn small color="purple lighten-5" v-show="!audit" @click="participate(activity.event_id)">
            报名
          </v-btn>
          <v-btn icon color="deep-orange" v-show="!audit" @click="likeEvent(activity.event_id,activity.op)">
            <v-icon>mdi-thumb-up</v-icon>
          </v-btn>
          <div v-show="!audit">{{ activity.like }}</div>
          <v-btn icon color="blue-grey darken-2" v-show="!audit" @click="dislikeEvent(activity.event_id,activity.op)">
            <v-icon>mdi-thumb-down</v-icon>
          </v-btn>
          <div v-show="!audit">{{ activity.dislike }}</div>
          <v-btn v-show="audit" elevation="10" icon circle color="green" @click="handlePass(activity.event_id)"
                 style="margin-right: 20px">
            <v-icon>
              mdi-check
            </v-icon>
          </v-btn>
          <v-btn v-show="audit" elevation="10" icon color="red" @click="handleFailPass(activity.event_id)"
                 style="margin-right: 5px">
            <v-icon>
              mdi-close
            </v-icon>
          </v-btn>
        </v-card-actions>
        <v-dialog v-model="activity.show">
          <v-card>
            <v-card-title>
              <span class="headline">{{ activity.title }}</span>
            </v-card-title>
            <v-card-text style="margin-top: 20px">
              <pre>{{ activity.content }}</pre>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="activity.show = false">关闭</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-card>
    </v-list-item>
  </v-list>
</template>

<script>
import Qs from "qs";

export default {
  name: "ActivityList",
  props: ['activities', 'text', 'audit'],
  methods:{
    participate(id) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/participate_event",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            event_id: id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("报名成功");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    likeEvent(id,status) {
      let op
      if (status === 0) op = 2
      else op = 0
      this.$axios.post(
          "http://127.0.0.1:8000/api/like_event",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            event_id: id,
            op: op
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("点赞成功");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    dislikeEvent(id,status) {
      let op
      if (status === 1) op = 2
      else op = 1
      this.$axios.post(
          "http://127.0.0.1:8000/api/like_event",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            event_id: id,
            op: op
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("点踩成功");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    handlePass(id) {
      /*
      DO:团委老师通过活动审批
       */
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_create_event",
          Qs.stringify({
            event_id: id,
            op: 1
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("活动审批通过");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    handleFailPass(id) {
      /*
      DO:团委老师拒绝了活动
       */
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_create_event",
          Qs.stringify({
            event_id: id,
            op: 0
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("活动审批拒绝");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
pre {
  tab-size: 2;
  white-space: pre-wrap;
  word-wrap: break-word;
}

.desBlock {
  margin-top: 30px;
}
</style>
