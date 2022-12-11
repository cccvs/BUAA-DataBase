use club_system;
insert into user(`user_id`, `password`, `time`, `email`, `followers`, `following`)
values ('u_c', 'c', CURRENT_TIMESTAMP, 'sb', 0, 0),
       ('u_b', 'b', CURRENT_TIMESTAMP, 'sb', 0, 0),
       ('20373743', '12345678a', CURRENT_TIMESTAMP, 'sb', 0, 0);
# select * from user;

insert into club(club_id, name, member_count, type, master_id, time, intro) value (1001, '机器人社', 0, 2, 'u_b', CURRENT_TIMESTAMP, '%s');
insert into club(club_id, name, member_count, type, master_id, time, intro) value (1002, '凌峰社', 0, 2, 'u_c', CURRENT_TIMESTAMP, '%s');
# select * from club;

insert into event(event_id, club_id, user_id, content, time, apply_time, expired_time, begin_time, end_time, member_count, member_limit) values (2001, 1001, '20373743', 'event1', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1, 200);
insert into event(event_id, club_id, user_id, content, time, apply_time, expired_time, begin_time, end_time, member_count, member_limit) values (2002, 1001, '20373743', 'event2', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, 1, 300)