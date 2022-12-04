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
            <v-tabs
                background-color="white"
                color="deep-purple accent-4"
                left
            >
              <v-tab>审核信息</v-tab>
              <v-tab>发布公告</v-tab>
              <v-tab>创建活动</v-tab>
              <v-tab>修改社团信息</v-tab>
              <v-tab>职务变动</v-tab>
              <v-tab-item>
                <CheckInfo></CheckInfo>
              </v-tab-item>
              <v-tab-item>
                <PublishNotice></PublishNotice>
              </v-tab-item>
              <v-tab-item>
                <CreateActivity></CreateActivity>
              </v-tab-item>
              <v-tab-item>
                <v-row style="margin-left: 10px;margin-top: 5px">
                  <v-icon color="blue">mdi-clipboard-text-search</v-icon>
                  <h1 style="margin-left: 10px;margin-top: 10px">修改社团的基本信息！</h1>
                </v-row>
                <FindClub2 style="margin-top: 10px"></FindClub2>
              </v-tab-item>
              <v-tab-item>
                <ChangePosition></ChangePosition>
              </v-tab-item>
            </v-tabs>
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
import FindClub2 from "@/components/FindClub2";
import ChangePosition from "@/components/ChangePosition";
export default {
  name: "ClubManage",
  components: {ChangePosition, FindClub2, CreateActivity, PublishNotice, CheckInfo, MyHeader, SideBar},
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