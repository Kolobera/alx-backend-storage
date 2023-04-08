-- SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
drop function if exists SafeDiv;
delimiter //
create function SafeDiv(a int, b int)
returns float deterministic
begin
    if b = 0 then
        return 0;
    end if;
    return a / b;
end //
delimiter ; 
