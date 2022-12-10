use club_system;
insert into user(`user_id`, `password`, `time`, `email`, `followers`, `following`)
values ('u_c', 'c', CURRENT_TIMESTAMP, 'sb', 0, 0),
       ('u_b', 'b', CURRENT_TIMESTAMP, 'sb', 0, 0),
       ('20373043', '12345678a', CURRENT_TIMESTAMP, 'sb', 0, 0);
# select * from user;

insert into club(name, member_count, type, master_id, time, intro) value ('机器人社', 0, 2, 'u_b', CURRENT_TIMESTAMP, '%s');
insert into club(name, member_count, type, master_id, time, intro) value ('凌峰社', 0, 2, 'u_c', CURRENT_TIMESTAMP, '%s');
# select * from club;