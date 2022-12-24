<template>
  <v-app style="height:100%;overflow-y: hidden;overflow-x: hidden">
    <h1 style="margin-top: 10px;margin-bottom: 10px">讨论：{{ post.title }}</h1>
    <v-card
        class="mx-auto"
        width="98%"
        color="blue lighten-5"
    >
      <v-card-title>
        <v-list-item-avatar color="grey darken-3">
          <v-img
              class="elevation-6"
              :src="post.user_avatar"
          ></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{ post.user_name }}</v-list-item-title>
          <v-list-item-subtitle>{{ post.time }}</v-list-item-subtitle>
          <v-row
              align="center"
              justify="end"
              style="margin-right: 20px;"
          >
            <v-btn icon color="deep-orange">
              <v-icon>mdi-thumb-up</v-icon>
            </v-btn>
            <div>{{ post.like }}</div>
            <v-btn icon color="blue-grey darken-2">
              <v-icon>mdi-thumb-down</v-icon>
            </v-btn>
            <div>{{ post.dislike }}</div>
          </v-row>
        </v-list-item-content>
      </v-card-title>
      <pre v-html="post.content"></pre>
    </v-card>
    <v-list>
      <v-list-item
          v-for="reply in replies"
          :key="reply.reply_id"
          style="margin-top: 20px;flex: auto"
          v-show="reply.op < 3"
      >
        <v-card
            class="mx-auto"
            width="100%"
            color="blue-grey lighten-4"
        >
          <v-card-title>
            <v-list-item-avatar color="grey darken-3">
              <v-img
                  class="elevation-6"
                  :src="reply.user_avatar"
              ></v-img>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>{{ reply.user_name }}</v-list-item-title>
              <v-list-item-subtitle>{{ reply.time }}</v-list-item-subtitle>
              <v-row
                  align="center"
                  justify="end"
                  style="margin-right: 20px;"
              >
                <v-btn icon color="deep-orange" @click="likeReply(reply)">
                  <v-icon>mdi-thumb-up</v-icon>
                </v-btn>
                <div>{{ reply.like }}</div>
                <v-btn icon color="blue-grey darken-2" @click="dislikeReply(reply)">
                  <v-icon>mdi-thumb-down</v-icon>
                </v-btn>
                <div>{{ reply.dislike }}</div>
                <v-btn icon color="indigo" @click="deleteReply(reply)" v-show="isMaster">
                  <v-icon>mdi-comment-remove</v-icon>
                </v-btn>
              </v-row>
            </v-list-item-content>
          </v-card-title>
          <pre v-html="reply.content"></pre>
        </v-card>
      </v-list-item>
    </v-list>

    <v-card-text style="margin-top: 30px">以{{realName}}的身份参与讨论：</v-card-text>
    <mavon-editor
        v-model="newReply.content"
        style="margin-top: 20px;height: 100%;width:100%;align-self: center"
        ref=md
        @change="change"
        fontSize="16px">
    </mavon-editor>
    <v-btn @click="submit" style="margin-top: 20px;float: left;width: 20px" color="primary">
      回帖
    </v-btn>
  </v-app>

</template>

<script>
import Qs from "qs";

export default {
  name: "ReplyList",
  props: ["replies", "post", "isMaster"],
  data() {
    return {
      realName:'',
      newReply: {
        content: "",
        html: ""
      }
    }
  },
  methods: {
    // 所有操作都会被解析重新渲染
    change(value, render) {
      // render 为 markdown 解析后的结果[html]
      this.newReply.html = render;
    },
    likeReply(post) {
      let op
      if (post.op === 0) op = 2
      else op = 0
      this.$axios.post(
          "http://127.0.0.1:8000/api/like_reply",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            reply_id: post.reply_id,
            op: op
          })
      ).then((res) => {
        if (res.data.code === 0) {
          if (post.op === 0) {
            post.op = 2
            post.like -= 1
            this.$message.success("取消点赞成功");
          } else if (post.op === 1) {
            post.op = 0
            post.like += 1
            post.dislike -= 1
            this.$message.success("点赞成功");
          } else {
            post.op = 0
            post.like += 1
            this.$message.success("点赞成功");
          }
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    dislikeReply(post) {
      let op
      if (post.op === 1) op = 2
      else op = 1
      this.$axios.post(
          "http://127.0.0.1:8000/api/like_reply",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            reply_id: post.reply_id,
            op: op
          })
      ).then((res) => {
        if (res.data.code === 0) {
          if (post.op === 1) {
            post.op = 2
            post.dislike -= 1
            this.$message.success("取消点踩成功");
          } else if (post.op === 0) {
            post.op = 1
            post.like -= 1
            post.dislike += 1
            this.$message.success("点踩成功");
          } else {
            post.op = 1
            post.dislike += 1
            this.$message.success("点踩成功");
          }
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    // 提交
    submit() {
      /*
      DO:将这里的数据传到后端，在后端存储生成id存储
       */
      console.log(this.newReply.html)
      this.$axios.post(
          "http://127.0.0.1:8000/api/reply_post",
          Qs.stringify({
            content:this.newReply.html,
            user_id:localStorage.getItem('user_id'),
            post_id:this.post.post_id
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(this.clubId)
          this.newReply.content = ''
          location.reload(true)
          this.$message.success("回复成功");
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    deleteReply(reply) {
      /*
      DO:删除回复帖
       */
      this.$axios.post(
          "http://127.0.0.1:8000/api/delete_reply",
          Qs.stringify({
            reply_id:reply.reply_id
          })
      ).then((res)=>{
        if(res.data.code===0){
          reply.op = 3
          this.$message.success("删除回复成功");
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    getUserName() {
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_user_information",
          Qs.stringify({
            'user_id': localStorage.getItem('user_id')
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.realName = res.data.user.real_name
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  created() {
    this.getUserName()
    console.log(this.post)
  }
}
</script>

<style scoped>
pre {
  margin-left: 20px;
  margin-bottom: 20px;
  margin-right: 20px;
  tab-size: 2;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>
