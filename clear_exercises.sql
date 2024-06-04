

DELETE FROM public.exercises_historicalexercisecomment where 1=1;

DELETE FROM public.exercises_exercisecomment where 1=1;

DELETE FROM public.manager_setting where 1=1;
DELETE FROM public.manager_workoutlog where 1=1;

DELETE FROM public.exercises_exercisebase_muscles_secondary WHERE 1=1;

DELETE FROM public.exercises_exercisebase_equipment WHERE 1=1;

DELETE FROM public.exercises_exercisebase_muscles WHERE 1=1;

DELETE FROM public.exercises_exercise WHERE 1=1;

DELETE FROM public.exercises_historicalexercise WHERE 1=1;

DELETE FROM public.exercises_exerciseimage WHERE 1=1;

DELETE FROM public.exercises_historicalexerciseimage WHERE 1=1;

DELETE FROM public.exercises_historicalexercisebase WHERE 1=1;

DELETE FROM public.exercises_exercisebase WHERE 1=1;

DELETE FROM public.easy_thumbnails_thumbnail WHERE 1=1;
DELETE FROM public.easy_thumbnails_source WHERE 1=1;

DELETE FROM public.exercises_equipment WHERE id IN (11, 12, 13, 14, 15, 16, 17);

SELECT pg_catalog.setval('public.easy_thumbnails_source_id_seq', (SELECT MAX(id) FROM easy_thumbnails_source), true);
SELECT pg_catalog.setval('public.easy_thumbnails_thumbnail_id_seq', (SELECT MAX(id) FROM easy_thumbnails_thumbnail), true);
SELECT pg_catalog.setval('public.exercises_exercise_id_seq', (SELECT MAX(id) FROM exercises_exercise), true);
SELECT pg_catalog.setval('public.exercises_exercisebase_equipment_id_seq', (SELECT MAX(id) FROM exercises_exercisebase_equipment), true);
SELECT pg_catalog.setval('public.exercises_exercisebase_id_seq', (SELECT MAX(id) FROM exercises_exercisebase), true);
SELECT pg_catalog.setval('public.exercises_exercisebase_muscles_id_seq', (SELECT MAX(id) FROM exercises_exercisebase_muscles), true);
SELECT pg_catalog.setval('public.exercises_exercisebase_muscles_secondary_id_seq', (SELECT MAX(id) FROM exercises_exercisebase_muscles_secondary), true);
SELECT pg_catalog.setval('public.exercises_exerciseimage_id_seq', (SELECT MAX(id) FROM exercises_exerciseimage), true);
SELECT pg_catalog.setval('public.exercises_historicalexercise_history_id_seq', (SELECT MAX(id) FROM exercises_historicalexercise), true);
SELECT pg_catalog.setval('public.exercises_historicalexercisebase_history_id_seq', (SELECT MAX(id) FROM exercises_historicalexercisebase), true);
SELECT pg_catalog.setval('public.exercises_historicalexerciseimage_history_id_seq', (SELECT MAX(id) FROM exercises_historicalexerciseimage), true);