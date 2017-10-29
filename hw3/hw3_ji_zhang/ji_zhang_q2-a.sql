CREATE VIEW action_view AS SELECT
DISTINCT customer.customer_id
FROM
	customer
	JOIN rental ON rental.customer_id = customer.customer_id
	JOIN inventory ON rental.inventory_id = inventory.inventory_id
	JOIN film_category ON film_category.film_id = inventory.film_id
	JOIN category ON film_category.category_id = category.category_id
WHERE
	category.`name` = 'Action'
	;