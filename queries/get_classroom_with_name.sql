select *,
       ST_X(ST_Transform(ST_SetSRID(geom, 32630), 4326)) as longitude,
       ST_Y(ST_Transform(ST_SetSRID(geom, 32630), 4326)) as latitude
from public.classrooms
where classrooms.name like %(name)s;
