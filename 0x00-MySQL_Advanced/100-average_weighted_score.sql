-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
drop procedure if exists ComputeAverageWeightedScoreForUser;
delimiter //
create procedure ComputeAverageWeightedScoreForUser(user_id int)
begin
    set @average_weighted_score = (select sum(score * weight) / sum(weight)
    from projects
    left join corrections on projects.id = corrections.project_id
    where corrections.user_id = user_id);
    update users 
    set average_score = @average_weighted_score where id = user_id;
end //
delimiter ;
