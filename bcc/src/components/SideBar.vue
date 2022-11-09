<template>
  <el-aside width="200px">
    <el-menu :default-active="this.$router.path"
             router
             class="el-menu-vertical-demo"
             :collapse="isCollapse">
      <el-menu-item index="mainpage" router>
        <i class="el-icon-video-camera"></i>
        <span slot="title">社团风采</span>
      </el-menu-item>
      <el-menu-item index="findclub" router>
        <i class="el-icon-search"></i>
        <span slot="title">发现社团</span>
      </el-menu-item>
      <el-submenu index="myclub" router>
        <template slot="title">
          <i class="el-icon-place"></i>
          <span slot="title">我的社团</span>
        </template>
        <el-menu-item index="myclub">凌峰社</el-menu-item>
        <el-menu-item index="myclub">篮球裁判社</el-menu-item>
      </el-submenu>
      <el-menu-item index="usercenter" router>
        <i class="el-icon-user-solid"></i>
        <span slot="title">个人中心</span>
      </el-menu-item>
      <el-menu-item index="clubmanage" router>
        <i class="el-icon-s-order"></i>
        <span slot="title">社团管理</span>
      </el-menu-item>
      <el-menu-item index="clubcenter" router>
        <i class="el-icon-office-building"></i>
        <span slot="title">社团中心</span>
      </el-menu-item>
    </el-menu>
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
  </el-aside>
</template>

<script>
export default {
  name: "SideBar",
  data() {
    return {
      isCollapse: false
    };
  }
}
</script>

<style scoped>

</style>