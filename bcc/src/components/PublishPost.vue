<template>
  <v-container fluid>
    <v-row>
      <v-icon color="blue" style="margin-left: 10px;margin-top: 10px">mdi-clipboard-text-multiple-outline</v-icon>
      <h1 style="margin-left: 10px;margin-top: 10px">参与到讨论中来！</h1>
    </v-row>
    <v-row>
        <v-text-field label="标题" hide-details="auto"
                      style="padding-bottom: 20px;margin-left: 10px"
                      v-model="post.title">
        </v-text-field>
    </v-row>
    <mavon-editor
        v-model="newPost.content"
        style="margin-top: 20px;height: 100%;width:100%;align-self: center"
        ref=md
        @change="change"
        fontSize="16px">
    </mavon-editor>
    <v-btn @click="submit" style="margin-top: 20px;float: left;width: 20px" color="primary">
      发布
    </v-btn>
    <MySnackBar></MySnackBar>
  </v-container>
</template>

<script>
import MySnackBar from "@/components/MySnackBar";

export default {
  name: "PublishPost",
  components: {MySnackBar},
  data() {
    return {
      /*
      TODO:前端容器，格式可以和后端配合
       */
      post: {
        id: 1,
        title: "",
        content: "",
        user_id: 20373021,
        top: true
      },
      newPost: {
        content: "",
        html: ""
      }
    }
  },
  methods: {
    handlePublish() {
      this.$bus.$emit('showSnackBar', "发布成功！")
    },
    // 所有操作都会被解析重新渲染
    change(value, render) {
      // render 为 markdown 解析后的结果[html]
      this.newPost.html = render;
    },
    // 提交
    submit() {
      console.log(this.newPost.content); //内容
      console.log(this.newPost.html); //dom 结构
      /*
      TODO:将这里的数据传到后端，在后端存储生成id存储
       */
    }
  }
}
</script>

<style scoped>

</style>