-- SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month
drop view if exists need_meeting;
create view need_meeting as
select u.name
from users u
where u.average_score < 80 
and (u.last_meeting is null or u.last_meeting < date_sub(now(), interval 1 month));
