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
            <v-tab>社团申请审批</v-tab>
            <v-tab>社团活动审批</v-tab>
            <v-tab>社团星级评定</v-tab>
            <v-tab-item>
              <ClubList :clubs="tmpList"></ClubList>
            </v-tab-item>
            <v-tab-item>
              <v-row>
                <v-col>
                  <ActivityList></ActivityList>
                </v-col>
                <v-col>
                  <ActivityList></ActivityList>
                </v-col>
                <v-col>
                  <ActivityList></ActivityList>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <ActivityList></ActivityList>
                </v-col>
                <v-col>
                  <ActivityList></ActivityList>
                </v-col>
                <v-col>
                  <ActivityList></ActivityList>
                </v-col>
              </v-row>
            </v-tab-item>
            <v-tab-item>
              <ClubList :clubs="tmpList" rate-club="true"></ClubList>
            </v-tab-item>
          </v-tabs>
        </v-app>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import SideBar from "@/components/SideBar";
import MyHeader from "@/components/MyHeader";
import ClubList from "@/components/ClubList";
import ActivityList from "@/components/ActivityList";

export default {
  name: "ClubCenter",
  components: {ClubList, MyHeader, SideBar, ActivityList},
  data() {
    return {
      tmpList: [
        {
          id: 1,
          name: "凌峰社",
          time: '2010.11.11',
          type: "体育",
          description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
          num: 200,
          level: 5
        },
        {
          id: 2,
          name: "篮球裁判社",
          type: "体育",
          time: '2011.11.11',
          num: 50,
          level: 4
        },
        {
          id: 3,
          name: "科协",
          type: "科技",
          time: '2012.11.11',
          num: 150,
          level: 3
        },
        {
          id: 4,
          name: "知行学社",
          type: "人文",
          time: '2013.11.11',
          num: 100,
          level: 2
        },
        {
          id: 5,
          name: "马克思主义学社",
          type: "人文",
          time: '2013.11.11',
          num: 100,
          level: 2
        }
      ],
    }
  }
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