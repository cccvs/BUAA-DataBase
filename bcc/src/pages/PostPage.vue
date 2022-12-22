<template>
  <el-container>
    <div class="side-bar">
      <SideBar></SideBar>
    </div>
    <el-container>
      <el-header>
        <MyHeader></MyHeader>
      </el-header>
      <el-main>
        <ReplyList :replies="replies" :post="curPost"></ReplyList>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import MyHeader from "@/components/MyHeader";
import SideBar from "@/components/SideBar";
import ReplyList from "@/components/ReplyList";

export default {
  name: "PostPage",
  components: {ReplyList, SideBar, MyHeader},
  data() {
    return {
      /*
      TODO: 通过路由参数获取post
       */
      curPost: {
        post_id: 1,
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        user_name: "陈俊杰",
        title: "自动化测试",
        like: 22,
        dislike: 0,
        time: "2022-12-20 12:40:20",
        content: "省流不看版 ..."
      },
      replies: [{
        reply_id: 1,
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        user_name: "陈俊杰",
        title: "自动化测试",
        like: 22,
        dislike: 8,
        time: "2022-12-20 12:40:20",
        content: "省流不看版 ..."
      }, {
        reply_id: 2,
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        user_name: "陈俊杰",
        title: "自动化测试",
        like: 22,
        dislike: 0,
        time: "2022-10-15 10:04:20",
        content: "66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666"
      }],
    }
  },
}
</script>

<style scoped>

</style>