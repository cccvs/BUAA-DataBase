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
                <CheckInfo :requests="clubRequests"></CheckInfo>
              </v-tab-item>
              <v-tab-item>
                <PublishNotice :clubId="clubId"></PublishNotice>
              </v-tab-item>
              <v-tab-item>
                <CreateActivity :club_id="clubId"></CreateActivity>
              </v-tab-item>
              <v-tab-item>
                <v-row style="margin-left: 10px;margin-top: 5px">
                  <v-icon color="blue">mdi-clipboard-text-search</v-icon>
                  <h1 style="margin-left: 10px;margin-top: 10px">修改社团的基本信息！</h1>
                </v-row>
                <FindClub2 style="margin-top: 10px" option="确认修改"></FindClub2>
              </v-tab-item>
              <v-tab-item>
                <ChangePosition :members="clubMembers" :club-id="clubId"></ChangePosition>
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
import Qs from "qs";
export default {
  name: "ClubManage",
  components: {ChangePosition, FindClub2, CreateActivity, PublishNotice, CheckInfo, MyHeader, SideBar},
  data() {
    return {
      masterClub:[],
      clubMembers:[],
      clubRequests:[],
      clubId:''
    }
  },
  methods: {
    getMasterClubList(){
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_master_club_list",
          Qs.stringify({
            jwt: {'code':localStorage.getItem('code'),'user_id':localStorage.getItem('user_id'),'time':localStorage.getItem('time')}
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(res.data)
          this.masterClub = res.data.club_list;
          this.clubId = this.masterClub[0].club_id;
          this.getClubMembers();
          this.getClubRequests();
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    getClubMembers(){
      console.log(this.clubId)
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_club_members",
          Qs.stringify({
            club_id: this.clubId
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(res.data)
          this.clubMembers = res.data.member_list;
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    getClubRequests(){
      console.log(this.clubId)
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_club_requests",
          Qs.stringify({
            club_id: this.clubId
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(res.data)
          this.clubRequests = res.data.requests;
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
  },
  created() {
    this.getMasterClubList();
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
