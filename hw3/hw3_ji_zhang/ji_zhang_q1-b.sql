SELECT DISTINCT
	category.`name`,
	COUNT( film_category.category_id ) AS category_count 
FROM
	film_category
	JOIN category ON category.category_id = film_category.category_id 
GROUP BY
	film_category.category_id 
ORDER BY
	category.`name`  ASC;
