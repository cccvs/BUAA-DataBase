use club_system;
insert into user(`user_id`, `password`, `time`, `email`)
values(UUID_TO_BIN(UUID()),'c', CURRENT_TIMESTAMP, 'sb'),
      (UUID_TO_BIN(UUID()),'b', CURRENT_TIMESTAMP, 'sb');
select * from user;

