import VueRouter from "vue-router";
import ClubCenter from "@/pages/ClubCenter";
import ClubManage from "@/pages/ClubManage";
import FindClub from "@/pages/FindClub";
import MainPage from "@/pages/MainPage";
import MyClub from "@/pages/MyClub";
import UserCenter from "@/pages/UserCenter";
import LoginPage from "@/pages/LoginPage";

const router = new VueRouter({
    // mode: 'hash', //hash||history
    routes: [
        {
            name: 'login',
            path: '/',
            component:LoginPage
        },
        {
            name: "clubcenter",
            path: '/clubcenter',
            component: ClubCenter
        },
        {
            name: "clubmanage",
            path: '/clubmanage',
            component: ClubManage
        },
        {
            name: "findclub",
            path: '/findclub',
            component: FindClub
        },
        {
            name: "mainpage",
            path: '/mainpage',
            component: MainPage
        },
        {
            name: "myclub",
            path: '/myclub/:id/:name',
            component: MyClub
        },
        {
            name: "usercenter",
            path: '/usercenter/:id/:name',
            component: UserCenter
        }
    ]
})
export default router
