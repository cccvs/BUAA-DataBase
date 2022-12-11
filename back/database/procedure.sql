# createUser
use club_system;

delimiter ;;
# createUser
create
    definer = root@localhost procedure createUser(in userId varchar(31), in UserPassword varchar(255),
                                                  in realName varchar(31), in userSex varchar(31),
                                                  in userInstitute varchar(31), in userEmail varchar(31))
begin
    insert into user(user_id, password, time, real_name, sex, institute, email, followers, following) value
        (userId, UserPassword, from_unixtime(unix_timestamp()), userSex, userInstitute, realName, userEmail, 0, 0);
    # end
end;;
delimiter ;

# TODO 限定每个人只能当一个社团社长
delimiter ;;
# createClub
create procedure createClub(in clubName varchar(31), in clubType smallint, in masterId varchar(31),
                            in clubIntro varchar(1022))
begin
    declare clubId int;
    set clubId = allocId();
    insert into club(club_id, name, member_count, type, master_id, time, intro) value (clubId, clubName, 0, clubType,
                                                                                       masterId,
                                                                                       from_unixtime(unix_timestamp()),
                                                                                       clubIntro);
    # 0:普通社员 1:管理员 2:社长
    insert into user_club(user_id, club_id, identity, label) value (masterId, clubId, 2, '社长');
    # end
end;;
delimiter ;

delimiter ;;
# updateUserClubLabel
create procedure updateUserClubLabel(in userLabel varchar(31), userId varchar(31), in clubId int)
begin
    update user_club
    set label = userLabel
    where user_id = userId
      and club_id = clubId;
    # end
end;;
delimiter ;

delimiter ;;
# updateUserField
create procedure updateUserField(in userId varchar(31), in realName varchar(31), in userSex varchar(31),
                                 in userInstitute varchar(31), in userPhone varchar(31), in userEmail varchar(31))
begin
    update user
    set real_name = realName,
        sex       = userSex,
        institute = userInstitute,
        phone     = userPhone,
        email     = userEmail
    where user_id = userId;
    # end
end;;
delimiter ;

delimiter ;;
# handleJoiningClub
create procedure handleJoiningClub(in op smallint, in formId int)
begin
    # type: 0->accept, 1->reject
    # status: 0->处理中, 1->已拒绝, 2->已接受
    declare applicantId varchar(31);
    declare clubId int;
    if op = 0 then
        set applicantId = (select applicant_id from joining_club where form_id = formId);
        set clubId = (select club_id from joining_club where form_id = formId);
        update joining_club set status = 2 where form_id = formId;
        insert into user_club(user_id, club_id, identity, label) values (applicantId, clubId, 0, null);
    else
        update joining_club set status = 1 where form_id = formId;
    end if;
    # end
end;;
delimiter ;

delimiter ;;
# createEvent
create procedure createEvent(in clubId int, in userId varchar(31), in eventTitle varchar(31),
                             in eventCover varchar(255), in eventContent varchar(255), in applyTime varchar(31),
                             in expiredTime varchar(31), in beginTime varchar(31), in endTime varchar(31),
                             in memberLimit int)
begin
    declare eventId int;
    set eventId = allocId();
    insert into event(event_id, club_id, user_id, title, cover, content, time, apply_time, expired_time, begin_time,
                      end_time, member_count, member_limit) VALUE (eventId, clubId, userId, eventTitle, eventCover,
                                                                   eventContent, from_unixtime(unix_timestamp()),
                                                                   applyTime, expiredTime, beginTime, endTime, 0,
                                                                   memberLimit);
    insert into user_event(user_id, event_id, identity) values (userId, eventId, 2);
    # end
end;;
delimiter ;

delimiter ;;
# handleFollowing
create procedure handleFollowing(in followerId varchar(31), in friendId varchar(31))
begin
    insert into follow(follower_id, friend_id) value (followerId, friendId);
    # end
end;;
delimiter ;

delimiter ;;
# handleUnfollowing
create procedure handleUnfollowing(in followerId varchar(31), in friendId varchar(31))
begin
    delete from follow where friend_id = friendId and follower_id = followerId;
    # end
end;;
delimiter ;

delimiter ;;
# updatePassword
create procedure updatePassword(in userId varchar(31), in userPassword varchar(255))
begin
    update user set password = userPassword where user_id = userId;
    # end
end;;
delimiter ;

delimiter ;;
# updateAvatar
create procedure updateAvatar(in userId varchar(31), in userAvatar varchar(255))
begin
    update user set avatar = userAvatar where user_id = userId;
    # end
end;;
delimiter ;