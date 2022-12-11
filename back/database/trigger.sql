use club_system;

delimiter ;;

create trigger updateFollow
    after insert on follow
    for each row
begin
    update user set following = following + 1 where user_id = NEW.follower_id;
    update user set followers = followers + 1 where user_id = NEW.friend_id;
end ;;

create trigger updateUnfollow
    after delete on follow
    for each row
begin
    update user set following = following + 1 where user_id = OLD.follower_id;
    update user set followers = followers + 1 where user_id = OLD.friend_id;
end ;;