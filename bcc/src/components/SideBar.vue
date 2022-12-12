<template>
  <div @mouseover="mouseOver"
       @mouseleave="mouseLeave"
       class="showHide">
    <el-menu :default-active="this.$router.path"
             router
             class="el-menu-vertical-demo"
             :collapse="isCollapse"
             :collapse-transition="false"
    >
      <el-menu-item index="/mainpage" router>
        <i class="el-icon-video-camera"></i>
        <span slot="title">社团风采</span>
      </el-menu-item>
      <el-menu-item index="/findclub" router>
        <i class="el-icon-search"></i>
        <span slot="title">发现社团</span>
      </el-menu-item>
      <el-submenu index="/myclub">
        <template slot="title">
          <i class="el-icon-place"></i>
          <span slot="title">我的社团</span>
        </template>
        <el-menu-item v-for="club in myClub"
        :key="club.id" :index="`/myclub/${club.id}/${club.name}`" router>
          {{club.name}}
        </el-menu-item>
      </el-submenu>
      <el-menu-item :index="`/usercenter/${this.user_id}/${this.user_name}`" router>
        <i class="el-icon-user-solid"></i>
        <span slot="title">个人中心</span>
      </el-menu-item>
      <el-menu-item index="/clubmanage" router :class="[{'hid': !hasClub}]">
        <i class="el-icon-s-order"></i>
        <span slot="title">社团管理</span>
      </el-menu-item>
      <el-menu-item index="/clubcenter" router>
        <i class="el-icon-office-building"></i>
        <span slot="title">社团中心</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>

import Qs from "qs";

export default {
  name: "SideBar",
  data() {
    return {
      hasClub: false,
      isCollapse: true,
      user_id: "20373021",
      user_name: "陈俊杰",
      myClub: [{
        id: 1,
        name: "凌峰社"
      }, {
        id: 2,
        name: "篮球裁判社"
      }, {
        id: 3,
        name: "科协"
      }]
    };
  },
  methods: {
    getClubList(){
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_club_list",
          Qs.stringify({
            jwt: {'code':localStorage.getItem('code'),'user_id':localStorage.getItem('user_id'),'time':localStorage.getItem('time')}
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(res.data)
          this.myClub = res.data.club_list;
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    getMasterClubList(){
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_master_club_list",
          Qs.stringify({
            jwt: {'code':localStorage.getItem('code'),'user_id':localStorage.getItem('user_id'),'time':localStorage.getItem('time')}
          })
      ).then((res)=>{
        if(res.data.code===0){
          console.log(res.data)
          if (res.data.club_list.length > 0) {
            this.hasClub = true;
          }
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    mouseOver() {
      this.isCollapse = false
    },
    mouseLeave() {
      this.isCollapse = true
    }
  },
  created() {
    this.getClubList();
    this.getMasterClubList();
  }
}
</script>
<style>
.hid{
  display: none;
}
</style>
