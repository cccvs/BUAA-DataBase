# getUser
select *
from user
where user_id = '%s';

# findClub
select *
from club
where name like '%%s%';


# getUserClubs
select *
from club
where club_id in (select club_id from user_club where user_id = '%s');

# getClubMembers
select * from user where user_id in (select user_id from user_club where club_id = '%s');

# getClubEvents
select * from event where club_id = '%s' and status = 2;

# getClubNotices
select * from notice where club_id = '%s';

# getClubRequests(返回user列表, 并且要求请求未处理(status=0))
select * from user where user_id in (select applicant_id from joining_club where (club_id = '%s' and status = 0));