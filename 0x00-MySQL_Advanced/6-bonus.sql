-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

drop procedure if exists AddBonus;
delimiter //
create procedure AddBonus(user_id int, project_name varchar(255), score int)
begin
    if (exists(select * from projects where name = project_name) == 0) then
        insert into projects (name) values (project_name);
    end if;
    set @project_id = (select id from projects where name = project_name limit 1);
    insert into corrections (user_id, project_id, score) values (user_id, @project_id, score);
end //
delimiter ;
