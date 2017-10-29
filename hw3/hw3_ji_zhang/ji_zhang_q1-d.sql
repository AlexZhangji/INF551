SELECT DISTINCT
	category.NAME 
FROM
	film_category
	JOIN category ON category.category_id = film_category.category_id 
GROUP BY
	film_category.category_id 
ORDER BY
	COUNT( film_category.category_id ) DESC 
	LIMIT 1;
