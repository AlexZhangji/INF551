SELECT DISTINCT
	category.NAME,
	COUNT( film_category.category_id ) AS cate_count 
FROM
	film_category
	JOIN category ON category.category_id = film_category.category_id 
GROUP BY
	film_category.category_id 
HAVING
	COUNT( film_category.category_id ) >= 60 
ORDER BY
	COUNT( film_category.category_id ) DESC;
