<template>
  <div>
    <div class="flexs">
      <h1>上午好，陈俊杰</h1>
      <el-badge :value="messageCount" :hidden="hidden">
        <el-button @click="drawer=true" circle icon="el-icon-message-solid"></el-button>
      </el-badge>
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
          <el-button type="success" icon="el-icon-check" circle></el-button>
        </v-list-item>
        <el-button icon="el-icon-finished" style="margin-left: 10px">全部已读</el-button>
        <v-divider></v-divider>
      </v-list>
    </el-drawer>
    <hr/>
  </div>
</template>

<script>
export default {
  name: "MyHeader",
  data() {
    return {
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