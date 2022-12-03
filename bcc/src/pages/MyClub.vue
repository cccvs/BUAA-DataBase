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