<template>
  <el-container>
    <SideBar></SideBar>
    <el-container>
      <el-header>
        <MyHeader></MyHeader>
      </el-header>
      <el-main>
        <h1>社团中心</h1>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import SideBar from "@/components/SideBar";
import MyHeader from "@/components/MyHeader";
export default {
  name: "ClubCenter",
  components: {MyHeader, SideBar}
}
</script>

<style scoped>

</style>