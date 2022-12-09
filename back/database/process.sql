# basic

# createUser
insert into user(user_id, password, time, real_name, email, followers, following) value ('%s', '%s', CURRENT_TIMESTAMP, '%s', '%s', 0, 0);

# getUser
select *
from user
where user_id = '%s';

# createClub
insert into club(club_id, name, member_count, type, master_id, time, intro) value (UUID_TO_BIN(UUID()), '%s', 0, '%s', '%s', CURRENT_TIMESTAMP, '%s');

# findClub
select *
from club
where name like '%%s%';

# updateUserClubLabel
update user_club set label = '%s' where user_id = '%s' and club_id = '%s';

# getUserClubs
select * from club where club_id in (select club_id from user_club where user_id = '%s');

# getClubMembers
select * from user where user_id in (select user_id from user_club where club_id = '%s')

# getClubActivities
select * from event where club_id = '%s';

# getClubNotices
select * from notice where notice_id in (select n)