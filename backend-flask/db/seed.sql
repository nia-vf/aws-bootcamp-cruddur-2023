INSERT INTO public.users (display_name, handle, cognito_user_id)
VALUES
  ('Nia Velinor-Fraser', 'Nia_VF', 'MOCK'),
  ('Andrew Brown', 'andrewbrown', 'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid FROM public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )