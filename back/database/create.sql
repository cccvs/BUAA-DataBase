drop schema `club_system`;
create schema `club_system`;
use `club_system`;

# entity
create table `user`
(
    `user_id`   varchar(31)  not null,
    `password`  varchar(255) not null,
    `avatar`    varchar(255),
    `time`      timestamp    not null,
    `real_name` varchar(31),
    `sex`       varchar(1),
    `institute` varchar(31),
    `phone`     varchar(31),
    `email`     varchar(31)  not null,
    `level`     smallint,
    `following` int          not null,
    `followers` int          not null,
    primary key (`user_id`),
    check (`sex` in ('M', 'F')),
    check ( 0 <= `level` and `level` <= 3 ) # 不同学生/管理员权限
);

create table `club`
(
    `club_id`   binary(16)  not null,
    `club_name` varchar(31) not null,
    `type`      smallint    not null,
    `star`      smallint,
    `score`     float,
    `time`      timestamp   not null,
    `intro`     varchar(1022),
    `master_id` varchar(31),
    primary key (`club_id`),
    foreign key (`master_id`) references `user` (`user_id`),
    check ( 0 <= `type` and `type` <= 5 ),
    check ( `star` is null or (1 <= `star` and `star` <= 5) ),
    check ( 1.0 <= `score` and `score` <= 5.0 )
);

create table `notice`
(
    `notice_id` binary(16) not null,
    `title`     varchar(31),
    `content`   varchar(1022),
    `user_id`   varchar(31),
    `top`       smallint,
    primary key (`notice_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    check ( `top` = 0 or `top` = 1 )
);

create table `event`
(
    `event_id`     binary(16) not null,
    `club_id`      binary(16) not null,
    `user_id`      varchar(31),
    `time`         timestamp  not null,
    `apply_time`   timestamp,
    `expired_time` timestamp,
    `begin_time`   timestamp,
    `end_time`     timestamp,
    `limit`        int,
    primary key (`event_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    foreign key (`user_id`) references `user` (`user_id`)
);

create table `post`
(
    `post_id` binary(16)    not null,
    `club_id` binary(16),
    `time`    timestamp     not null,
    `title`   varchar(31)   not null,
    `content` varchar(1022) not null,
    `like`    int           not null,
    `dislike` int           not null,
    primary key (`post_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0)
);

create table `reply`
(
    `reply_id` binary(16)    not null,
    `post_id`  binary(16)    not null,
    `time`     varchar(31)   not null,
    `content`  varchar(1022) not null,
    `like`     int           not null,
    `dislike`  int           not null,
    primary key (`reply_id`),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0)
);

create table `application`
(
    `form_id`      binary(16)  not null,
    `applicant_id` varchar(31) not null,
    `verifier_id`  varchar(31) not null,
    `status`       smallint    not null,
    `club_name`    varchar(31) not null,
    `type`         smallint    not null,
    `apply_time`   timestamp   not null,
    `verify_time`  timestamp,
    `content`      varchar(1022),
    primary key (`form_id`),
    foreign key (`applicant_id`) references `user` (`user_id`),
    foreign key (`verifier_id`) references `user` (`user_id`),
    check ( 0 <= `status` and `status` <= 2),
    check ( 0 <= `type` and `type` <= 5)
);

# relation
create table `user_club`
(
    `user_id`  varchar(31) not null,
    `club_id`  binary(16)  not null,
    `identity` smallint    not null,
    `label`    varchar(31),
    primary key (`user_id`, `club_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check (`identity` in (0, 1, 2))
);

create table `user_event`
(
    `user_id`  varchar(31) not null,
    `event_id` binary(16)  not null,
    `identity` smallint    not null,
    primary key (`user_id`, `event_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`event_id`) references `event` (`event_id`),
    check ( `identity` in (0, 1, 2))
);

create table `score`
(
    `user_id` varchar(31) not null,
    `club_id` binary(16)  not null,
    `score`   float       not null,
    primary key (`user_id`, `club_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`club_id`) references `club` (`club_id`),
    check ( `score` in (1.0, 2.0, 3.0, 4.0, 5.0) )
);

create table `user_post`
(
    `user_id` varchar(31) not null,
    `post_id` binary(16)  not null,
    `action`  smallint    not null,
    primary key (`user_id`, `post_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`post_id`) references `post` (`post_id`),
    check ( `action` in (0, 1) )
);

create table `user_reply`
(
    `user_id`  varchar(31) not null,
    `reply_id` binary(16)  not null,
    `action`   smallint    not null,
    primary key (`user_id`, `reply_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`reply_id`) references `reply` (`reply_id`),
    check ( `action` in (0, 1) )
);

create table `follow`
(
    `follower_id` varchar(31) not null,
    `friend_id`   varchar(31) not null,
    primary key (`follower_id`, `friend_id`),
    foreign key (`follower_id`) references `user` (`user_id`),
    foreign key (`friend_id`) references `user` (`user_id`)
)