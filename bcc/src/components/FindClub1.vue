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
      <div class="clubBar" v-for="item in clubList" :key="item.data" @click="gotoClub(item)">
        <span class="clubNameSpan" :title="item.name">{{item.name}} 星级：{{item.level}} 人数：{{item.num}}</span>
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
      level:null,
      club:{
        clubName:"",
        clubId:0,
      },
      clubList: [],
      tmpList: [
        {
          id: 1,
          name: "凌峰社",
          time:'',
          num: 200,
          level: 5
        },
        {
          id: 2,
          name: "篮球裁判社",
          time:'',
          num: 50,
          level: 4
        }
      ]
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
      for(let i = 0; i < this.clubList.length; i++){
        for(let j = 0; j < this.clubList.length-i-1; j++){
          if(this.sortCmp(this.clubList[j],this.clubList[j+1])){
            let tmp = this.clubList[j];
            this.clubList[j] = this.clubList[j+1];
            this.clubList[j+1] = tmp;
          }
        }
      }
    },
    gotoClub(){
    },
    selectLevel(){
      this.clubList = [];
      if (this.level == null) {
        this.clubList = this.tmpList;
      }
      let j = 0;
      for(let i = 0; i < this.tmpList.length; i++){
        if (this.tmpList[i].level === this.level){
          this.clubList[j++] = this.tmpList[i];
        }
      }
    },
    handleSelectLevel(command){
      if (command !== '6') {
        this.level = command - '0'
      } else {
        this.level = null;
      }
      this.selectLevel();
    }
  }
}
</script>

<style scoped>
.tools{
  height: 30px;
  width: 400px;
  display: flex;
}
.search-box{
  width: 300px;
  margin-right: 40px;
}
.dropdownSort-box{
  width: 200px;
}
.dropdownLevel-box{
 width: 90px;
  margin-right: 10px;
}
</style>
