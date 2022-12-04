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
              <MemberList :members="members" text="查看社团内的成员" follow="true"></MemberList>
              <v-btn @click="showCharts">展示</v-btn>
              <div v-show="charts" style="width:500px;height:500px" id="mychart"></div>
            </v-tab-item>
            <v-tab-item>
              <ActivityList :activities="activities" text="查看社团的活动"></ActivityList>
            </v-tab-item>
            <v-tab-item>
              <NoticeList :notices="notices"></NoticeList>
            </v-tab-item>
            <v-tab-item>

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

export default {
  name: "MyClub",
  components: {NoticeList, ActivityList, MemberList, ClubList, MyHeader, SideBar},
  data() {
    /*
    TODO: 前端容器，curClub是当前的社团【挂载和路由更新时获取】，注意是数组格式，但只含一个元素
     members是当前社团的所有成员，activities是当前社团的所有活动，notices是当前社团的所有公告
     */
    return {
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
        id: 1,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24,
        show: false,
      }, {
        id: 2,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24,
        show: false,
      }, {
        id: 3,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24,
        show: false,
      }, {
        id: 4,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24,
        show: false,
      }, {
        id: 5,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24,
        show: false,
      }, {
        id: 6,
        title: "hhhh",
        content: "xxx",
        user_id: "20373021",
        apply_time: "2022-10-01~2022-12-18",
        begin_time: "2022-10-01~2022-12-18",
        limit: 24,
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
      charts: false,
      firstClick: true
    }
  },
  methods: {
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
              { value: 1048, name: '男' },
              { value: 735, name: '女' },
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
    }
  },
  mounted() {
    /*
    FIXME:注意JS的数据格式，===如果两边类型不一致不会相等
     */
    let id = Number(this.$router.history.current.params.id);
    /*
    TODO: myClubList是假设从后端获取的当前用户所在社团的列表
     */
    let myClubList = [
      {
        id: 1,
        name: "凌峰社",
        time: '2010.11.11',
        type: "体育",
        description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
        num: 200,
        level: 5
      },
      {
        id: 2,
        name: "篮球裁判社",
        type: "体育",
        time: '2011.11.11',
        num: 50,
        level: 4
      },
      {
        id: 3,
        name: "科协",
        type: "科技",
        time: '2012.11.11',
        num: 150,
        level: 3
      },
      {
        id: 4,
        name: "知行学社",
        type: "人文",
        time: '2013.11.11',
        num: 100,
        level: 2
      }
    ];
    this.curClub = myClubList.filter((club) => {
      return club.id === id
    })
  },
  beforeRouteUpdate(to, from, next) {
    if (to.params && from.params && to.params.id !== from.params.id) {
      console.log("update");
      let id = Number(to.params.id);
      let myClubList = [
        {
          id: 1,
          name: "凌峰社",
          time: '2010.11.11',
          type: "体育",
          description: "是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
          num: 200,
          level: 5
        },
        {
          id: 2,
          name: "篮球裁判社",
          type: "体育",
          time: '2011.11.11',
          num: 50,
          level: 4
        },
        {
          id: 3,
          name: "科协",
          type: "科技",
          time: '2012.11.11',
          num: 150,
          level: 3
        },
        {
          id: 4,
          name: "知行学社",
          type: "人文",
          time: '2013.11.11',
          num: 100,
          level: 2
        }
      ];
      this.curClub = myClubList.filter((club) => {
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