<template>
  <v-list subheader>
    <v-subheader>{{ text }}</v-subheader>
    <v-list-item
        v-for="member in members"
        :key="member.user_id"
        @dblclick="detailOfUser(member)">
      <v-list-item-avatar>
        <v-avatar>
          <img :src="member.avatar" alt="头像">
        </v-avatar>
      </v-list-item-avatar>
      <v-list-item-content style="padding-left: 10px">
        <v-list-item-title v-text="member.real_name"></v-list-item-title>
        <v-list-item-subtitle v-text="member.label"></v-list-item-subtitle>
      </v-list-item-content>
      <v-spacer></v-spacer>
      <v-btn v-show="checkInfo" elevation="10" icon circle color="green" @click="handlePass(member.user_id)"
             style="margin-right: 20px">
        <v-icon>
          mdi-check
        </v-icon>
      </v-btn>
      <v-btn v-show="checkInfo" elevation="10" icon color="red" @click="handleFailPass(member.user_id)"
             style="margin-right: 5px">
        <v-icon>
          mdi-close
        </v-icon>
      </v-btn>
      <el-select filterable v-show="changePosition" v-model="member.label" placeholder="请选择"
                 style="margin-right: 20px">
        <el-option
            v-for="item in items"
            :key="item.id"
            :label="item.label"
            :value="item.label">
        </el-option>
      </el-select>
      <v-btn v-show="changePosition"
             color="blue lighten-3"
             @click="handelChangePosition(member.user_id)">确认修改
      </v-btn>
      <v-btn v-show="follow&&member.is_follow === 0&&(member.user_id !== curId)"
             color="blue lighten-3"
             @click="handelFollow(member)"
             style="min-width: 120px">
        <v-icon>
          mdi-account-heart
        </v-icon>
        关注
      </v-btn>
      <v-btn v-show="follow&&member.is_follow === 1&&(member.user_id !== curId)"
             color="orange lighten-3"
             @click="handleUnFollow(member)"
      >
        <v-icon>
          mdi-account-cancel
        </v-icon>
        取消关注
      </v-btn>
    </v-list-item>
  </v-list>
</template>

<script>
import Qs from "qs";

export default {
  name: "MemberList",
  props: ["members", "checkInfo", "text", "changePosition", "follow"],
  data() {
    return {
      // '社长', '副社长', '办公室部长'
      /*
      DO: 获取当前ID
       */
      curId:localStorage.getItem('user_id'),
      items: [{
        id: 1,
        label: "社长"
      }, {
        id: 2,
        label: "副社长"
      }, {
        id: 3,
        label: "办公室部长"
      }],
    }
  },
  methods: {
    /*
    DO: 关注/取消关注接口
     */
    handelFollow(member) {
      // console.log(id)
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_following",
          Qs.stringify({
            'follower_id': localStorage.getItem('user_id'),
            'friend_id': member.user_id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          // console.log(res.data)
          member.is_follow = 1
          this.$message.success("你已成功关注！")
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    handleUnFollow(member) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_unfollowing",
          Qs.stringify({
            'follower_id': localStorage.getItem('user_id'),
            'friend_id': member.user_id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          // console.log(res.data)
          member.is_follow = 0
          this.$message.success("你已成功取消关注！")
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    handlePass(id) {
      this.$bus.$emit('handlePass', id)
    },
    handleFailPass(id) {
      this.$bus.$emit('handleFailPass', id)
    },
    handelChangePosition(id) {
      this.$bus.$emit('handelChangePosition', id)
    },
    detailOfUser(member) {
      if (this.$router.history.current.params.id !== member.user_id) {
        let path = "/usercenter/" + member.user_id + "/" + member.real_name;
        this.$router.push({
          path
        });
      }
    }
  },
}
</script>
<style>
</style>
