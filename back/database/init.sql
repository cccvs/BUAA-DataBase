use club_system;

select allocId();

insert into user(`user_id`, `password`, `time`, `email`, `followers`, `following`)
values ('u_c', 'c', from_unixtime(unix_timestamp()), 'sb', 0, 0),
       ('u_b', 'b', from_unixtime(unix_timestamp()), 'sb', 0, 0),
       ('20373743', '12345678a', from_unixtime(unix_timestamp()), 'sb', 0, 0);
# select * from user;

insert into club(club_id, name, member_count, type, master_id, time, intro) value (1001, '机器人社', 0, 2, 'u_b', from_unixtime(unix_timestamp()), '%s');
insert into club(club_id, name, member_count, type, master_id, time, intro) value (1002, '凌峰社', 0, 2, 'u_c', from_unixtime(unix_timestamp()), '%s');
# select * from club;

insert into event(event_id, club_id, user_id, content, time, apply_time, expired_time, begin_time, end_time, member_count, member_limit) values (2001, 1001, '20373743', 'event1', from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), 1, 200);
insert into event(event_id, club_id, user_id, content, time, apply_time, expired_time, begin_time, end_time, member_count, member_limit) values (2002, 1001, '20373743', 'event2', from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), from_unixtime(unix_timestamp()), 1, 300);