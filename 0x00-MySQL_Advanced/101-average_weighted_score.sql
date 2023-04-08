-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
drop procedure if exists ComputeAverageWeightedScoreForUsers;
delimiter //
create procedure ComputeAverageWeightedScoreForUsers()
begin
    declare n int default 0;
    declare i int default 0;
    select count(*) into n from users;
    set i = 0;
    while i < n do
        set @average_weighted_score = (select sum(score * weight) / sum(weight)
        from projects
        left join corrections on projects.id = corrections.project_id
        where (select id from users limit i, 1);
        update users
        set average_score = @average_weighted_score where id = (select id from users limit i, 1);
        set i = i + 1;
    end while;
end //
delimiter ;
