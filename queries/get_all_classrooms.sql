select classrooms.name as name,
       classrooms.floor_number as floor_number,
       ST_X(ST_Transform(ST_SetSRID(classrooms.geom, 32630), 4326)) as longitude,
       ST_Y(ST_Transform(ST_SetSRID(classrooms.geom, 32630), 4326)) as latitude,
       b.name as building_name
from public.classrooms as classrooms
         LEFT JOIN public.buildings AS b
                   ON b.id = classrooms.building_id;
