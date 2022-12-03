<template>
  <div style="height: 800px;">
    <div class="tools">
      <div class="search-box">
        <el-input v-model="searchClubName" placeholder="请输入要搜索的社团名称" clearable size="mini" @input="searchClub"/>
      </div>
      <div class="dropdownLevel-box">
        <el-dropdown placement="bottom" trigger="click" @command="handleSelectLevel">
          <span style="cursor: pointer;color: dodgerblue">星级{{level}}<i class="el-icon-arrow-down el-icon--right"/></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="1">1</el-dropdown-item>
            <el-dropdown-item command="2">2</el-dropdown-item>
            <el-dropdown-item command="3">3</el-dropdown-item>
            <el-dropdown-item command="4">4</el-dropdown-item>
            <el-dropdown-item command="5">5</el-dropdown-item>
            <el-dropdown-item command="6">-</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div class="dropdownType-box">
        <el-dropdown placement="bottom" trigger="click" @command="handleSelectType">
          <span style="cursor: pointer;color: dodgerblue">类型{{type}}<i class="el-icon-arrow-down el-icon--right"/></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="科技">科技</el-dropdown-item>
            <el-dropdown-item command="人文">人文</el-dropdown-item>
            <el-dropdown-item command="实践">实践</el-dropdown-item>
            <el-dropdown-item command="体育">体育</el-dropdown-item>
            <el-dropdown-item command="艺术">艺术</el-dropdown-item>
            <el-dropdown-item command="空">-</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
      <div class="dropdownSort-box">
        <el-dropdown placement="bottom" trigger="click" @command="handleSort">
          <span style="cursor: pointer;color: dodgerblue">{{ sortType }}<i class="el-icon-arrow-down el-icon--right"/></span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="timeDown">按成立时间降序</el-dropdown-item>
            <el-dropdown-item command="timeUp">按成立时间升序</el-dropdown-item>
            <el-dropdown-item command="numDown">按社团人数降序</el-dropdown-item>
            <el-dropdown-item command="numUp">按社团人数升序</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
    <div class="clubs-container" style="margin-top: 10px">
      <div class="clubBar" v-for="item in selectedList" :key="item.data" @click="gotoClub(item)">
        <div class="club_picture"><img src="../assets/logo.png"></div>
        <div class="club_name">{{item.name}}</div>
        <div class="club_info">{{item.type}} {{item.level}}星级 {{item.time}}</div>
        <div class="club_dis">{{item.description}}</div>
      </div>
    </div>
  </div>
</template>

<script>
// import qs from "qs";
export default {
  name: "FindClub-1",
  data(){
    return{
      searchClubName: '',
      sortType:'按成立时间降序',
      level: null,
      isLevel: false,
      type: null,
      isType: false,
      club:{
        clubName:"",
        clubId:0,
      },
      clubList: [],
      levelList: [],
      typeList: [],
      tmpList: [
        {
          id: 1,
          name: "凌峰社",
          time:'2010.11.11',
          type:"体育",
          description:"是一个以攀岩、暑期登山、科考，以及其他户外活动为特色的北航“明星社团”",
          num: 200,
          level: 5
        },
        {
          id: 2,
          name: "篮球裁判社",
          type:"体育",
          time:'2011.11.11',
          num: 50,
          level: 4
        },
        {
          id: 3,
          name: "科协",
          type:"科技",
          time:'2012.11.11',
          num: 150,
          level: 3
        },
        {
          id: 4,
          name: "知行学社",
          type:"人文",
          time:'2013.11.11',
          num: 100,
          level: 2
        }
      ],
      selectedList: this.tmpList
    }
  },
  methods:{
    searchClub(){
      // this.$axios.post(
      //     "http://43.138.22.20:8000/api/user/search_project",
      //     qs.stringify({
      //       content: this.searchClubName,
      //     })
      // ).then((res)=>{
      //   if(res.data.errno===0){
      //     this.clubList = [];
      //     let array = res.data.data;
      //     for(let i in array){
      //       this.clubList.push({
      //         id: array[i].club_id,
      //         name: array[i].name,
      //         time: array[i].time
      //       });
      //     }
      //   } else this.$notify.error(res.data.msg)
      // }).catch((error)=>{
      //   console.log(error)
      // })
    },
    handleSort(command){
      switch (command){
        case 'timeDown':
          this.sortType = '按成立时间降序';
          break;
        case 'timeUp':
          this.sortType = '按成立时间升序';
          break;
        case 'numDown':
          this.sortType = '按社团人数降序';
          break;
        case 'numUp':
          this.sortType = '按社团人数升序';
          break;
      }
      this.sortClubs()
    },
    sortCmp(itemA, itemB){
      switch (this.sortType){
        case '按成立时间降序':
          return itemA.time < itemB.time;
        case '按成立时间升序':
          return itemB.time < itemA.time;
        case '按社团人数降序':
          return itemA.num < itemB.num;
        case '按社团人数升序':
          return itemB.num < itemA.num;
      }
    },
    sortClubs(){
      for(let i = 0; i < this.selectedList.length; i++){
        for(let j = 0; j < this.selectedList.length-i-1; j++){
          if(this.sortCmp(this.selectedList[j],this.selectedList[j+1])){
            let tmp = this.selectedList[j];
            this.selectedList[j] = this.selectedList[j+1];
            this.selectedList[j+1] = tmp;
          }
        }
      }
    },
    gotoClub(){
    },
    selectLevel(){
      this.levelList = [];
      if (this.isType) {
        if (this.level == null) {
          this.levelList = this.typeList;
        } else {
          let j = 0;
          for(let i = 0; i < this.typeList.length; i++){
            if (this.typeList[i].level === this.level){
              this.levelList[j++] = this.typeList[i];
            }
          }
        }
      } else {
        if (this.level == null) {
          this.levelList = this.tmpList;
        } else {
          let j = 0;
          for(let i = 0; i < this.tmpList.length; i++){
            if (this.tmpList[i].level === this.level){
              this.levelList[j++] = this.tmpList[i];
            }
          }
        }
      }
      this.selectedList = this.levelList;
    },
    handleSelectLevel(command){
      if (command !== '6') {
        this.level = command - '0';
        this.isLevel = true;
      } else {
        this.level = null;
        this.isLevel = false;
      }
      this.selectLevel();
      this.sortClubs();
    },
    selectType(){
      this.typeList = [];
      if (this.isLevel) {
        if (this.type == null) {
          this.typeList = this.levelList;
        } else {
          let j = 0;
          for(let i = 0; i < this.levelList.length; i++){
            if (this.levelList[i].type === this.type){
              this.typeList[j++] = this.levelList[i];
            }
          }
        }
      } else {
        if (this.type == null) {
          this.typeList = this.tmpList;
        } else {
          let j = 0;
          for(let i = 0; i < this.tmpList.length; i++){
            if (this.tmpList[i].type === this.type){
              this.typeList[j++] = this.tmpList[i];
            }
          }
        }
      }
      this.selectedList = this.typeList;
    },
    handleSelectType(command){
      if (command !== "空") {
        this.type = command;
        this.isType = true;
      } else {
        this.type = null;
        this.isType = false;
      }
      this.selectType();
      this.sortClubs();
    }
  }
}
</script>

<style scoped>
.tools{
  height: 30px;
  width: 1200px;
  display: flex;
}
.search-box{
  width: 420px;
  margin-right: 20px;
}
.dropdownSort-box{
  width: 250px;
}
.dropdownType-box{
  width: 90px;
  margin-right: 10px;
}
.dropdownLevel-box{
 width: 90px;
  margin-right: 10px;
}
.clubBar{
  width: 650px;
  float: left;
  height: 200px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
  margin-right: 20px;
  margin-bottom: 20px;
}
.club_picture{
  margin-left: 10px;
  width: 200px;
  height: 200px;
  float: left;
  margin-right: 30px;
}
.club_name{
  font-size: 50px;
  width: 410px;
  float: left;
  margin-top: 10px;
  margin-bottom: 10px;
}
.club_info{
  float: left;
  width: 410px;
  margin-bottom: 10px;
}
.club_dis{
  word-wrap: break-word;
  display: inline;
}
</style>
