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
        <v-app>
          <v-card>
            <v-tabs
                background-color="white"
                color="deep-purple accent-4"
                left
            >
              <v-tab>审核信息</v-tab>
              <v-tab>发布公告</v-tab>
              <v-tab>创建活动</v-tab>
              <v-tab>修改社团信息</v-tab>
              <v-tab>指定社团骨干</v-tab>
              <v-tab>社长换届</v-tab>
              <v-tab-item>
                <CheckInfo></CheckInfo>
              </v-tab-item>
              <v-tab-item>
                <PublishNotice></PublishNotice>
              </v-tab-item>
              <v-tab-item>
                <CreateActivity></CreateActivity>
              </v-tab-item>
            </v-tabs>
          </v-card>
        </v-app>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import MyHeader from "@/components/MyHeader";
import SideBar from "@/components/SideBar";
import CheckInfo from "@/components/CheckInfo";
import PublishNotice from "@/components/PublishNotice";
import CreateActivity from "@/components/CreateActivity";
export default {
  name: "ClubManage",
  components: {CreateActivity, PublishNotice, CheckInfo, MyHeader, SideBar},
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