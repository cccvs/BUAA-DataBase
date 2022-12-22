<template>
  <v-container fluid>
    <v-row>
      <v-icon color="blue" style="margin-left: 10px;margin-top: 10px">mdi-clipboard-text-multiple-outline</v-icon>
      <h1 style="margin-left: 10px;margin-top: 10px">发布新的公告！</h1>
    </v-row>
    <v-row>
      <v-col cols="5">
        <v-text-field label="标题" hide-details="auto"
                      style="padding-bottom: 20px"
                      v-model="notice.title">
        </v-text-field>
      </v-col>
      <v-col cols="5">
        <v-checkbox label="置顶" v-model="notice.top">
        </v-checkbox>
      </v-col>
    </v-row>
    <v-textarea
        counter
        auto-grow
        clearable
        clear-icon="mdi-close"
        label="正文内容"
        v-model="notice.content"
    ></v-textarea>
    <v-btn color="primary" @click="handlePublish">
      <v-icon dark style="margin-right: 5px">mdi-checkbox-marked-circle</v-icon>
      确认发布
    </v-btn>
    <MySnackBar></MySnackBar>
  </v-container>
</template>

<script>
import MySnackBar from "@/components/MySnackBar";
import Qs from "qs";
export default {
  name: "PublishNotice",
  components: {MySnackBar},
  props:['clubId'],
  data() {
    return {
      /*
      TODO:前端容器，格式可以和后端配合
       */
      notice: {
        id: 1,
        title: "",
        content: "",
        user_id: 20373021,
        top: false,
      }
    }
  },
  methods:{
    /*
    DO: 发布公告的接口，暂时没有添加任何约束。如果置顶，可以将公告插入到后端容器首？
    */
    handlePublish() {
      this.$axios.post(
          "http://127.0.0.1:8000/api/publish_notice",
          Qs.stringify({
            title:this.notice.title,
            content:this.notice.content,
            user_id:localStorage.getItem('user_id'),
            club_id:this.clubId,
            top:this.notice.top ? 1 : 0
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(this.clubId)
          this.notice.title = ''
          this.notice.content = ''
          this.notice.top = false
          this.$bus.$emit('showSnackBar', "发布成功！")
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
