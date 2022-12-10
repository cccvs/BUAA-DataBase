<template>
  <div class="clubs-container" style="margin-top: 10px">
    <div class="clubBar" v-for="club in clubs" :key="club.data" @dblclick="gotoClub(club)">
      <div class="club_picture"><img src="../assets/logo.png" alt="社团封面"></div>
      <div class="club_name">{{club.name}}
        <div class="club_level" v-show="rateClub">
          <v-rating color="yellow" background-color="grey lighten-1" v-model="club.level" ></v-rating>
        </div>
        <div class="club_check" v-show="checkInfo">
<!--          <el-switch-->
<!--              v-model="club.isPass"-->
<!--              active-color="#13ce66"-->
<!--              inactive-color="#ff4949"-->
<!--              active-text="通过">-->
<!--          </el-switch>-->
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
export default {
  name: "ClubList",
  props: ["clubs", "rateClub", "checkInfo"],
  methods: {
    gotoClub(club) {
      if (this.$router.history.current.params.id !== club.id) {
        let path = "/myclub/" +  club.id + "/" + club.name;
        this.$router.push({
          path
        });
      }
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