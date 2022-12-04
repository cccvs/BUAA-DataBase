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
              <ClubList :clubs="clubList" check-info="true"></ClubList>
            </v-tab-item>
            <v-tab-item>
              <ActivityList :activities="activities"></ActivityList>
            </v-tab-item>
            <v-tab-item>
              <ClubList :clubs="clubList" rate-club="true"></ClubList>
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
      clubList: [
        {
          id: 1,
          name: "凌峰社",
          time: '2010.11.11',
          type: "体育",
          description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
          num: 200,
          level: 5,
          isPass: false
        },
        {
          id: 2,
          name: "篮球裁判社",
          type: "体育",
          time: '2011.11.11',
          num: 50,
          level: 4,
          isPass: false
        },
        {
          id: 3,
          name: "科协",
          type: "科技",
          time: '2012.11.11',
          num: 150,
          level: 3,
          isPass: false
        },
        {
          id: 4,
          name: "知行学社",
          type: "人文",
          time: '2013.11.11',
          num: 100,
          level: 2,
          isPass: false
        },
        {
          id: 5,
          name: "马克思主义学社",
          type: "人文",
          time: '2013.11.11',
          num: 100,
          level: 2,
          isPass: false
        }
      ],
      activities: [{
        id: 1,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24
      },{
        id: 2,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24
      },{
        id: 3,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24
      },{
        id: 4,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24
      },{
        id: 5,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24
      },{
        id: 6,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24
      }]
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