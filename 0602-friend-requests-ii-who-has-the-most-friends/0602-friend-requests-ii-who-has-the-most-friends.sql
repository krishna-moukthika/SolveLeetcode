# Write your MySQL query statement below
WITH num_friends AS(
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id
    FROM RequestAccepted
)

SELECT id, COUNT(id) As num
FROM num_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1