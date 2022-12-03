use club_system;
insert into user(`user_id`, `password`, `time`, `email`, `followers`, `following`)
values('u_c','c', CURRENT_TIMESTAMP, 'sb', 0, 0),
      ('u_b','b', CURRENT_TIMESTAMP, 'sb', 0, 0);
select * from user;
