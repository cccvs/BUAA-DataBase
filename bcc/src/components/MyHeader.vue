<template>
  <div>
    <div class="flexs">
      <h1>上午好，{{ userName }}</h1>
      <el-badge :value="messages.length" :hidden="hidden" v-show="messages.length!==0">
        <el-button circle @click="quit" icon="el-icon-switch-button"></el-button>
        <el-button @click="drawer=true" circle icon="el-icon-message-solid"></el-button>
      </el-badge>
      <div v-show="messages.length===0">
        <el-button circle @click="quit" icon="el-icon-switch-button"></el-button>
        <el-button @click="drawer=true" circle icon="el-icon-message-solid"></el-button>
      </div>
    </div>
    <el-drawer
        title="新消息列表"
        :visible.sync="drawer"
        direction="rtl">
      <v-list subheader>
        <v-list-item
            v-for="message in messages"
            :key="message.time">
          <v-list-item-content>
            <v-list-item-title v-text="message.time"></v-list-item-title>
            <v-card-text v-text="message.content"></v-card-text>
          </v-list-item-content>
          <el-button type="success" icon="el-icon-check" circle @click="deleteMessage(message.message_id)"></el-button>
        </v-list-item>
        <el-button icon="el-icon-finished" style="margin-left: 10px" @click="deleteAllMessages">全部已读</el-button>
        <v-divider></v-divider>
      </v-list>
    </el-drawer>
    <hr/>
  </div>
</template>

<script>
import Qs from "qs";

export default {
  name: "MyHeader",
  data() {
    return {
      userName: '',
      hidden: false,
      messageCount: 12,
      drawer: false,
      messages: [{
        time: "2022-12-20 12:00:00",
        content: '您已成功加入凌峰社！',
      }, {
        time: "2022-12-20 12:00:00",
        content: "你创建的活动已通过审批"
      }, {
        time: "2022-12-20 12:00:00",
        content: "你创建的社团已通过审批"
      },]
    }
  },
  methods: {
    quit() {
      let path = "/";
      this.$router.push({
        path
      });
      localStorage.clear()
    },
    getMessages() {
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_messages",
          Qs.stringify({
            user_id: localStorage.getItem('user_id')
          })
      ).then((res) => {
        if (res.data.code === 0) {
          // console.log(res.data)
          this.messages = res.data.messages
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    getUserInformation() {
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_user_information",
          Qs.stringify({
            'user_id': localStorage.getItem('user_id'),
          })
      ).then((res) => {
        if (res.data.code === 0) {
          // console.log(res.data)
          this.userName = res.data.user.real_name
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    deleteMessage(id) {
      this.$axios.post(
          "http://127.0.0.1:8000/api/delete_message",
          Qs.stringify({
            message_id: id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.messages = this.messages.filter((message) => {
            return message.message_id !== id
          })
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
    deleteAllMessages() {
      this.$axios.post(
          "http://127.0.0.1:8000/api/delete_all_messages",
          Qs.stringify({
            user_id: localStorage.getItem('user_id')
          })
      ).then((res) => {
        if (res.data.code === 0) {
          this.messages = []
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    }
  },
  mounted() {
    this.getMessages()
    this.getUserInformation()
  }
}
</script>

<style scoped>
.flexs {
  height: 75px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
