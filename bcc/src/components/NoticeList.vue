<template>
  <v-timeline align-top :dense="$vuetify.breakpoint.smAndDown">
    <v-timeline-item
        v-for="notice in notices"
        :key="notice.notice_id"
        :color="curColor(notice.notice_id)"
        :icon="curIcon(notice.notice_id)"
        fill-dot
    >
      <v-card
          :color="curColor(notice.notice_id)"
          dark
      >
        <v-card-title class="title">{{notice.title}}</v-card-title>
        <v-card-text class="white text--primary">
          <pre>{{notice.content}}</pre>
          <v-btn
              :color="curColor(notice.notice_id)"
              class="mx-0"
              outlined
              @click="deleteNotice(notice.notice_id)"
          >
            删除公告
          </v-btn>
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

<script>

export default {
  name: "NoticeList",
  props: ["notices"],
  data() {
    return {
      items: [
        {
          color: 'red lighten-2',
          icon: 'mdi-star',
        },
        {
          color: 'purple darken-1',
          icon: 'mdi-book-variant',
        },
        {
          color: 'green lighten-1',
          icon: 'mdi-airballoon',
        },
        {
          color: 'indigo',
          icon: 'mdi-atom',
        },
      ],
    }
  },
  methods: {
    deleteNotice(notice_id) {
      console.log(notice_id);
      /*
      TODO: 删除公告，前端限制只有社长可以
       */
    }
  },
  computed: {
    curColor() {
      return function (id) {
        let index = parseInt(id % 4);
        return this.items[index].color;
      }
    },
    curIcon() {
      return function (id) {
        let index = parseInt(id % 4);
        return this.items[index].icon;
      }
    }
  },
}
</script>

<style scoped>
pre {
  tab-size: 2;
  white-space: pre-wrap;
  word-wrap: break-word;
}
</style>
