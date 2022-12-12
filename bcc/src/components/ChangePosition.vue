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
import Qs from "qs";

export default {
  name: "ChangePosition",
  components: {MySnackBar, MemberList},
  props: ["members","clubId"],
  data() {
    return {
      // member: [{
      //   user_id: "20373021",
      //   real_name: "陈俊杰",
      //   avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
      //   label: "社长"
      // }, {
      //   user_id: "123",
      //   real_name: "蒋博文",
      //   avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      //   label: "副社长"
      // }, {
      //   user_id: "124",
      //   real_name: "陈楚岩",
      //   avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg',
      //   label: "办公室部长"
      // }]
    }
  },
  methods: {
    handelChangePosition(id) {
      let newLabel
      this.members.forEach((member) => {
        if (member.user_id === id) newLabel = member.label
      })
      console.log(this.clubId)
      // console.log(newLabel);
      this.$axios.post(
          "http://127.0.0.1:8000/api/change_position",
          Qs.stringify({
            user_id:id,
            club_id: this.clubId,
            label:newLabel
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.$bus.$emit('showSnackBar', "修改成功，该学生已成为社团" + newLabel)
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
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
