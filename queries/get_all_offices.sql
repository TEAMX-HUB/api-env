select offices.staff_personnel as name,
       offices.floor_number as floor_number,
       ST_X(ST_Transform(ST_SetSRID(offices.geom, 32630), 4326)) as longitude,
       ST_Y(ST_Transform(ST_SetSRID(offices.geom, 32630), 4326)) as latitude,
       b.name as building_name
from public.offices as offices
         LEFT JOIN public.buildings AS b
                   ON b.id = offices.building_id;
