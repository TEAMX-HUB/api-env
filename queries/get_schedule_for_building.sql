SELECT aew.weekday
     ,aew.department
     ,ss.course_code
     ,ss.year_group
     ,st.start_time
     ,st.end_time
     ,c.name          AS class_name
     ,l.lab_reference AS lab_name
FROM public.academic_event_week AS aew
         LEFT JOIN public.academic_track AS ast
                   ON aew.track_id = ast.id
         LEFT JOIN public.session_schedule AS ss
                   ON aew.schedule_id = ss.id
         LEFT JOIN public.session_time AS st
                   ON ss.schedule_time = st.id
         LEFT JOIN public.classrooms AS c
                   ON ss.class_location = c.id
        left join public.buildings as bb
                on c.building_id = bb.id
         LEFT JOIN public.laboratories AS l
                   ON ss.lab_location = l.id
WHERE aew.weekday = %(weekday)s
        AND bb.id = %(building_id)s;
