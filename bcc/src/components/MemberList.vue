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
      <v-btn v-show="follow"
             color="blue lighten-3"
             @click="handelFollow(member.user_id)">关注
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
      tableData: [
        {index: 1, name: '我是1号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 2, name: '我是2号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 3, name: '我是3号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 4, name: '我是4号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 5, name: '我是5号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 6, name: '我是6号', age: 18, sex: '女', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 7, name: '我是7号', age: 18, sex: '女', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 8, name: '我是8号', age: 18, sex: '女', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 9, name: '我是9号', age: 18, sex: '女', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 10, name: '我是10号', age: 18, sex: '女', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 11, name: '我是11号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 12, name: '我是12号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 13, name: '我是13号', age: 18, sex: '女', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 14, name: '我是14号', age: 18, sex: '女', hobby: 'web', hair: 'thick', salaried: '99999999'},
        {index: 15, name: '我是15号', age: 18, sex: '男', hobby: 'web', hair: 'thick', salaried: '99999999'}
      ],
    }
  },
  methods: {
    /*
    DO: 关注/取消关注接口
     */
    handelFollow(id) {
      // console.log(id)
      this.$axios.post(
          "http://127.0.0.1:8000/api/handle_following",
          Qs.stringify({
            'follower_id': localStorage.getItem('user_id'),
            'friend_id': id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          // console.log(res.data)
          this.$bus.$emit('showSnackBar', "你已成功关注！")
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
  }
}
</script>
<style>
</style>
