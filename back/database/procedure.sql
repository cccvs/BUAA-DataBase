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
        (userId, UserPassword, from_unixtime(unix_timestamp()), realName, userSex, userInstitute, userEmail, 0, 0);
    # end
end;;
delimiter ;

# TODO 限定每个人只能当一个社团社长
delimiter ;;
# createClub
create procedure createClub(in clubName varchar(31), in clubType smallint, in masterId varchar(31),
                            in clubIntro varchar(1022), in clubCover varchar(255), in clubWelcome varchar(255),
                            in clubWelcomeImage varchar(255))
begin
    declare clubId int;
    set clubId = allocId();
    # 审核状态，0-2分别对应：审核中，未通过，已通过
    insert into club(club_id, name, type, star, member_count, time, intro, master_id, cover,
                     status, welcome, welcome_image) value (clubId, clubName, clubType, 0, 0,
                                                            from_unixtime(unix_timestamp()), clubIntro,
                                                            masterId, clubCover, 0, clubWelcome, clubWelcomeImage);
    commit;
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
create procedure handleJoiningClub(in op smallint, in formId int, in clubLabel varchar(31))
begin
    # type: 0->accept, 1->reject
    # status: 0->处理中, 1->已拒绝, 2->已接受
    declare applicantId varchar(31);
    declare clubId int;
    declare messageId int;
    declare receiverId varchar(31);
    declare clubName varchar(31);
    set applicantId = (select applicant_id from joining_club where form_id = formId);
    set clubId = (select club_id from joining_club where form_id = formId);
    set messageId = allocId();
    set receiverId = applicantId;
    set clubName = (select name from club where club_id = clubId);
    if op = 0 then
        update joining_club set status = 2 where form_id = formId;
        insert into user_club(user_id, club_id, identity, label) values (applicantId, clubId, 0, clubLabel);
        # 消息
        insert into message(message_id, receiver_id, time, content)
        values (messageId, receiverId, from_unixtime(unix_timestamp()),
                concat('Your request of joining club \'', clubName, '\' has been approved.'));
    else
        delete from joining_club where form_id = formId;
        # 消息
        insert into message(message_id, receiver_id, time, content)
        values (messageId, receiverId, from_unixtime(unix_timestamp()),
                concat('Your request of joining club \'', clubName, '\' has been rejected.'));
    end if;
    delete from joining_club where form_id = formId;
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
                      end_time, member_count, member_limit, status, `like`, dislike)
    values (eventId, clubId, userId,
            eventTitle, eventCover, eventContent,
            from_unixtime(unix_timestamp()),
            applyTime, expiredTime, beginTime, endTime,
            0, memberLimit, 0, 0, 0);
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

# 1221
delimiter ;;
# publishNotice
create procedure publishNotice(in noticeTitle varchar(31), in noticeContent varchar(1022), in userId varchar(31),
                               in clubId int,
                               in noticeTop smallint)
begin
    declare noticeId int;
    set noticeId = allocId();
    insert into notice(notice_id, title, content, user_id, club_id, top)
    values (noticeId, noticeTitle, noticeContent, userId, clubId, noticeTop);
end ;;
delimiter ;

delimiter ;;
# joinClub
create procedure joinClub(in userId varchar(31), in clubId int)
begin
    declare formId int;
    set formId = allocId();
    delete from joining_club where applicant_id = userId and club_id = clubId;
    insert into joining_club(form_id, applicant_id, club_id, status, time)
    values (formId, userId, clubId, 0, from_unixtime(unix_timestamp()));
end ;;
delimiter ;

delimiter ;;
# joinClub
create procedure joinClubDirect(in userId varchar(31), in clubId int, in clubLabel varchar(31))
begin
    delete from user_club where user_id = userId and club_id = clubId;
    insert into user_club(user_id, club_id, identity, label) values (userId, clubId, 0, clubLabel);
end ;;
delimiter ;

delimiter ;;
# quitClub
create procedure quitClub(in userId varchar(31), in masterId varchar(31), in clubId int, in clubName varchar(31))
begin
    declare messageId int;
    set messageId = allocId();
    delete from user_club where user_id = userId and club_id = clubId;
    insert into message(message_id, receiver_id, time, content)
    values (messageId, masterId, from_unixtime(unix_timestamp()), concat(userId, ' has quit club ', clubName, '.'));
end ;;
delimiter ;

delimiter ;;
create procedure deleteMessage(in messageId int)
begin
    delete from message where message_id = messageId;
end ;;
delimiter ;

delimiter ;;
create procedure deleteAllMessages(in userId varchar(31))
begin
    delete from message where receiver_id = userId;
end ;;
delimiter ;

# 1222
delimiter ;;
create procedure participateEvent(in userId varchar(31), in eventId int)
begin
    declare memberCount int;
    declare memberLimit int;
    set memberCount = (select member_count from event where event_id = eventId);
    set memberLimit = (select member_limit from event where event_id = eventId);
    if memberCount < memberLimit then
        delete from user_event_participate where user_id = userId and event_id = eventId;
        insert into user_event_participate (user_id, event_id, identity) values (userId, eventId, 0);
    end if;
end ;;
delimiter ;

delimiter ;;
create procedure likeEvent(in userId varchar(31), in eventId int, in op int)
begin
    delete from user_event_like where user_id = userId and event_id = eventId;
    # 相应赞/踩
    if op <> 2 then
        insert into user_event_like(user_id, event_id, action) values (userId, eventId, op);
    end if;
end ;;
delimiter ;

delimiter ;;
create procedure likePost(in userId varchar(31), in postId int, in op int)
begin
    delete from user_post where user_id = userId and post_id = postId;
    # 相应赞/踩
    if op <> 2 then
        insert into user_post(user_id, post_id, action) values (userId, postId, op);
    end if;
end ;;
delimiter ;

delimiter ;;
create procedure publishPost(in userId varchar(31), in clubId int, in postTitle varchar(31),
                             in postContent varchar(1022))
begin
    declare postId int;
    set postId = allocId();
    insert into post(post_id, club_id, user_id, time, title, content, `like`, dislike)
    values (postId, clubId, userId, from_unixtime(unix_timestamp()), postTitle, postContent, 0, 0);
end ;;
delimiter ;

delimiter ;;
create procedure handleCreateClub(in clubId int, in op int, in userLabel varchar(31))
begin
    declare masterId varchar(31);
    declare messageId int;
    declare receiverId varchar(31);
    declare clubName varchar(31);
    set messageId = allocId();
    set receiverId = (select master_id from club where club_id = clubId);
    set clubName = (select name from club where club_id = clubId);
    # op 0不通过, 1通过
    if op = 1 then
        # 0普通社员, 2社长
        set masterId = (select master_id from club where club_id = clubId);
        update club set status = 2 where club_id = clubId;
        insert into user_club(user_id, club_id, identity, label) values (masterId, clubId, 2, userLabel);
        # 通知
        insert into message(message_id, receiver_id, time, content)
        values (messageId, receiverId, from_unixtime(unix_timestamp()),
                concat('Your request of creating club \'', clubName, '\' has been approved.'));
    else
        delete from club where club_id = clubId;
        # 通知
        insert into message(message_id, receiver_id, time, content)
        values (messageId, receiverId, from_unixtime(unix_timestamp()),
                concat('Your request of creating club \'', clubName, '\' has been rejected.'));
    end if;
    # 删除表单
end ;;
delimiter ;

delimiter ;;
create procedure handleCreateEvent(in eventId int, in op int)
begin
    declare userId varchar(31);
    declare messageId int;
    declare receiverId varchar(31);
    declare eventTile varchar(31);
    set messageId = allocId();
    set receiverId = (select user_id from event where event_id = eventId);
    set eventTile = (select title from event where event_id = eventId);
    # op 0不通过, 1通过
    if op = 1 then
        # 0参与者, 2发起者
        set userId = (select user_id from event where event_id = eventId);
        update event set status = 2 where event_id = eventId;
        insert into user_event_participate(user_id, event_id, identity) values (userId, eventId, 2);
        # 通知
        insert into message(message_id, receiver_id, time, content)
        values (messageId, receiverId, from_unixtime(unix_timestamp()),
                concat('Your request of creating event \'', eventTile, '\' has been approved.'));
    else
        delete from event where event_id = eventId;
        # 通知
        insert into message(message_id, receiver_id, time, content)
        values (messageId, receiverId, from_unixtime(unix_timestamp()),
                concat('Your request of creating event \'', eventTile, '\' has been rejected.'));
    end if;
    # 删除表单
end ;;
delimiter ;

# 1223
delimiter ;;
create procedure deleteNotice(in noticeId int)
begin
    delete from notice where notice_id = noticeId;
end ;;
delimiter ;

delimiter ;;
create procedure deletePost(in postId int)
begin
    # 级联删除
    delete from post where post_id = postId;
end ;;
delimiter ;

delimiter ;;
create procedure deleteReply(in replyId int)
begin
    delete from reply where reply_id = replyId;
end ;;
delimiter ;

delimiter ;;
create procedure rateClubStar(in clubId int, in clubStar smallint)
begin
    update club set star = clubStar where club_id = clubId;
end ;;
delimiter ;

delimiter ;;
create procedure modifyClubInfo(in clubId int, in clubName varchar(31), in clubType smallint,
                                in clubIntro varchar(1022), in clubCover varchar(255), in clubWelcome varchar(255),
                                in clubWelcomeImage varchar(255))
begin
    update club
    set name          = clubName,
        type          = clubType,
        intro         = clubIntro,
        cover         = clubCover,
        welcome       = clubWelcome,
        welcome_image = clubWelcomeImage
    where club_id = clubId;
end ;;
delimiter ;

delimiter ;;
create procedure replyPost(in userId varchar(31), in postId int, in postContent varchar(255))
begin
    declare replyId int;
    set replyId = allocId();
    insert into reply (reply_id, post_id, user_id, time, content, `like`, dislike)
    values (replyId, postId, userId, from_unixtime(unix_timestamp()), postContent, 0, 0);
end ;;
delimiter ;

delimiter ;;
create procedure likeReply(in userId varchar(31), in replyId int, in op int)
begin
    delete from user_reply where user_id = userId and reply_id = replyId;
    # 相应赞/踩
    if op <> 2 then
        insert into user_reply(user_id, reply_id, action) values (userId, replyId, op);
    end if;
end ;;
delimiter ;