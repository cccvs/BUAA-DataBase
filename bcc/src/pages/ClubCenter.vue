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
.side-bar {
  width: 65px;
  transition:width 0.5s;
  -moz-transition:width 0.5s;
  -webkit-transition:width 0.5s;
  -o-transition:width 0.5s;
}

.side-bar:hover{
  width: 150px;
}
</style>