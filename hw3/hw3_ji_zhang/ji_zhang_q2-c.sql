SELECT
	COUNT( DISTINCT customer.customer_id ) 
FROM
	customer 
WHERE
	customer.customer_id IN 
	( SELECT action_view.customer_id FROM action_view ) 
	AND 
	customer.customer_id NOT IN 
	( SELECT horror_view.customer_id FROM horror_view );