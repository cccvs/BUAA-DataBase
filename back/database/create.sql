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
    `club_id`       int auto_increment not null,
    `name`          varchar(31)        not null,
    `type`          smallint           not null,
    `star`          smallint,
    `member_count`  int                not null,
    `time`          varchar(31)        not null,
    `intro`         varchar(16382),
    `master_id`     varchar(31),
    `cover`         varchar(255),
    `status`        smallint           not null,
    `welcome`       varchar(255),
    `welcome_image` varchar(255),
    primary key (`club_id`),
    foreign key (`master_id`) references `user` (`user_id`),
    check ( 0 <= `type` and `type` <= 5 ),
    check ( `star` is null or (0 <= `star` and `star` <= 5) ),
    check ( `member_count` >= 0 ),
    check ( `status` in (0, 1, 2) )
);

drop table if exists `notice`;
create table `notice`
(
    `notice_id` int auto_increment not null,
    `title`     varchar(31),
    `content`   varchar(16382),
    `user_id`   varchar(31),
    `club_id`   int,
    `top`       smallint,
    primary key (`notice_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`club_id`) references `club` (`club_id`) on delete cascade,
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
    `content`      varchar(16382),
    `time`         varchar(31)        not null,
    `apply_time`   varchar(31),
    `expired_time` varchar(31),
    `begin_time`   varchar(31),
    `end_time`     varchar(31),
    `member_count` int,
    `member_limit` int,
    `status`       smallint,
    `like`         int,
    `dislike`      int,
    primary key (`event_id`),
    foreign key (`club_id`) references `club` (`club_id`) on delete cascade,
    foreign key (`user_id`) references `user` (`user_id`),
    check ( `member_count` >= 0),
    check ( `member_limit` >= 0 ),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0 ),
    check ( `status` in (0, 1, 2) )
);

drop table if exists `post`;
create table `post`
(
    `post_id` int auto_increment not null,
    `club_id` int,
    `user_id` varchar(31)        not null,
    `time`    varchar(31)        not null,
    `title`   varchar(31)        not null,
    `content` varchar(16382)     not null,
    `like`    int                not null,
    `dislike` int                not null,
    primary key (`post_id`),
    foreign key (`club_id`) references `club` (`club_id`) on delete cascade,
    foreign key (`user_id`) references `user` (`user_id`),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0)
);

drop table if exists `reply`;
create table `reply`
(
    `reply_id` int auto_increment not null,
    `post_id`  int                not null,
    `user_id`  varchar(31)        not null,
    `time`     varchar(31)        not null,
    `content`  varchar(16382)     not null,
    `like`     int                not null,
    `dislike`  int                not null,
    primary key (`reply_id`),
    foreign key (`post_id`) references post (`post_id`) on delete cascade,
    foreign key (`user_id`) references user (`user_id`),
    check ( `like` >= 0 ),
    check ( `dislike` >= 0)
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
    foreign key (`club_id`) references `club` (`club_id`) on delete cascade,
    check ( 0 <= `status` and `status` <= 2)
);

drop table if exists `message`;
create table `message`
(
    `message_id`  int auto_increment not null,
    `receiver_id` varchar(31),
    `time`        varchar(31)        not null,
    `content`     varchar(16382)     not null,
    `is_log`      smallint           not null,
    primary key (`message_id`),
    foreign key (`receiver_id`) references user (`user_id`),
    check ( `is_log` in (0, 1))
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
    foreign key (`club_id`) references `club` (`club_id`) on delete cascade,
    check (`identity` in (0, 1, 2))
);

drop table if exists user_event_participate;
create table user_event_participate
(
    `user_id`  varchar(31) not null,
    `event_id` int         not null,
    `identity` smallint    not null,
    primary key (`user_id`, `event_id`),
    foreign key (`user_id`) references `user` (`user_id`),
    foreign key (`event_id`) references `event` (`event_id`),
    check ( `identity` in (0, 1, 2))
);


drop table if exists `user_post`;
create table `user_post`
(
    `user_id` varchar(31) not null,
    `post_id` int         not null,
    `action`  smallint    not null,
    primary key (`user_id`, `post_id`),
    foreign key (`user_id`) references `user` (`user_id`) on delete cascade,
    foreign key (`post_id`) references `post` (`post_id`) on delete cascade,
    check ( `action` in (0, 1) )
);

drop table if exists `user_reply`;
create table `user_reply`
(
    `user_id`  varchar(31) not null,
    `reply_id` int         not null,
    `action`   smallint    not null,
    primary key (`user_id`, `reply_id`),
    foreign key (`user_id`) references `user` (`user_id`) on delete cascade,
    foreign key (`reply_id`) references `reply` (`reply_id`) on delete cascade,
    check ( `action` in (0, 1) )
);

drop table if exists `follow`;
create table `follow`
(
    `follower_id` varchar(31) not null,
    `friend_id`   varchar(31) not null,
    primary key (`follower_id`, `friend_id`),
    foreign key (`follower_id`) references `user` (`user_id`) on delete cascade,
    foreign key (`friend_id`) references `user` (`user_id`) on delete cascade
);

drop table if exists `user_event_like`;
create table `user_event_like`
(
    `user_id`  varchar(31) not null,
    `event_id` int         not null,
    `action`   smallint    not null,
    primary key (`user_id`, `event_id`),
    foreign key (`user_id`) references `user` (`user_id`) on delete cascade,
    foreign key (`event_id`) references `event` (`event_id`) on delete cascade,
    check ( `action` in (0, 1))
);


# alloc id
drop table if exists `id_allocator`;
create table `id_allocator`
(
    `global_id` int not null,
    primary key (`global_id`)
)

