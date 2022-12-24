<template>
  <div class="clubs-container" style="margin-top: 10px">
    <div class="clubBar" v-for="club in clubs" :key="club.data" @dblclick="gotoClub(club)" v-show="checkInfo && club.star < 6 || !checkInfo">
      <div><img :src="club.cover" alt="社团封面" class="club_picture"></div>
      <div class="club_name">{{ club.name }}
        <div class="club_level" v-show="rateClub" @click="starRating(club.club_id,club.star)">
          <v-rating color="yellow" background-color="grey lighten-1" v-model="club.star"></v-rating>
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
          <v-btn v-show="checkInfo" elevation="10" icon circle color="green" @click="handlePass(club)"
                 style="margin-right: 20px">
            <v-icon>
              mdi-check
            </v-icon>
          </v-btn>
          <v-btn v-show="checkInfo" elevation="10" icon color="red" @click="handleFailPass(club)"
                 style="margin-right: 5px">
            <v-icon>
              mdi-close
            </v-icon>
          </v-btn>
        </div>
      </div>
      <div class="club_info">{{clubType(club.type)}} {{club.star}}星级 {{club.time}}</div>
      <div class="club_dis">{{club.intro}}</div>
    </div>
  </div>
</template>

<script>
import Qs from "qs";

export default {
  name: "ClubList",
  props: ["clubs", "rateClub", "checkInfo", "joinClub", "leaveClub"],
  methods: {
    clubType(type) {
      if (type === 0) return '科技'
      if (type === 1) return '人文'
      if (type === 2) return '实践'
      if (type === 3) return '体育'
      if (type === 4) return '艺术'
      if (type === 5) return '其它'
    },
    gotoClub(club) {
      let path = "/myclub/" + club.club_id + "/" + club.name;
      this.$router.push({
        path
      });
    },
    starRating(id,level) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/rate_club_star",
          Qs.stringify({
            club_id: id,
            star: level
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("社团星级已修改");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    joinInClub(id) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/join_club",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            club_id: id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("申请成功，请等待审批");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    quitClub(id) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/quit_club",
          Qs.stringify({
            user_id: localStorage.getItem('user_id'),
            club_id: id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.$message.success("成功退出社团");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    handlePass(club) {
      /*
      DO:团委老师通过社团审批
       */
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_create_club",
          Qs.stringify({
            club_id: club.club_id,
            op: 1
          })
      ).then((res) => {
        if (res.data.code === 0) {
          club.star = 6
          this.$message.success("社团审批通过");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    handleFailPass(club) {
      /*
      DO:团委老师拒绝了社团申请
       */
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_create_club",
          Qs.stringify({
            club_id: club.club_id,
            op: 0
          })
      ).then((res) => {
        if (res.data.code === 0) {
          club.star = 6
          this.$message.success("社团审批拒绝");
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  created() {
    console.log(this.clubs)
  }
}
</script>

<style scoped>
.clubs-container {
  height: 800px;
}

.club_level {
  float: right;
}

.club_check {
  margin-right: 10px;
  float: right;
}

.clubBar {
  width: 600px;
  float: left;
  height: 200px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  margin-right: 20px;
  margin-bottom: 20px;
}

.club_picture {
  margin-left: 10px;
  width: 200px;
  height: 200px;
  float: left;
  margin-right: 30px;
}

.club_name {
  font-size: 30px;
  width: 360px;
  float: left;
  margin-top: 10px;
  margin-bottom: 10px;
}

.club_info {
  float: left;
  width: 360px;
  margin-bottom: 10px;
}

.club_dis {
  word-wrap: break-word;
  display: inline;
}
</style>
