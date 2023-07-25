select building.id                                                as building_id,
       building.name                                              as building_name,
       ST_X(ST_Transform(ST_SetSRID(building.geom, 32630), 4326)) as building_longitude,
       ST_Y(ST_Transform(ST_SetSRID(building.geom, 32630), 4326)) as building_latitude,
       lab.id                                                   as lab_id,
       lab.lab_reference                                                 as lab_name,
       lab.floor_number                                         as lab_floor_number,
       ST_X(ST_Transform(ST_SetSRID(lab.geom, 32630), 4326))    as lab_longitude,
       ST_Y(ST_Transform(ST_SetSRID(lab.geom, 32630), 4326))    as lab_latitude
from public.laboratories lab
         left join buildings building on lab.building_id = building.id
where building.id = %(building_id)s;
