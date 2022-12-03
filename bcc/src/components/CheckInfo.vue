<template>
    <v-card
        max-width="100%"
        class="align-center"
    >
      <v-toolbar
          src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
        <v-toolbar-title>新的入社申请</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>
      <v-list subheader>
        <v-subheader>又有新的小伙伴要加入社团了</v-subheader>

        <v-list-item
            v-for="request in requests"
            :key="request.id">
          <!--                      @click=""-->
          <!--                  >-->
          <v-list-item-avatar>
            <v-avatar>
              <img :src="request.avatar" alt="头像">
            </v-avatar>
          </v-list-item-avatar>

          <v-list-item-content style="padding-left: 10px">
            <v-list-item-title v-text="request.userName"></v-list-item-title>
          </v-list-item-content>
          <v-spacer></v-spacer>
          <v-btn elevation="10" icon circle color="green" @click="handlePass(request.id)" style="margin-right: 20px">
            <v-icon>
              mdi-check
            </v-icon>
          </v-btn>
          <v-btn elevation="10" icon color="red" @click="handleFailPass(request.id)" style="margin-right: 5px">
            <v-icon>
              mdi-close
            </v-icon>
          </v-btn>
        </v-list-item>
      </v-list>
      <v-snackbar
          center
          top
          v-model="snackbar.show"
      >
        {{ snackbar.text }}
        <template v-slot:action="{ attrs }">
          <v-btn
              color="pink"
              text
              v-bind="attrs"
              @click="snackbar.show = false"
          >
            关闭
          </v-btn>
        </template>
      </v-snackbar>
    </v-card>
</template>

<script>
export default {
  name: "CheckInfo",
  data() {
    return {
      snackbar: {
        show: false,
        text: ""
      },
      requests: [{
        id: 1,
        userName: "陈俊杰",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
      }, {
        id: 2,
        userName: "蒋博文",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
      }, {
        id: 3,
        userName: "陈楚岩",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
      }]
    }
  },
  methods: {
    handlePass(id) {
      this.requests = this.requests.filter((request) => {
        return request.id !== id;
      })
      this.snackbar.show = true;
      this.snackbar.text = "审核成功，该学生成功加入社团！"
    },
    handleFailPass(id) {
      this.requests = this.requests.filter((request) => {
        return request.id !== id;
      })
      this.snackbar.show = true;
      this.snackbar.text = "已拒绝该学生成功加入社团"
    }
  }
}
</script>

<style scoped>

</style>