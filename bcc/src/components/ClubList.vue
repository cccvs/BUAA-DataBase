<template>
  <div class="clubs-container" style="margin-top: 10px">
    <div class="clubBar" v-for="club in clubs" :key="club.data" @dblclick="gotoClub(club)">
      <div><img :src="club.cover" alt="社团封面" class="club_picture"></div>
      <div class="club_name">{{club.name}}
        <div class="club_level" v-show="rateClub">
          <v-rating color="yellow" background-color="grey lighten-1" v-model="club.level" ></v-rating>
        </div>
        <div class="club_check">
<!--          <el-switch-->
<!--              v-model="club.isPass"-->
<!--              active-color="#13ce66"-->
<!--              inactive-color="#ff4949"-->
<!--              active-text="通过">-->
<!--          </el-switch>-->
          <v-btn v-show="joinClub" style="margin-right: 5px" color="blue lighten-3" @click="joinInClub(club.club_id)">
            加入社团
          </v-btn>
          <v-btn v-show="leaveClub" style="margin-right: 5px" color="yellow lighten-3" @click="quitClub(club.club_id)">
            退出社团
          </v-btn>
          <v-btn v-show="checkInfo" elevation="10" icon circle color="green" @click="handlePass(club.id)"
                 style="margin-right: 20px">
            <v-icon>
              mdi-check
            </v-icon>
          </v-btn>
          <v-btn v-show="checkInfo" elevation="10" icon color="red" @click="handleFailPass(club.id)"
                 style="margin-right: 5px">
            <v-icon>
              mdi-close
            </v-icon>
          </v-btn>
        </div>
      </div>
      <div class="club_info">{{club.type}} {{club.level}}星级 {{club.time}}</div>
      <div class="club_dis">{{club.description}}</div>
    </div>
  </div>
</template>

<script>
import Qs from "qs";

export default {
  name: "ClubList",
  props: ["clubs", "rateClub", "checkInfo", "joinClub", "leaveClub"],
  methods: {
    gotoClub(club) {
      if (this.$router.history.current.params.id !== club.id) {
        let path = "/myclub/" +  club.id + "/" + club.name;
        this.$router.push({
          path
        });
      }
    },
    joinInClub(id) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/join_club",
          Qs.stringify({
            user_id:localStorage.getItem('user_id'),
            club_id:id
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.$message.success("申请成功，请等待审批");
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    quitClub(id) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/quit_club",
          Qs.stringify({
            user_id:localStorage.getItem('user_id'),
            club_id:id
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.$message.success("成功退出社团");
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    methods:{
      handlePass(id) {
        /*
        TODO:团委老师通过社团审批
         */
        console.log(id);
      },
      handleFailPass(id) {
        /*
        TODO:团委老师拒绝了社团申请
         */
        console.log(id);
      }
    }
  }
}
</script>

<style scoped>
.clubs-container{
  height: 800px;
}
.club_level {
  float: right;
}
.club_check {
  margin-right: 10px;
  float: right;
}
.clubBar{
  width: 650px;
  float: left;
  height: 200px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  margin-right: 20px;
  margin-bottom: 20px;
}
.club_picture{
  margin-left: 10px;
  width: 200px;
  height: 200px;
  float: left;
  margin-right: 30px;
}
.club_name{
  font-size: 50px;
  width: 410px;
  float: left;
  margin-top: 10px;
  margin-bottom: 10px;
}
.club_info{
  float: left;
  width: 410px;
  margin-bottom: 10px;
}
.club_dis{
  word-wrap: break-word;
  display: inline;
}
</style>
