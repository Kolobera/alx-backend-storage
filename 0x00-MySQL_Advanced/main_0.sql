
-- add one order
SELECT * FROM items;
SELECT * FROM orders;

SELECT "--";

INSERT INTO orders (item_name, number) VALUES ('item 1', 1);

SELECT "--";

SELECT * FROM items;
SELECT * FROM orders;