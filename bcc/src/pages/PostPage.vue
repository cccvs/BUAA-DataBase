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
        <ReplyList :replies="replies"></ReplyList>
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
      replies: [{
        reply_id: 1,
        like: 22,
        dislike: 0,
        content: "省流不看版 ..."
      }, {
        reply_id: 2,
        like: 22,
        dislike: 0,
        content: "省流不看版 ..."
      }],
    }
  },
}
</script>

<style scoped>

</style>