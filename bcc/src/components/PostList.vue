<template>
  <v-list>
    <v-list-item
        v-for="post in posts"
        :key="post.post_id"
        @dblclick="detailForPost(post.post_id)"
    >
      <v-avatar>
        <img :src="post.avatar" alt="头像">
      </v-avatar>
      <v-list-item-content style="padding-left: 10px">
        <v-list-item-title>{{post.title}} - {{post.user_name}}</v-list-item-title>
        <pre v-html="post.content"></pre>
      </v-list-item-content>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn icon color="deep-orange">
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>
      <div>{{ post.like }}</div>
      <v-btn icon color="blue-grey darken-2">
        <v-icon>mdi-thumb-down</v-icon>
      </v-btn>
      <div>{{ post.dislike }}</div>
      <v-list-item-content style="margin-right: 10px;margin-left: 20px">{{post.time}}</v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
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
</style>
