<template>
  <v-app style="height:100%;overflow-y: hidden;overflow-x: hidden">
    <v-list subheader>
      <v-list-item
          v-for="reply in replies"
          :key="reply.reply_id"
      >
        <v-icon large color="blue darken-2">mdi-message-text</v-icon>
        <v-list-item-content style="padding-left: 10px" v-text="reply.content">
        </v-list-item-content>
        <v-spacer></v-spacer>
        <v-list-item-content style="margin-right: 10px">2022-10-15 10:04</v-list-item-content>
      </v-list-item>
    </v-list>
    <v-card-text style="margin-top: 30px">以陈俊杰的身份参与讨论：</v-card-text>
    <mavon-editor
        v-model="newReply.content"
        style="margin-top: 20px;height: 100%;width:100%;align-self: center"
        ref=md
        @change="change"
        fontSize="16px">
    </mavon-editor>
    <v-btn @click="submit" style="margin-top: 20px;float: left;width: 20px" color="pink accent-4">
      提交
    </v-btn>
  </v-app>

</template>

<script>
export default {
  name: "ReplyList",
  props: ["replies"],
  data() {
    return {
      newReply: {
        content:"",
        html:""
      }
    }
  },
  methods: {
    // 所有操作都会被解析重新渲染
    change(value, render){
      // render 为 markdown 解析后的结果[html]
      this.html = render;
    },
    // 提交
    submit(){
      console.log(this.newReply.content); //内容
      console.log(this.newReply.html);
      /*
      TODO:将这里的数据传到后端，在后端存储生成id存储
       */
    }
  },
}
</script>

<style scoped>

</style>