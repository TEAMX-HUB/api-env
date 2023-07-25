insert into public.ratings(comments, building_id, classroom_id, office_id, lab_id, rate_value)
values (%(comments)s, %(building_id)s, %(classroom_id)s, %(office_id)s, %(lab_id)s, %(rate_value)s );
