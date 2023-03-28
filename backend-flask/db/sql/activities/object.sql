SELECT 
  activities.uuid,
  users.display_name,
  users.handle,
  activities.message,
  activities.created_at,
  activities.expires_at
FROM public.activities
INNER JOIN ´public.users ON users.uuid = activities.user_
WHERE 
  activities.uuid = %(uuid)s