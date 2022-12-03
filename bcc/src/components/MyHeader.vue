<template>
  <div>
    <div class="flexs">
      <h1>上午好，陈俊杰</h1>
      <el-badge :value="messageCount" :hidden="hidden">
        <el-button circle icon="el-icon-message-solid"></el-button>
      </el-badge>
    </div>
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