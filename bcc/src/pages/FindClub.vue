<template>
  <el-tabs>
    <el-tab-pane label="加入社团" name="first">
      <find-club1></find-club1>
    </el-tab-pane>
    <el-tab-pane label="创建社团" name="second">
      <find-club2></find-club2>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import FindClub1 from "@/pages/FindClub1";
import FindClub2 from "@/pages/FindClub2";
export default {
  name: "FindClub",
  components: {FindClub2, FindClub1}
}
</script>

<style scoped>

</style>