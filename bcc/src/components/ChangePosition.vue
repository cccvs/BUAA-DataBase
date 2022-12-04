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
                text="您可以社团成员骨干或进行社长换届" change-position="true"></MemberList>
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
    return {
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
  methods: {
    handelChangePosition(id) {
      let newLabel
      this.members.forEach((member) => {
        if (member.id === id) newLabel = member.label
      })
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