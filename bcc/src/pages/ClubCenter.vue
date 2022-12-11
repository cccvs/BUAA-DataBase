<template>
  <el-container>
    <div class="side-bar">
      <SideBar></SideBar>
    </div>
    <el-container>
      <el-header>
        <MyHeader></MyHeader>
      </el-header>
      <el-main>
        <v-app>
          <v-tabs
              background-color="white"
              color="deep-purple accent-4"
              left
          >
            <v-tab>社团申请审批</v-tab>
            <v-tab>社团活动审批</v-tab>
            <v-tab>社团星级评定</v-tab>
            <v-tab-item>
              <ClubList :clubs="clubList" check-info="true"></ClubList>
            </v-tab-item>
            <v-tab-item>
              <ActivityList :activities="activities" audit="true" text="审批社团发起的活动"></ActivityList>
            </v-tab-item>
            <v-tab-item>
              <ClubList :clubs="clubList" rate-club="true"></ClubList>
            </v-tab-item>
          </v-tabs>
        </v-app>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import SideBar from "@/components/SideBar";
import MyHeader from "@/components/MyHeader";
import ClubList from "@/components/ClubList";
import ActivityList from "@/components/ActivityList";

export default {
  name: "ClubCenter",
  components: {ClubList, MyHeader, SideBar, ActivityList},
  data() {
    return {
      clubList: [
        {
          id: 1,
          name: "凌峰社",
          time: '2010.11.11',
          type: "体育",
          description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
          num: 200,
          level: 5,
          isPass: false
        },
        {
          id: 2,
          name: "篮球裁判社",
          type: "体育",
          time: '2011.11.11',
          num: 50,
          level: 4,
          isPass: false
        },
        {
          id: 3,
          name: "科协",
          type: "科技",
          time: '2012.11.11',
          num: 150,
          level: 3,
          isPass: false
        },
        {
          id: 4,
          name: "知行学社",
          type: "人文",
          time: '2013.11.11',
          num: 100,
          level: 2,
          isPass: false
        },
        {
          id: 5,
          name: "马克思主义学社",
          type: "人文",
          time: '2013.11.11',
          num: 100,
          level: 2,
          isPass: false
        }
      ],
      activities: [{
        event_id: 1,
        club_name: "凌峰社",
        club_face: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        title: "黄花梁——龙门涧探险",
        intro:
            `黄花梁位于北京市门头沟区清水镇梨园岭村北，呈南—北走向，全长约5千米，南接梨园岭，北达东灵山前往椴木沟的垭口，由数座缓坡山峰组成，最高海拔1850米左右。山梁之上，亚高山草甸漫山遍野，郁郁葱葱。每到初夏，忘忧草盛开，金黄色的花朵装点着翠绿的青草，铺满5公里的山梁，故得名“黄花梁”。

龙门涧分为东西两涧，各绵延十余里。由于这里聚集了我国几类著名风景区的景色，诸如“三峡之气势”、“桂林之秀美”、“匡庐之飞瀑”、“黄山之叠泉”，都可以在这里看到缩影，因此，龙门涧得到了许多如“燕京小三峡”、“京西小桂林”、“京西小黄山”等美誉。

路线亮点：可以看到梨园岭古村落，梨园岭长城遗址，保存比较完整的无编号敌楼，登顶有大片开阔的亚高山草甸观景。

车程三小时左右可从学院路到达龙门涧

路线为：燕家台村——龙门涧——黄花梁——梨园岭

全长18km
累计爬升1500m
最高海拔（黄花梁山顶）1850m

总结
风景：★★★★☆（在我走过的路线里仅次于京门铁路）

难度：★★★★☆（排除掉下雨路滑的因素，最多三星，难度主要在第一天）

强度：★★★☆☆（18km能走一天线，爬升有点急，对大多数人来说强度大了，对山队来说还不太够）

体验：★★★★☆（遇上雨天和寒潮还算不错，高海拔扎营还是一如既往的痛苦，但是风景好，路线也挺有趣，人更有趣）

没想到第一次领队就是探线，出发前看着路线极其自信，但是实际上对难度的估计有很大的偏差，这根本不是一条休闲线（还好没让萌叔带妹子来）！好在所有人都比我更有经验，更加强大，以及一学期以来磨合出的默契，所以没有出什么大的问题，让我能顺利的把这条线带下来，也感谢大家一路对菜鸡领队的帮助和包容。原以为能给社团探一条新的休闲线，现在看来只能留给明年的山队走了。山顶的海拔较高，可以体验被大风吹的折磨，强度适中，也有一定难度，适合山队前期出两天线。

最后感谢耀姐、阿传、李昀、冠阳学长、郭哥、文慧、语诚、帅帅对本次探线的大力支持`,
        time: "2022-09-25",
        real_name: "陈俊杰",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-12-10~2022-12-18",
        member_count: 12,
        limit: 24,
        score: 1,
        avg_score: 2,
        like: 12,
        dislike: 10,
        show: false,
      }, {
        event_id: 2,
        club_name: "凌峰社",
        club_face: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        title: "hhhh",
        intro: "xxx",
        time: "2022-09-25",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        real_name: "陈俊杰",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-12-10~2022-12-18",
        member_count: 12,
        limit: 24,
        score: 1,
        like: 12,
        dislike: 10,
        show: false,
      }, {
        event_id: 3,
        club_name: "凌峰社",
        club_face: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        title: "hhhh",
        intro: "xxx",
        time: "2022-09-25",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        real_name: "陈俊杰",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-12-10~2022-12-18",
        member_count: 12,
        limit: 24,
        score: 1,
        like: 12,
        dislike: 10,
        show: false,
      }, {
        event_id: 4,
        club_name: "凌峰社",
        club_face: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        title: "hhhh",
        intro: "xxx",
        time: "2022-09-25",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        real_name: "陈俊杰",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-12-10~2022-12-18",
        member_count: 12,
        limit: 24,
        score: 1,
        like: 12,
        dislike: 10,
        show: false,
      }, {
        event_id: 5,
        club_name: "凌峰社",
        club_face: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        title: "hhhh",
        intro: "xxx",
        time: "2022-09-25",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        real_name: "陈俊杰",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-12-10~2022-12-18",
        member_count: 12,
        limit: 24,
        score: 1,
        like: 12,
        dislike: 10,
        show: false,
      }]
    }
  }
}
</script>

<style scoped>
.side-bar {
  width: 65px;
  transition: width 0.5s;
  -moz-transition: width 0.5s;
  -webkit-transition: width 0.5s;
  -o-transition: width 0.5s;
}

.side-bar:hover {
  width: 150px;
}
</style>