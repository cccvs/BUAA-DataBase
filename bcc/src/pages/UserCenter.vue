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
        <MyUserCenterHeader></MyUserCenterHeader>
      </el-main>
      <el-main class="el-main-table">
        <el-descriptions class="margin-top" :column="1" border>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-postcard"></i>
              用户编号
            </template>
            {{ user.user_id }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-user"></i>
              用户昵称
            </template>
            <label v-show="!isEdit">{{ user.user_name }}</label>
            <el-input v-model="user.user_name" v-show="isEdit"></el-input>
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-time"></i>
              注册时间
            </template>
            {{ user.time }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-real_name"></i>
              姓名
            </template>
            <label v-show="!isEdit">{{ user.real_name }}</label>
            <el-input v-model="user.real_name" v-show="isEdit"></el-input>
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-sex"></i>
              性别
            </template>
            <label v-show="!isEdit">{{ user.sex }}</label>
            <template>
              <el-radio v-model="user.sex" v-show="isEdit" label="男">男</el-radio>
              <el-radio v-model="user.sex" v-show="isEdit" label="女">女</el-radio>
            </template>
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-s-check"></i>
              职务
            </template>
            {{ user.level }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-institute"></i>
              学院
            </template>
            <label v-show="!isEdit">{{ user.institute }}</label>
            <el-select v-model="user.institute" filterable v-show="isEdit">
              <el-option
                  v-for="institute in institutes"
                  :key="institute.name"
                  :label="institute.name"
                  :value="institute.name">
              </el-option>
            </el-select>
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-mobile-phone"></i>
              手机号
            </template>
            <label v-show="!isEdit">{{ user.phone }}</label>
            <el-input v-model="user.phone" v-show="isEdit"></el-input>
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-email"></i>
              邮箱
            </template>
            <label v-show="!isEdit">{{ user.email }}</label>
            <el-input v-model="user.email" v-show="isEdit"></el-input>
          </el-descriptions-item>
        </el-descriptions>
        <div class="flexs">
          <el-button type="primary" @click="isEdit = !isEdit">{{ mode }}</el-button>
          <el-button type="primary" v-show="isEdit" @click="isEdit = !isEdit">取消</el-button>
        </div>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import MyHeader from "@/components/MyHeader";
import SideBar from "@/components/SideBar";
import MyUserCenterHeader from "@/components/MyUserCenterHeader";

export default {
  name: "UserCenter",
  components: {MyUserCenterHeader, MyHeader, SideBar},
  data() {
    return {
      user: {
        user_id: "20373021",
        user_name: "cjj826",
        password: "123456",
        avatar: "https://cn.bing.com/images/search?view=detailV2&ccid=wc%2FdCG%2FK&id=2A67B025EDB55DFCC3EACFBF5B0CD513CC71AE39&thid=OIP-C.wc_dCG_KbIKZwMdtD3gL2QHaEt&mediaurl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-58d652598269710fa67ec8d1c88d8f03_r.jpg%3Fsource%3D1940ef5c&exph=1304&expw=2048&q=%e5%9b%be%e7%89%87&simid=607986392466485047&form=IRPRST&ck=7906E4DE8F66609504206A4E0B045F1E&selectedindex=3&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
        time: "2022-11-22",
        real_name: "陈俊杰",
        sex: "男",
        institute: "计算机学院",
        phone: "15978757317",
        email: "2624882033@qq.com",
        level: "学生"
      },
      institutes: [{
        name: "计算机学院"
      }, {
        name: "电子信息学院"
      }, {
        name: "数学学院"
      }],
      isEdit: false
    }
  },
  computed: {
    mode() {
      if (this.isEdit) {
        return "提交"
      } else {
        return "编辑"
      }
    }
  }
}
</script>

<style scoped>
.el-main-table {
  width: 50%;
  align-self: center;
}

.flexs {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

.el-icon {
  color: cornflowerblue;
}

.el-icon-real_name {
  background: url("../assets/real_name.png") no-repeat;
  font-size: 16px;
  background-size: contain;
}

.el-icon-real_name:before {
  content: "ccc";
  font-size: 1px;
  color: rgba(255, 255, 255, 0);
}

.el-icon-sex {
  background: url("../assets/sex.png") no-repeat;
  font-size: 16px;
  background-size: cover;
}

.el-icon-sex:before {
  content: "ccc";
  font-size: 1px;
  color: rgba(255, 255, 255, 0);
}

.el-icon-institute {
  background: url("../assets/institute.png") no-repeat;
  font-size: 16px;
  background-size: cover;
}

.el-icon-institute:before {
  content: "ccc";
  font-size: 1px;
  color: rgba(255, 255, 255, 0);
}

.el-icon-email {
  background: url("../assets/email.png") no-repeat;
  font-size: 16px;
  background-size: cover;
}

.el-icon-email:before {
  content: "ccc";
  font-size: 1px;
  color: rgba(255, 255, 255, 0);
}

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