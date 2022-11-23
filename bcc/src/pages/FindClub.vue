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
        <el-tabs>
          <el-tab-pane label="加入社团" name="first">
            <find-club1></find-club1>
          </el-tab-pane>
          <el-tab-pane label="创建社团" name="second">
            <find-club2></find-club2>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import FindClub1 from "@/components/FindClub1";
import FindClub2 from "@/components/FindClub2";
import MyHeader from "@/components/MyHeader";
import SideBar from "@/components/SideBar";

export default {
  name: "FindClub",
  components: {FindClub2, FindClub1, MyHeader, SideBar}
}
</script>

<style scoped>
.side-bar {
  width: 65px;
  transition: width 0.5s;
  -moz-transition: width 0.5s;
  -webkit-transition: width 0.5s;
  -o-transition: width 0.5s;
}

.side-bar:hover {
  width: 150px;
}
</style>