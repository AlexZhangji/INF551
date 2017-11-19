SELECT
	film.title,
	category.NAME 
FROM
	( film JOIN film_category ON film.film_id = film_category.film_id )
	JOIN category ON category.category_id = film_category.category_id 
ORDER BY
	film.title ASC;