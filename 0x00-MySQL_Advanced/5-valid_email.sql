-- SQL script to resets the attribute valid_email only when the email has been changed
delimiter //
create trigger reset_valid_email
before update on users
for each row
begin
    if old.email != new.email then
        set new.valid_email = 0;
    end if;
end //
delimiter ;
