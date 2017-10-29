SELECT 
	( CONCAT( actor.first_name, '  ', actor.last_name ) ) AS actor_name 
FROM
	actor
	JOIN film_actor ON film_actor.actor_id = actor.actor_id 
GROUP BY
	film_actor.actor_id 
HAVING
	COUNT( film_actor.actor_id ) >= 2 
ORDER BY
	( CONCAT( actor.first_name, '  ', actor.last_name ) ) ASC;
