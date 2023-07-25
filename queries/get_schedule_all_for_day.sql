SELECT
    aew.id,
    aew.weekday,
    aew.department,
    ss.course_code,
    ss.course_name,
    ss.class_location,
    st.start_time,
    st.end_time,
    at.semester,
    at.academic_year
FROM
    public.academic_event_week aew
        RIGHT JOIN public.session_schedule ss ON aew.schedule_id = ss.id
        RIGHT JOIN public.session_time st ON ss.schedule_time = st.id
        RIGHT JOIN public.academic_track at ON aew.track_id = at.id
WHERE
        aew.weekday = %(weekday)s;
