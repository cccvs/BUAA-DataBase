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
    }
  },
  methods: {
    /*
    TODO: 关注/取消关注接口
     */
    handelFollow(id) {
      console.log(id)
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
        let path = "/usercenter/" +  member.user_id + "/" + member.real_name;
        this.$router.push({
          path
        });
      }
    }
  }
}
</script>

<style scoped>

</style>