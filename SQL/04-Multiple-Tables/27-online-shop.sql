SELECT products.name, COUNT(item_id) 
FROM orders
JOIN products
ON orders.item_id = products.id
GROUP BY item_id
ORDER BY COUNT(item_id) DESC;

SELECT products.name, orders.customer
FROM orders
JOIN products
ON orders.item_id = products.id
GROUP BY orders.item_id;

SELECT date, COUNT(item_id)
FROM orders
GROUP BY DATE
ORDER BY COUNT(item_id) DESC;