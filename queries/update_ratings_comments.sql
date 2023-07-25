update public.ratings

SET comments = %(new_comment)s
WHERE ratings.id = %(rating_id)s;
