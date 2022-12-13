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
import Qs from "qs";
export default {
  name: "CheckInfo",
  components: {MemberList, MySnackBar},
  props: ["requests"],
  data() {
    return {
      /*
      DO: 前端容器requests，也需要在挂载的时候从后端获取，
       只需要将容器传递给MemberList，模式设定为check-info，requset是否需要自己的id？
       */
      request: [{
        user_id: "20373021",
        real_name: "陈俊杰",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg"
      }, {
        user_id: "123",
        real_name: "蒋博文",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
      }, {
        user_id: "124",
        real_name: "陈楚岩",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
      }]
    }
  },
  methods: {
    /*
    DO: 申请加入社团请求通过的接口
     */
    handlePass(id) {
      let curRequest = this.requests.filter((request) => {
        return request.user_id === id;
      })
      console.log(curRequest)
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_joining_club",
          Qs.stringify({
            op: 0,
            request_id: curRequest[0].form_id
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.$bus.$emit('showSnackBar', "审核成功，该学生成功加入社团！")
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    /*
    DO: 申请加入社团请求拒绝的接口
     */
    handleFailPass(id) {
      let curRequest = this.requests.filter((request) => {
        return request.user_id === id;
      })
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_joining_club",
          Qs.stringify({
            op: 1,
            request_id: curRequest.form_id
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.$bus.$emit('showSnackBar', "已拒绝该学生成功加入社团")
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
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
