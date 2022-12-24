<template>
  <v-list style="margin-top: 10px">
    <v-list-item
        v-for="post in posts"
        :key="post.post_id"
        @dblclick="detailForPost(post.post_id)"
        style="margin-top: 10px"
        v-show="post.op <= 2"
    >
      <v-avatar>
        <img :src="post.user_avatar" alt="头像">
      </v-avatar>
      <v-list-item-content style="padding-left: 10px">
        <v-list-item-title>{{ post.title }} - {{ post.user_name }}</v-list-item-title>
        <v-list-item-subtitle v-html="post.content"></v-list-item-subtitle>
      </v-list-item-content>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn icon color="deep-orange" @click="likePost(post)">
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>
      <div>{{ post.like }}</div>
      <v-btn icon color="blue-grey darken-2" @click="dislikePost(post)">
        <v-icon>mdi-thumb-down</v-icon>
      </v-btn>
      <div>{{ post.dislike }}</div>
      <v-btn icon color="indigo" @click="deletePost(post)">
        <v-icon>mdi-comment-remove</v-icon>
      </v-btn>
      <v-list-item-content style="margin-left: 20px">{{ post.time }}</v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
import Qs from "qs";

export default {
  name: "PostList",
  props: ["posts"],
  methods: {
    detailForPost(id) {
      // alert(id);
      let path = "/post/" + id;
      console.log(path);
      this.$router.push({
        path
      });
    },
    likePost(post) {
      let op
      if (post.op === 0) op = 2
      else op = 0
      this.$axios.post(
          "http://127.0.0.1:8000/api/like_post",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            post_id: post.post_id,
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
    dislikePost(post) {
      let op
      if (post.op === 1) op = 2
      else op = 1
      this.$axios.post(
          "http://127.0.0.1:8000/api/like_post",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            post_id: post.post_id,
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
    deletePost(post) {
      /*
      DO:删除主题帖
       */
      this.$axios.post(
          "http://127.0.0.1:8000/api/delete_post",
          Qs.stringify({
            post_id: post.post_id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          post.op = 3
          this.$message.success("删除主题帖成功");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  mounted() {
    console.log(this.posts)
  }
}
</script>

<style scoped>
pre {
  tab-size: 2;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>
