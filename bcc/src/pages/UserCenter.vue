<template>
  <el-container>
    <div class="side-bar">
      <SideBar></SideBar>
    </div>
    <v-app>
      <MySnackBar></MySnackBar>
    </v-app>
      <el-container>
        <el-header>
          <MyHeader></MyHeader>
        </el-header>
        <el-container>
          <el-main>
            <MyUserCenterHeader
                :real_name="user.real_name"
                :followers="user.followers"
                :following="user.following"
                :avatar="user.avatar"
                :cur-id="this.$router.history.current.params.id"></MyUserCenterHeader>
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
                <el-input size="mini" v-model="user.real_name" v-show="isEdit"></el-input>
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-sex"></i>
                  性别
                </template>
                <label v-show="!isEdit">{{ user.sex }}</label>
                <template>
                  <el-radio size="mini" v-model="user.sex" v-show="isEdit" label="男">男</el-radio>
                  <el-radio size="mini" v-model="user.sex" v-show="isEdit" label="女">女</el-radio>
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
                <el-select size="mini" v-model="user.institute" filterable v-show="isEdit">
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
                <el-input size="mini" v-model="user.phone" v-show="isEdit"></el-input>
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-email"></i>
                  邮箱
                </template>
                <label v-show="!isEdit">{{ user.email }}</label>
                <el-input size="mini" v-model="user.email" v-show="isEdit"></el-input>
              </el-descriptions-item>
            </el-descriptions>
            <div class="flexs" v-show="this.$router.history.current.params.id === id">
              <el-button type="primary" @click="submitChangeInfo">{{ mode }}</el-button>
              <el-button type="primary" v-show="isEdit" @click="isEdit = !isEdit">取消</el-button>
            </div>
          </el-main>
        </el-container>
      </el-container>
  </el-container>
</template>

<script>
import MyHeader from "@/components/MyHeader";
import SideBar from "@/components/SideBar";
import MyUserCenterHeader from "@/components/MyUserCenterHeader";
import MySnackBar from "@/components/MySnackBar";
import Qs from "qs";

export default {
  name: "UserCenter",
  components: {MySnackBar, MyUserCenterHeader, MyHeader, SideBar},
  data() {
    return {
      id:localStorage.getItem('user_id'),
      user: {
        user_id: "20373021",
        password: "123456",
        avatar: "https://cn.bing.com/images/search?view=detailV2&ccid=wc%2FdCG%2FK&id=2A67B025EDB55DFCC3EACFBF5B0CD513CC71AE39&thid=OIP-C.wc_dCG_KbIKZwMdtD3gL2QHaEt&mediaurl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-58d652598269710fa67ec8d1c88d8f03_r.jpg%3Fsource%3D1940ef5c&exph=1304&expw=2048&q=%e5%9b%be%e7%89%87&simid=607986392466485047&form=IRPRST&ck=7906E4DE8F66609504206A4E0B045F1E&selectedindex=3&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
        time: "2022-11-22",
        real_name: "陈俊杰",
        sex: "男",
        institute: "计算机学院",
        phone: "15978757317",
        email: "2624882033@qq.com",
        level: "学生",
        following: 24,
        followers: 22
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
  methods: {
    detailOfUser(id) {
      console.log(id)
      this.user.user_id = id
    },
    submitChangeInfo() {
      if (this.isEdit) {
        this.$axios.post(
            "http://127.0.0.1:8000/api/update_user_information",
            Qs.stringify(
                this.user
            )
        ).then((res) => {
          if (res.data.code === 0) {
            this.$bus.$emit('showSnackBar', "你已成功修改信息！")
          } else this.$notify.error(res.data.message)
        }).catch((error) => {
          console.log(error)
        })
        /*
        DO:提交基本信息（不包括密码和头像【在另一个组件】）修改的接口，
         此时前端容器存储的即为最新的需要保存的信息，将其传回后端保存
         showSnackBar是我实现的一个组件，用以方便地提示用户操作结果，调用示例如下：
         */
      }
      this.isEdit = !this.isEdit
    },
    getUserInformation() {
      this.$axios.post(
          "http://127.0.0.1:8000/api/get_user_information",
          Qs.stringify({
            'user_id': this.$router.history.current.params.id
          })
      ).then((res) => {
        if (res.data.code === 0) {
          // console.log(res.data)
          this.user = res.data.user
        } else this.$notify.error(res.data.message)
      }).catch((error) => {
        console.log(error)
      })
    },
  },
  computed: {
    mode() {
      if (this.isEdit) {
        return "提交"
      } else {
        return "编辑"
      }
    }
  },
  mounted() {
    this.getUserInformation()
    // let id = this.$router.history.current.params.id
    //根据id从后端获得用户数据，这里假设拿到了user_list
    /*
    DO:根据路由参数中的id从后端读取用户的数据，并更新前端容器，
     这里的userList及filter函数是从后端获取的数据，作示例用
     */
    // let userList = [{
    //   user_id: "20373021",
    //   password: "123456",
    //   avatar: "https://cn.bing.com/images/search?view=detailV2&ccid=wc%2FdCG%2FK&id=2A67B025EDB55DFCC3EACFBF5B0CD513CC71AE39&thid=OIP-C.wc_dCG_KbIKZwMdtD3gL2QHaEt&mediaurl=https%3A%2F%2Fpic3.zhimg.com%2Fv2-58d652598269710fa67ec8d1c88d8f03_r.jpg%3Fsource%3D1940ef5c&exph=1304&expw=2048&q=%e5%9b%be%e7%89%87&simid=607986392466485047&form=IRPRST&ck=7906E4DE8F66609504206A4E0B045F1E&selectedindex=3&ajaxhist=0&ajaxserp=0&vt=0&sim=11",
    //   time: "2022-11-22",
    //   real_name: "陈俊杰",
    //   sex: "男",
    //   institute: "计算机学院",
    //   phone: "15978757317",
    //   email: "2624882033@qq.com",
    //   level: "学生",
    //   following: 24,
    //   followers: 22
    // }, {
    //   user_id: "123",
    //   real_name: "蒋博文",
    //   avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
    // }, {
    //   user_id: "124",
    //   real_name: "陈楚岩",
    //   avatar: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg'
    // }];
    // this.user = (userList.filter((user) => {
    //   return user.user_id === id;
    // })).pop();
  },
  beforeRouteUpdate(to,from,next){
    this.$axios.post(
        "http://127.0.0.1:8000/api/get_user_information",
        Qs.stringify({
          'user_id': to.params.id
        })
    ).then((res) => {
      if (res.data.code === 0) {
        console.log(res.data)
        this.user = res.data.user
      } else this.$notify.error(res.data.message)
    }).catch((error) => {
      console.log(error)
    })
    next()
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
