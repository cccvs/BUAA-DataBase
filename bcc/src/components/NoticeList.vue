<template>
  <v-timeline align-top :dense="$vuetify.breakpoint.smAndDown">
    <v-timeline-item
        v-for="notice in noticeList"
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
          <p>{{notice.content}}</p>
          <v-btn
              :color="curColor(notice.notice_id)"
              class="mx-0"
              outlined
          >
            确认收到
          </v-btn>
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>

<script>

export default {
  name: "NoticeList",
  data() {
    return {
      noticeList: [
        {
          notice_id: 1,
          title: "社长换届1",
          content: "卸职：张三，任命：李四",
          user_id: "20373021",
        }, {
          notice_id: 2,
          title: "社长换届2",
          content: "卸职：张三，任命：李四",
          user_id: "20373021",
        }, {
          notice_id: 3,
          title: "社长换届3",
          content: "卸职：张三，任命：李四",
          user_id: "20373021",
        }, {
          notice_id: 4,
          title: "社长换届4",
          content: "卸职：张三，任命：李四",
          user_id: "20373021",
        }
      ],
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
          icon: 'mdi-buffer',
        },
      ],
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
  }
}
</script>


<style scoped>

</style>