<template>
  <v-card
      max-width="100%"
      class="align-center"
  >
    <v-row style="margin-left: 10px;margin-top: 10px">
      <v-icon color="blue">mdi-account-sync</v-icon>
      <h1 style="margin-left: 10px;margin-top: 10px">管理社内职务！</h1>
    </v-row>
    <MemberList :members="members"
                style="margin-top: 20px"
                text="您可以社团成员骨干或进行社长换届" :change-position="true"></MemberList>
    <MySnackBar></MySnackBar>
  </v-card>
</template>

<script>
import MemberList from "@/components/MemberList";
import MySnackBar from "@/components/MySnackBar";

export default {
  name: "ChangePosition",
  components: {MySnackBar, MemberList},
  data() {
    /*
    TODO: 前端容器，保存社团成员，应该在挂载时获取。
     */
    return {
      members: [{
        user_id: "20373021",
        real_name: "陈俊杰",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        label: "社长"
      }, {
        user_id: "123",
        real_name: "蒋博文",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        label: "副社长"
      }, {
        user_id: "124",
        real_name: "陈楚岩",
        avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
        label: "办公室部长"
      }]
    }
  },
  methods: {
    /*
    TODO:确认修改的接口，这里只修改了前端容器，需要同步到后端，可以写一个触发器，验证某种职务是否人数已满
     */
    handelChangePosition(id) {
      let newLabel
      this.members.forEach((member) => {
        if (member.user_id === id) newLabel = member.label
      })
      console.log(newLabel);
      this.$bus.$emit('showSnackBar', "修改成功，该学生已成为社团" + newLabel)
    }
  },
  mounted() {
    this.$bus.$on("handelChangePosition", this.handelChangePosition)
  },
  beforeDestroy() {
    this.$bus.$off("handelChangePosition", this.handelChangePosition)
  }
}
</script>

<style scoped>

</style>