drop schema `club_system`;
create schema `club_system`;
use `club_system`;

create table `user` (
    `user_id` binary(16) not null ,
    `user_name` varchar(31) not null ,
    `password` varchar(127) not null ,
    `avatar` varchar(255),
    `time` timestamp not null ,
    `real_name` varchar(31),
    `sex` varchar(2),
    `institute` varchar(31),
    `phone` varchar(31),
    `email` varchar(31) not null ,
    primary key (`user_id`),
    check (`sex` in ('M','F'))
);

create table `admin` (
    `admin_id` binary(16) not null,
    `admin_name` varchar(31) not null ,
    `password` varchar(127) not null ,
    `avatar` varchar(255),
    `time` timestamp not null ,
    `real_name` varchar(31),
    `sex` varchar(2),
    `institute` varchar(31),
    `phone` varchar(31),
    `email` varchar(31),
    `level` smallint,
    primary key (`admin_id`),
    check (`sex` in ('M','F')),
    check ( 0 <= `level` and `level` <= 3 ) # 不同管理员权限
);

create table `club` (
    `club_id` binary(16) not null,
    `club_name` varchar(31) not null ,
    `type` smallint not null,
    `star` smallint,
    `time` timestamp not null,
    `intro` varchar(1023),
    `master_id` binary(16),
    primary key (`club_id`),
    foreign key (`master_id`) references user(`user_id`),
    check ( 1 <= `type` and `type` <= 5 ),
    check ( `star` is null or (1 <= `star` and `star` <= 5) )
);

create table `notice`(
    `notice_id` binary(16) not null,
    `title` varchar(31),
    `content` varchar(1023),
    `user_id` binary(16),
    `top` smallint,
    primary key (`notice_id`),
    foreign key (`user_id`) references user(`user_id`),
    check ( `top` = 0 or `top` = 1 )
);

