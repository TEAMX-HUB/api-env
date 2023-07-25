SELECT  aew.id                                            AS academic_event_week_id
       ,aew.weekday
       ,aew.department
       ,ss.course_code
       ,ss.course_name
       ,ss.year_group
       ,st.start_time
       ,st.end_time
       ,c.name                                            AS class_name
       ,ST_X(ST_Transform(ST_SetSRID(c.geom,32630),4326)) AS class_longitude
       ,ST_Y(ST_Transform(ST_SetSRID(c.geom,32630),4326)) AS class_latitude
       ,l.lab_reference                                   AS lab_name
       ,ST_X(ST_Transform(ST_SetSRID(l.geom,32630),4326)) AS lab_longitude
       ,ST_Y(ST_Transform(ST_SetSRID(l.geom,32630),4326)) AS lab_latitude
       ,ast.academic_year
       ,ast.semester
FROM public.academic_event_week AS aew
LEFT JOIN public.academic_track AS ast
ON aew.track_id = ast.id
LEFT JOIN public.session_schedule AS ss
ON aew.schedule_id = ss.id
LEFT JOIN public.session_time AS st
ON ss.schedule_time = st.id
LEFT JOIN public.classrooms AS c
ON ss.class_location = c.id
LEFT JOIN public.laboratories AS l
ON ss.lab_location = l.id;
