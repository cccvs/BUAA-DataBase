use club_system;

delimiter ;;

drop trigger if exists updateUserClub1;
create trigger updateUserClub1
    after insert on user_club
    for each row
begin
    update club set member_count = member_count + 1 where club_id = NEW.club_id;
end ;;

drop trigger if exists updateUserClub2;
create trigger updateUserClub2
    after delete on user_club
    for each row
begin
    update club set member_count = member_count - 1 where club_id = OLD.club_id;
end ;;

drop trigger if exists updateFollow;
create trigger updateFollow
    after insert on follow
    for each row
begin
    update user set following = following + 1 where user_id = NEW.follower_id;
    update user set followers = followers + 1 where user_id = NEW.friend_id;
end ;;

drop trigger if exists updateUnfollow;
create trigger updateUnfollow
    after delete on follow
    for each row
begin
    update user set following = following - 1 where user_id = OLD.follower_id;
    update user set followers = followers - 1 where user_id = OLD.friend_id;
end ;;

drop trigger if exists updateUserPost1;
create trigger updateUserPost1
    after insert on user_post
    for each row
begin
    if NEW.action = 0 then
        update post set `like` = `like` + 1 where post.post_id = NEW.post_id;
    else
        update post set dislike = dislike + 1 where post.post_id = NEW.post_id;
    end if ;
end ;;

drop trigger if exists updateUserPost2;
create trigger updateUserPost2
    after update on user_post
    for each row
begin
    if OLD.action = 0 then
        update post set `like` = `like` - 1 where post.post_id = OLD.post_id;
    else
        update post set dislike = dislike - 1 where post.post_id = OLD.post_id;
    end if ;
    if NEW.action = 0 then
        update post set `like` = `like` + 1 where post.post_id = NEW.post_id;
    else
        update post set dislike = dislike + 1 where post.post_id = NEW.post_id;
    end if ;
end ;;

drop trigger if exists updateUserPost3;
create trigger updateUserPost3
    after delete on user_post
    for each row
begin
    if OLD.action = 0 then
        update post set `like` = `like` - 1 where post.post_id = OLD.post_id;
    else
        update post set dislike = dislike - 1 where post.post_id = OLD.post_id;
    end if ;
end ;;

drop trigger if exists updateUserReply1;
create trigger updateUserReply1
    after insert on user_reply
    for each row
begin
    if NEW.action = 0 then
        update reply set `like` = `like` + 1 where reply.reply_id = NEW.reply_id;
    else
        update reply set `dislike` = `dislike` + 1 where reply.reply_id = NEW.reply_id;
    end if ;
end ;;

drop trigger if exists updateUserReply2;
create trigger updateUserReply2
    after update on user_reply
    for each row
begin
    if OLD.action = 0 then
        update reply set `like` = `like` - 1 where reply.reply_id = OLD.reply_id;
    else
        update reply set `dislike` = `dislike` - 1 where reply.reply_id = OLD.reply_id;
    end if ;
    if NEW.action = 0 then
        update reply set `like` = `like` + 1 where reply.reply_id = NEW.reply_id;
    else
        update reply set `dislike` = `dislike` + 1 where reply.reply_id = NEW.reply_id;
    end if ;
end ;;

drop trigger if exists updateUserReply3;
create trigger updateUserReply3
    after delete on user_reply
    for each row
begin
    if OLD.action = 0 then
        update reply set `like` = `like` - 1 where reply.reply_id = OLD.reply_id;
    else
        update reply set `dislike` = `dislike` - 1 where reply.reply_id = OLD.reply_id;
    end if ;
end ;;

drop trigger if exists updateUserEventLike1;
create trigger updateUserEventLike1
    after insert on user_event_like
    for each row
begin
    if NEW.action = 0 then
        update event set `like` = `like` + 1 where event.event_id = NEW.event_id;
    else
        update event set dislike = dislike + 1 where event.event_id = NEW.event_id;
    end if ;
end ;;

drop trigger if exists updateUserEventLike2;
create trigger updateUserEventLike2
    after update on user_event_like
    for each row
begin
    if OLD.action = 0 then
        update event set `like` = `like` - 1 where event.event_id = OLD.event_id;
    else
        update event set dislike = dislike - 1 where event.event_id = OLD.event_id;
    end if ;
    if NEW.action = 0 then
        update event set `like` = `like` + 1 where event.event_id = NEW.event_id;
    else
        update event set dislike = dislike + 1 where event.event_id = NEW.event_id;
    end if ;
end ;;

drop trigger if exists updateUserEventLike3;
create trigger updateUserEventLike3
    after delete on user_event_like
    for each row
begin
    if OLD.action = 0 then
        update event set `like` = `like` - 1 where event.event_id = OLD.event_id;
    else
        update event set dislike = dislike - 1 where event.event_id = OLD.event_id;
    end if ;
end ;;

drop trigger if exists updateUserEventParticipate1;
create trigger updateUserEventParticipate1
    after insert on user_event_participate
    for each row
begin
    update event set member_count = member_count + 1 where event.event_id = NEW.event_id;
end ;;

drop trigger if exists updateUserEventParticipate2;
create trigger updateUserEventParticipate2
    after delete on user_event_participate
    for each row
begin
    update event set member_count = member_count - 1 where event.event_id = OLD.event_id;
end ;;

delimiter ;
