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
            <v-tab>概览</v-tab>
            <v-tab>成员</v-tab>
            <v-tab>活动</v-tab>
            <v-tab>公告</v-tab>
            <v-tab-item>
              <ClubList :clubs="curClub"></ClubList>
            </v-tab-item>
            <v-tab-item>
              <MemberList :members="members"></MemberList>
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
              <NoticeList></NoticeList>
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
import ClubList from "@/components/ClubList";
import MemberList from "@/components/MemberList";
import ActivityList from "@/components/ActivityList";
import NoticeList from "@/components/NoticeList";
export default {
  name: "MyClub",
  components: {NoticeList, ActivityList, MemberList, ClubList, MyHeader, SideBar},
  data() {
    return {
      curClub:[{
        id: 1,
        name: "凌峰社",
        time:'2010.11.11',
        type:"体育",
        description:"是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
        num: 200,
        level: 5
      }],
      members: [{
        id: "20373021",
        userName: "陈俊杰",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        label: "社长"
      }, {
        id: "123",
        userName: "蒋博文",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        label: "副社长"
      }, {
        id: "124",
        userName: "陈楚岩",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        label: "办公室部长"
      }]
    }
  },
  mounted() {
    let id = Number(this.$router.history.current.params.id);
    let myClubList =  [
      {
        id: 1,
        name: "凌峰社",
        time:'2010.11.11',
        type:"体育",
        description:"是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
        num: 200,
        level: 5
      },
      {
        id: 2,
        name: "篮球裁判社",
        type:"体育",
        time:'2011.11.11',
        num: 50,
        level: 4
      },
      {
        id: 3,
        name: "科协",
        type:"科技",
        time:'2012.11.11',
        num: 150,
        level: 3
      },
      {
        id: 4,
        name: "知行学社",
        type:"人文",
        time:'2013.11.11',
        num: 100,
        level: 2
      }
    ];
    this.curClub = myClubList.filter((club) => {
      return club.id === id
    })
  },
  beforeRouteUpdate(to, from, next) {
    if (to.params && from.params && to.params.id !== from.params.id) {
      console.log("update");
      let id = Number(to.params.id);
      let myClubList =  [
        {
          id: 1,
          name: "凌峰社",
          time:'2010.11.11',
          type:"体育",
          description:"是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
          num: 200,
          level: 5
        },
        {
          id: 2,
          name: "篮球裁判社",
          type:"体育",
          time:'2011.11.11',
          num: 50,
          level: 4
        },
        {
          id: 3,
          name: "科协",
          type:"科技",
          time:'2012.11.11',
          num: 150,
          level: 3
        },
        {
          id: 4,
          name: "知行学社",
          type:"人文",
          time:'2013.11.11',
          num: 100,
          level: 2
        }
      ];
      this.curClub = myClubList.filter((club) => {
        return club.id === id
      })
      next();
    }
  }
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