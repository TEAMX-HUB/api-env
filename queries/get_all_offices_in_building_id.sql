select building.id                                                as building_id,
       building.name                                              as building_name,
       ST_X(ST_Transform(ST_SetSRID(building.geom, 32630), 4326)) as building_longitude,
       ST_Y(ST_Transform(ST_SetSRID(building.geom, 32630), 4326)) as building_latitude,
       staff.id                                                   as staff_id,
       staff.staff_personnel                                                 as staff_name,
       staff.floor_number                                         as staff_floor_number,
       ST_X(ST_Transform(ST_SetSRID(staff.geom, 32630), 4326))    as staff_longitude,
       ST_Y(ST_Transform(ST_SetSRID(staff.geom, 32630), 4326))    as staff_latitude
from public.offices staff
         left join buildings building on staff.building_id = building.id
where building.id = %(building_id)s;
