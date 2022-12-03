<template>
  <v-container fluid>
    <v-row>
      <v-icon color="blue" style="margin-left: 10px;margin-top: 10px">mdi-clipboard-text-multiple-outline</v-icon>
      <h1 style="margin-left: 10px;margin-top: 10px">发布新的公告！</h1>
    </v-row>
    <v-row>
      <v-col cols="5">
        <v-text-field label="标题" hide-details="auto"
                      style="padding-bottom: 20px"
                      v-model="notice.title">
        </v-text-field>
      </v-col>
      <v-col cols="5">
        <v-checkbox label="置顶" v-model="notice.top">
        </v-checkbox>
      </v-col>
    </v-row>
    <v-textarea
        clearable
        clear-icon="mdi-close"
        label="正文内容"
        :value="notice.content"
    ></v-textarea>
  </v-container>
</template>

<script>
export default {
  name: "PublishNotice",
  data() {
    return {
      notice: {
        id: 1,
        title: "",
        content: "",
        user_id: 20373021,
        top: true
      }
    }
  }
}
</script>

<style scoped>

</style>