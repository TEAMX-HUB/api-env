select labs.lab_reference as name,
       labs.floor_number as floor_number,
       ST_X(ST_Transform(ST_SetSRID(labs.geom, 32630), 4326)) as longitude,
       ST_Y(ST_Transform(ST_SetSRID(labs.geom, 32630), 4326)) as latitude,
       b.name as building_name
from public.laboratories as labs
         LEFT JOIN public.buildings AS b
                   ON b.id = labs.building_id;
