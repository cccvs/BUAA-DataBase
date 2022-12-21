<template>
  <v-list>
    <v-list-item
        v-for="post in posts"
        :key="post.post_id"
        @dblclick="detailForPost(post.post_id)"
    >
      <v-icon large color="blue darken-2">mdi-message-text</v-icon>
      <v-list-item-content style="padding-left: 10px">
        <v-list-item-title v-text="post.title"></v-list-item-title>
        <v-list-item-subtitle v-text="post.content"></v-list-item-subtitle>
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
      <v-list-item-content style="margin-right: 10px;margin-left: 20px">2022-10-15 10:04</v-list-item-content>
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

</style>