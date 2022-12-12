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
            <v-tab>概览</v-tab>
            <v-tab>成员</v-tab>
            <v-tab>活动</v-tab>
            <v-tab>公告</v-tab>
            <v-tab>论坛</v-tab>
            <v-tab-item>
              <ClubList :clubs="curClub"></ClubList>
            </v-tab-item>
            <v-tab-item>
              <v-row style="margin-left: 10px;margin-top: 10px">
                <v-icon color="blue">mdi-account-group</v-icon>
                <h1 style="margin-left: 10px;margin-top: 5px">查看社团内的成员</h1>
              </v-row>
              <MemberList :members="members" follow="true" text="您可以关注同社团的小伙伴"></MemberList>
              <v-btn @click="showCharts">展示</v-btn>
              <div v-show="charts" style="width:500px;height:500px" id="mychart"></div>
            </v-tab-item>
            <v-tab-item>
              <ActivityList :activities="activities" text="查看社团的活动"></ActivityList>
            </v-tab-item>
            <v-tab-item>
              <v-row style="margin-left: 10px;margin-top: 10px">
                <v-icon color="blue">mdi-clipboard-check-multiple-outline</v-icon>
                <h1 style="margin-left: 10px;margin-top: 5px">查看社团公告</h1>
              </v-row>
              <NoticeList :notices="notices"></NoticeList>
            </v-tab-item>
            <v-tab-item>
              <v-row style="margin-left: 10px;margin-top: 10px">
                <v-icon color="blue">mdi-chat-plus</v-icon>
                <h1 style="margin-left: 10px;margin-top: 10px">和社团的小伙伴一起尽情讨论吧！</h1>
              </v-row>
              <PostList :posts="posts"></PostList>
            </v-tab-item>
          </v-tabs>
        </v-app>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import MyHeader from "@/components/MyHeader";
import SideBar from "@/components/SideBar";
import ClubList from "@/components/ClubList";
import MemberList from "@/components/MemberList";
import ActivityList from "@/components/ActivityList";
import NoticeList from "@/components/NoticeList";
import * as echarts from "echarts";
import PostList from "@/components/PostList";
import Qs from "qs";

export default {
  name: "MyClub",
  components: {PostList, NoticeList, ActivityList, MemberList, ClubList, MyHeader, SideBar},
  data() {
    /*
    TODO: 前端容器，curClub是当前的社团【挂载和路由更新时获取】，注意是数组格式，但只含一个元素
     members是当前社团的所有成员，activities是当前社团的所有活动，notices是当前社团的所有公告
     */
    return {
      myClubList:[],
      curClub: [{
        id: 1,
        name: "凌峰社",
        time: '2010.11.11',
        type: "体育",
        description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
        num: 200,
        level: 5
      }],
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
      }],
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
        time: "2022-09-25 10:01:06",
        avatar: "https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg",
        real_name: "陈俊杰",
        apply_time: "2022-10-01 12:00:00~2022-12-18 13:01:20",
        begin_time: "2022-12-10 12:00:00~2022-12-18 13:01:20",
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
      }],
      notices: [
        {
          notice_id: 1,
          title: "社长换届1",
          content: "卸职：张三，任命：李四",
          user_id: "20373021",
        }, {
          notice_id: 2,
          title: "社长换届2",
          content: "卸职：张三，任命：李四",
          user_id: "20373021",
        }, {
          notice_id: 3,
          title: "社长换届3",
          content: "卸职：张三，任命：李四",
          user_id: "20373021",
        }, {
          notice_id: 4,
          title: "社长换届4",
          content: `卸职：
经理事会商定，同意原北京航空航天大学凌峰社社长郭伟恒辞去社长一职，感谢他一年来为凌峰社所做的贡献，并祝愿他在以后的学习工作中发扬凌峰精神，向上攀登，仰望最辽阔的天空。
任命：
经理事会商定，任命李书实担任凌峰社社长一职，希望他在新的一年中带领凌峰社向高攀怀抱希望，让凌峰的旗帜在顶峰飘扬！`,
          user_id: "20373021",
        }
      ],
      posts: [{
        post_id: 1,
        title: "自动化测试",
        like: 22,
        dislike: 0,
        content: "省流不看版 ..."
      }, {
        post_id: 2,
        title: "自动化测试",
        like: 22,
        dislike: 0,
        content: "省流不看版 ..."
      }],
      charts: false,
      firstClick: true
    }
  },
  methods: {
    getClubList(){
      return new Promise((resolve)=>{
        this.$axios.post(
            "http://127.0.0.1:8000/api/get_club_list",
            Qs.stringify({
              jwt: {'code':localStorage.getItem('code'),'user_id':localStorage.getItem('user_id'),'time':localStorage.getItem('time')}
            })
        ).then((res)=>{
          if(res.data.code===0){
            this.myClubList = res.data.club_list;
            let id = Number(this.$router.history.current.params.id);
            this.curClub = this.myClubList.filter((club) => {
              return club.club_id === id
            })
            resolve();
          } else this.$notify.error(res.data.message)
        }).catch((error)=>{
          console.log(error)
        })
      })
    },
    getMembers(){
      console.log(this.curClub[0].club_id)
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_club_members",
          Qs.stringify({
            club_id: this.curClub[0].club_id
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.members = res.data.member_list;
          console.log(this.members)
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    getActivities(){
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_club_events",
          Qs.stringify({
            club_id: this.curClub[0].club_id
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.activities = res.data.event_list;
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    getNotices(){
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_club_events",
          Qs.stringify({
            club_id: this.curClub[0].club_id
          })
      ).then((res)=>{
        if(res.data.code===0){
          this.notices = res.data.notice_list;
        } else this.$notify.error(res.data.message)
      }).catch((error)=>{
        console.log(error)
      })
    },
    showCharts() {
      if (this.firstClick) {
        this.initEcharts()
        this.firstClick = false
      }
      this.charts = !this.charts
    },
    initEcharts() {
      const option = {
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Access From',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: 1048, name: '男'},
              {value: 735, name: '女'},
            ]
          }
        ]
      };
      const myChart = echarts.init(document.getElementById("mychart"));// 图标初始化
      myChart.setOption(option);// 渲染页面
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        myChart.resize();
      });
    },
    init() {
      Promise.all([this.getClubList()])
      .then(()=>{
        this.getMembers();
        this.getActivities();
        this.getNotices();
      })
    }
  },
  mounted() {
    this.init();
    // let myClubList = [
    //   {
    //     id: 1,
    //     name: "凌峰社",
    //     time: '2010.11.11',
    //     type: "体育",
    //     description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
    //     num: 200,
    //     level: 5
    //   },
    //   {
    //     id: 2,
    //     name: "篮球裁判社",
    //     type: "体育",
    //     time: '2011.11.11',
    //     num: 50,
    //     level: 4
    //   },
    //   {
    //     id: 3,
    //     name: "科协",
    //     type: "科技",
    //     time: '2012.11.11',
    //     num: 150,
    //     level: 3
    //   },
    //   {
    //     id: 4,
    //     name: "知行学社",
    //     type: "人文",
    //     time: '2013.11.11',
    //     num: 100,
    //     level: 2
    //   }
    // ];
  },
  beforeRouteUpdate(to, from, next) {
    if (to.params && from.params && to.params.id !== from.params.id) {
      console.log("update");
      let id = Number(to.params.id);
      // let myClubList = [
      //   {
      //     id: 1,
      //     name: "凌峰社",
      //     time: '2010.11.11',
      //     type: "体育",
      //     description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
      //     num: 200,
      //     level: 5
      //   },
      //   {
      //     id: 2,
      //     name: "篮球裁判社",
      //     type: "体育",
      //     time: '2011.11.11',
      //     num: 50,
      //     level: 4
      //   },
      //   {
      //     id: 3,
      //     name: "科协",
      //     type: "科技",
      //     time: '2012.11.11',
      //     num: 150,
      //     level: 3
      //   },
      //   {
      //     id: 4,
      //     name: "知行学社",
      //     type: "人文",
      //     time: '2013.11.11',
      //     num: 100,
      //     level: 2
      //   }
      // ];
      this.curClub = this.myClubList.filter((club) => {
        return club.id === id
      })
      next();
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
