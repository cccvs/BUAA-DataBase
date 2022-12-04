<template>
  <v-list>
    <v-subheader>{{ text }}</v-subheader>
    <v-list-item
        v-for="activity in activities"
        :key="activity.id"
        style="margin-top: 20px"
    >
      <v-card
          class="mx-auto"
      >
        <v-list-item>
          <v-list-item-avatar color="grey">
            <img src="https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg" alt="头像">
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="headline">{{activity.title}}</v-list-item-title>
            <v-list-item-subtitle>{{activity.user_id}}，发布时间</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
        <v-img
            src="https://cdn.vuetifyjs.com/images/cards/mountain.jpg"
            height="194"
        ></v-img>
        <v-card-text>
          报名时间：{{activity.apply_time}}
        </v-card-text>
        <v-card-text>
          活动时间：{{activity.begin_time}}
        </v-card-text>
        <v-rating v-model="rating" dense color="yellow" style="margin-left: 10px"></v-rating>
        <v-card-actions>
          <v-btn
              text
              color="deep-purple accent-4"
              @click="activity.show = !activity.show"
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
          <div v-show="activity.show">
            <v-divider></v-divider>
            <v-card-text>
              {{activity.content}}
            </v-card-text>
          </div>
        </v-expand-transition>
      </v-card>
    </v-list-item>
  </v-list>

</template>

<script>
export default {
  name: "ActivityList",
  props: ['activities', 'text'],
  data() {
    return {
      rating: 4.6
    }
  },
  methods: {
    detailOfActivity() {
      this.show = true
    }
  }
}
</script>

<style scoped>

</style>