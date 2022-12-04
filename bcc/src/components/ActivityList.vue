<template>
  <v-card
      max-width="344"
      class="mx-auto"
  >
    <v-list-item>
      <v-list-item-avatar color="grey"></v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title class="headline">活动标题</v-list-item-title>
        <v-list-item-subtitle>发布者，2022-12-04</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-img
        src="https://cdn.vuetifyjs.com/images/cards/mountain.jpg"
        height="194"
    ></v-img>
    <v-card-text>
      报名时间：2022-10-01~2022-11-02
    </v-card-text>
    <v-card-text>
      活动时间：2022-12-01~2022-12-10
    </v-card-text>
    <v-rating v-model="rating" dense color="yellow" style="margin-left: 10px"></v-rating>
    <v-card-actions>
      <v-btn
          text
          color="deep-purple accent-4"
          @click="show = !show"
      >
        查看详情
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-thumb-up</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-thumb-down</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-chat</v-icon>
      </v-btn>
    </v-card-actions>
    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>
        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for
          sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you
          add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: "ActivityList",
  data() {
    return {
      show: false,
      rating: 4.6
    }
  }
}
</script>

<style scoped>

</style>