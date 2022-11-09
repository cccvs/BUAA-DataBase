<template>
  <el-container>
    <SideBar></SideBar>
    <el-container>
      <el-header>
        <MyHeader></MyHeader>
      </el-header>
      <el-main>
        <h1>我的社团</h1>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import MyHeader from "@/components/MyHeader";
import SideBar from "@/components/SideBar";
export default {
  name: "MyClub",
  components: {MyHeader, SideBar}
}
</script>

<style scoped>

</style>