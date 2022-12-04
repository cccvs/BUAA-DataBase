<template>
    <v-card
        max-width="100%"
        class="align-center"
    >
      <v-row style="margin-left: 10px;margin-top: 10px">
        <v-icon color="blue">mdi-chat-plus</v-icon>
        <h1 style="margin-left: 10px;margin-top: 10px">新的入社申请！</h1>
      </v-row>
      <MemberList :members="requests" :check-info="true"
      text="又有新的小伙伴要加入社团了" style="margin-top: 20px"></MemberList>
      <MySnackBar></MySnackBar>
    </v-card>
</template>

<script>
import MySnackBar from "@/components/MySnackBar";
import MemberList from "@/components/MemberList";
export default {
  name: "CheckInfo",
  components: {MemberList, MySnackBar},
  data() {
    return {
      requests: [{
        id: "20373021",
        userName: "陈俊杰",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
      }, {
        id: "123",
        userName: "蒋博文",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
      }, {
        id: "124",
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
      this.$bus.$emit('showSnackBar', "审核成功，该学生成功加入社团！")
    },
    handleFailPass(id) {
      this.requests = this.requests.filter((request) => {
        return request.id !== id;
      })
      this.$bus.$emit('showSnackBar', "已拒绝该学生成功加入社团")
    }
  },
  mounted() {
    this.$bus.$on('handlePass', this.handlePass)
    this.$bus.$on('handleFailPass', this.handleFailPass)
  },
  beforeDestroy() {
    this.$bus.$off('handlePass', this.handlePass)
    this.$bus.$off('handleFailPass', this.handleFailPass)
  }
}
</script>

<style scoped>

</style>