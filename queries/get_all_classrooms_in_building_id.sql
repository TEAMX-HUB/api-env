select building.id                                                as building_id,
       building.name                                              as building_name,
       ST_X(ST_Transform(ST_SetSRID(building.geom, 32630), 4326)) as building_longitude,
       ST_Y(ST_Transform(ST_SetSRID(building.geom, 32630), 4326)) as building_latitude,
       class.id                                                   as class_id,
       class.name                                                 as class_name,
       class.room_number                                          as class_room_number,
       class.floor_number                                         as class_floor_number,
       ST_X(ST_Transform(ST_SetSRID(class.geom, 32630), 4326))    as class_longitude,
       ST_Y(ST_Transform(ST_SetSRID(class.geom, 32630), 4326))    as class_latitude
from public.classrooms class
         left join buildings building on class.building_id = building.id
where building.id = %(building_id)s;
