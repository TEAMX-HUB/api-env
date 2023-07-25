SELECT
    aew.id,
    aew.weekday,
    aew.department,
    aew.schedule_id,
    aew.track_id,
    st.start_time,
    st.end_time,
    ss.course_code,
    ss.course_name,
    ss.year_group,
    ss.class_location,
    ss.lab_location
FROM
    public.academic_event_week aew
        RIGHT JOIN public.session_schedule ss ON aew.schedule_id = ss.id
        RIGHT JOIN public.session_time st ON ss.schedule_time = st.id
WHERE
        aew.weekday = %(weekday)s
  AND st.start_time = %(start_time)s
  AND st.end_time = %(end_time)s;
