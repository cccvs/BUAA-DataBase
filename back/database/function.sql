use club_system;
set global log_bin_trust_function_creators = 1;

delimiter ;;
drop function if exists allocId;
create definer = root@localhost function allocId() returns int
begin
    declare init int;
    declare idCount int;
    set init = (select count(*) from id_allocator);
    if init = 0 then
        insert into id_allocator(global_id) values (0);
    end if;
    set idCount = (select global_id from id_allocator limit 1);
    update id_allocator set global_id = (global_id + 1);
    return idCount;
end;;
delimiter ;