SELECT name
FROM customer c1
WHERE NOT EXISTS (
    SELECT 1
    FROM customer c2
    WHERE c2.referee_id = 2 AND c1.referee_id = c2.referee_id
);
