use club_system;
insert into user(`user_id`, `password`, `time`, `email`)
values('u_c','c', CURRENT_TIMESTAMP, 'sb'),
      ('u_b','b', CURRENT_TIMESTAMP, 'sb');
select * from user;
