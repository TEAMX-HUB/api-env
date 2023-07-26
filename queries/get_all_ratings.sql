SELECT  
    comments,
    rate_value
FROM public.ratings
    LEFT JOIN buildings b ON ratings.building_id = b.id
    LEFT JOIN classrooms c ON b.id = c.building_id
    LEFT JOIN offices o ON b.id = o.building_id
    LEFT JOIN laboratories l ON b.id = l.building_id;
