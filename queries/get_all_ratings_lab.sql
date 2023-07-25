select
       comments,
       rate_value

from public.ratings
         left join buildings b on ratings.building_id = b.id
         left join classrooms c on b.id = c.building_id
         left join offices o on b.id = o.building_id
         left join laboratories l on b.id = l.building_id
where lab_id = %(lab_id)s;
