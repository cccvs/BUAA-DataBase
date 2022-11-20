use club_system;
insert into user(`user_id`, `user_name`, `password`, `time`, `email`)
values(UUID_TO_BIN(UUID()), 'c', 'c', CURRENT_TIMESTAMP, 'sb'),
      (UUID_TO_BIN(UUID()), 'b', 'b', CURRENT_TIMESTAMP, 'sb');
select * from user;
