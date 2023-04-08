-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
drop procedure if exists ComputeAverageScoreForUser;
delimiter //
create procedure ComputeAverageScoreForUser(user_id int)
begin
    set @average_score = (select avg(score) from corrections c where c.user_id = user_id);
    update users set average_score = @average_score where id = user_id;
end //
delimiter ;
