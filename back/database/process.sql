# basic

# createUser
insert into user(user_id, password, time, real_name, email, followers, following) value ('%s', '%s', CURRENT_TIMESTAMP, '%s', '%s', 0, 0);

# getUser
select *
from user
where user_id = '%s';

# createClub
# TODO 限定每个人只能当一个社团社长
insert into club(club_id, name, member_count, type, master_id, time, intro) value (UUID_TO_BIN(UUID()), '%s', 0, '%s', '%s', CURRENT_TIMESTAMP, '%s');

# findClub
select *
from club
where name like '%%s%';

# updateUserClubLabel
update user_club
set label = '%s'
where user_id = '%s'
  and club_id = '%s';

# getUserClubs
select *
from club
where club_id in (select club_id from user_club where user_id = '%s');

# getClubMembers
select *
from user
where user_id in (select user_id from user_club where club_id = '%b');

# getClubActivities
select *
from event
where club_id = '%b';

# getClubNotices
select *
from notice
where club_id = '%b';

# updateUserField
update user
set password  = '%s',
    avatar    = '%s',
    time      = '%s',
    real_name = '%s',
    sex       = '%s',
    institute = '%s',
    phone     = '%s',
    email     = '%s',
    level     = '%s',
    following = '%s',
    followers = '%s'
where user_id = '%s';

# getUser
select *
from user
where user_id = '%s';

# getClubRequests(返回user列表, 并且要求请求未处理(status=0))
select *
from user
where user_id in (select applicant_id from joining_club where (club_id = '%s' and status = 0));

# handleJoining
create procedure handleJoining(in type smallint, in formId binary(16))
begin
    # type: 0->accept, 1->reject
    # status: 0->处理中, 1->已拒绝, 2->已接受
    declare applicantId varchar(31);
    declare clubId binary(16);
    declare error int default 0;
    declare continue handler for sqlexception set error = 1;
    if type = 0 then
        set applicantId = (select applicant_id from joining_club where form_id = formId);
        set clubId = (select club_id from joining_club where form_id = formId);
        update joining_club set status = 2 where form_id = formId;
        insert into user_club(user_id, club_id, identity, label) values (applicantId, clubId, 0, null);
    else
        update joining_club set status = 1 where form_id = formId;
    end if;
    # end
    if error = 1 then
        rollback;
    else
        commit;
    end if;
end;

# createEvent
# insert into event(event_id, club_id, user_id, intro, time, apply_time, expired_time, begin_time, end_time, member_count, `limit`) values ('%s')