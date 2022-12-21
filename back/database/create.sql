drop schema if exists `club_system`;
create schema `club_system` default charset = utf8;
use `club_system`;

# entity
drop table if exists `user`;
create table `user`
(
    `user_id`   varchar(31)  not null,
    `password`  varchar(255) not null,
    `avatar`    varchar(255),
    `time`      varchar(31)  not null,
    `real_name` varchar(31),
    `sex`       varchar(31),
    `institute` varchar(31),
    `phone`     varchar(31),
    `email`     varchar(31)  not null,
    `level`     smallint,
    `following` int          not null,
    `followers` int          not null,
    primary key (`user_id`),
    check ( 0 <= `level` and `level` <= 3 ) # 不同学生/管理员权限
);


drop table if exists `club`;
create table `club`
(
    `club_id`      int auto_increment not null,
    `name`         varchar(31)        not null,
    `type`         smallint           not null,
    `star`         smallint,
    `member_count` int                not null,
    `score`        float,
    `time`         varchar(31)        not null,
    `intro`        varchar(1022),
    `master_id`    varchar(31),
    `cover`        varchar(255),
    primary key (`club_id`),
    foreign key (`master_id`) references `user` (`user_id`),
    check ( 0 <= `type` and `type` <= 5 ),
    check ( `star` is null or (1 <= `star` and `star` <= 5) ),
    check ( `member_count` >= 0 ),
    check ( 1.0 <= `score` and `score` <= 5.0 )
);

drop table if exists `notice`;
create table `notice`
(
    `notice_id` int auto_increment not null,
    `title`     varchar(31),
    `content`   varchar(1022),
    `user_id`   varchar(31),
    `club_id`   int,
    `top`       smallint,
    primary key (`notice_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check ( `top` = 0 or `top` = 1 )
);

drop table if exists `event`;
create table `event`
(
    `event_id`     int auto_increment not null,
    `club_id`      int                not null,
    `user_id`      varchar(31),
    `title`        varchar(31),
    `cover`        varchar(255),
    `content`      varchar(255),
    `time`         varchar(31)        not null,
    `apply_time`   varchar(31),
    `expired_time` varchar(31),
    `begin_time`   varchar(31),
    `end_time`     varchar(31),
    `member_count` int,
    `member_limit` int,
    `status`       smallint,
    primary key (`event_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    check ( `member_count` >= 0),
    check ( `member_limit` >= 0 ),
    check ( `status` in (0, 1, 2) )
);

drop table if exists `post`;
create table `post`
(
    `post_id` int auto_increment not null,
    `club_id` int,
    `time`    varchar(31)        not null,
    `title`   varchar(31)        not null,
    `content` varchar(1022)      not null,
    `like`    int                not null,
    `dislike` int                not null,
    primary key (`post_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0)
);

drop table if exists `reply`;
create table `reply`
(
    `reply_id` int auto_increment not null,
    `post_id`  int                not null,
    `time`     varchar(31)        not null,
    `content`  varchar(1022)      not null,
    `like`     int                not null,
    `dislike`  int                not null,
    primary key (`reply_id`),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0)
);

drop table if exists `comment`;
create table `comment`
(
    `comment_id` int auto_increment not null,
    `user_id`    varchar(31)        not null,
    `event_id`   int                not null,
    `time`       varchar(31)        not null,
    `content`    varchar(1022),
    `score`      float              not null,
    `like`       int                not null,
    `dislike`    int                not null,
    primary key (`comment_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`event_id`) references `event` (`event_id`),
    check ( `score` in (1.0, 2.0, 3.0, 4.0, 5.0) ),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0)
);

drop table if exists `establishing_club`;
create table `establishing_club`
(
    `form_id`      int auto_increment not null,
    `applicant_id` varchar(31)        not null,
    `verifier_id`  varchar(31),
    `status`       smallint           not null,
    `club_name`    varchar(31)        not null,
    `type`         smallint           not null,
    `apply_time`   varchar(31)        not null,
    `verify_time`  varchar(31),
    `content`      varchar(1022),
    primary key (`form_id`),
    foreign key (`applicant_id`) references `user` (`user_id`),
    foreign key (`verifier_id`) references `user` (`user_id`),
    check ( 0 <= `status` and `status` <= 2),
    check ( 0 <= `type` and `type` <= 5)
);

drop table if exists `joining_club`;
create table `joining_club`
(
    `form_id`      int auto_increment not null,
    `applicant_id` varchar(31),
    `club_id`      int,
    `status`       smallint           not null,
    `time`         varchar(31)        not null,
    primary key (`form_id`),
    foreign key (`applicant_id`) references `user` (`user_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check ( 0 <= `status` and `status` <= 2)
);

drop table if exists `message`;
create table `message`
(
    `message_id` int auto_increment not null,
    `club_id`    int,
    `time`       varchar(31)        not null,
    `content`    varchar(255)       not null,
    foreign key (`club_id`) references club (`club_id`)
);

# relation
drop table if exists `user_club`;
create table `user_club`
(
    `user_id`  varchar(31) not null,
    `club_id`  int         not null,
    `identity` smallint    not null,
    `label`    varchar(31),
    primary key (`user_id`, `club_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check (`identity` in (0, 1, 2))
);

drop table if exists `user_event`;
create table `user_event`
(
    `user_id`  varchar(31) not null,
    `event_id` int         not null,
    `identity` smallint    not null,
    primary key (`user_id`, `event_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`event_id`) references `event` (`event_id`),
    check ( `identity` in (0, 1, 2))
);

drop table if exists `score`;
create table `score`
(
    `user_id` varchar(31) not null,
    `club_id` int         not null,
    `score`   float       not null,
    primary key (`user_id`, `club_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check ( `score` in (1.0, 2.0, 3.0, 4.0, 5.0) )
);

drop table if exists `user_post`;
create table `user_post`
(
    `user_id` varchar(31) not null,
    `post_id` int         not null,
    `action`  smallint    not null,
    primary key (`user_id`, `post_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`post_id`) references `post` (`post_id`),
    check ( `action` in (0, 1) )
);

drop table if exists `user_reply`;
create table `user_reply`
(
    `user_id`  varchar(31) not null,
    `reply_id` int         not null,
    `action`   smallint    not null,
    primary key (`user_id`, `reply_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`reply_id`) references `reply` (`reply_id`),
    check ( `action` in (0, 1) )
);

drop table if exists `follow`;
create table `follow`
(
    `follower_id` varchar(31) not null,
    `friend_id`   varchar(31) not null,
    primary key (`follower_id`, `friend_id`),
    foreign key (`follower_id`) references `user` (`user_id`),
    foreign key (`friend_id`) references `user` (`user_id`)
);

# alloc id
drop table if exists `id_allocator`;
create table `id_allocator`
(
    `global_id` int not null,
    primary key (`global_id`)
)

