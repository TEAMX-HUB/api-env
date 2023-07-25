select user_id,
       comments,
       rate_value,
       b.name as building_name,
       ST_X(ST_Transform(ST_SetSRID(b.geom, 32630), 4326)) as building_longitude,
       ST_Y(ST_Transform(ST_SetSRID(b.geom, 32630), 4326)) as building_latitude,
       c.name as class,
       ST_X(ST_Transform(ST_SetSRID(c.geom, 32630), 4326)) as class_longitude,
       ST_Y(ST_Transform(ST_SetSRID(c.geom, 32630), 4326)) as class_latitude,
       o.staff_personnel as office_of,
       ST_X(ST_Transform(ST_SetSRID(o.geom, 32630), 4326)) as office_longitude,
       ST_Y(ST_Transform(ST_SetSRID(o.geom, 32630), 4326)) as office_latitude,
       l.lab_reference as lab,
       ST_X(ST_Transform(ST_SetSRID(l.geom, 32630), 4326)) as lab_longitude,
       ST_Y(ST_Transform(ST_SetSRID(l.geom, 32630), 4326)) as lab_latitude

from public.ratings
         left join buildings b on ratings.building_id = b.id
         left join classrooms c on b.id = c.building_id
         left join offices o on b.id = o.building_id
         left join laboratories l on b.id = l.building_id
where o.id = %(office_id)s;
