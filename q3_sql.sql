-- 1.	Which are the foreign keys,  and that do they mean in the current database?

-- take FKs from TABLE supplierProduct2; make references between products and suppliers

-- 2.	Display the names of the products that are supplied

SELECT distinct name FROM supplierproduct.product;

-- 3.	Display the names of products that are supplied in more than 400 units

select distinct name from product right join supplierproduct2 on product.id = supplierproduct2.pid where qty > 400;

SELECT distinct product.name
from product, supplierproduct2
where product.id=supplierproduct2.pid
and supplierproduct2.qty>400;

-- 4.	Write a query to count the number of suppliers

select count(distinct name) from supplier;
select count(*) from supplier;

-- 5.	Display the total number of products

select count(distinct name) from product;
select count(*) from product;

-- 6.	Count the total number of suppliers that are offering product P1

select count(sid) from supplierproduct2 where pid='P1';

select count(supplier.name)
from supplier, supplierproduct2
where supplier.id=supplierproduct2.sid
and supplierproduct2.pid='P1';

select count(distinct supplierproduct2.sid) as N_suppliers
from supplierproduct2
where supplierproduct2.pid='P1';

-- 7.	Write a query to display the names of products that smith is offering.

select product.name
from product, supplier, supplierproduct2
where product.id=supplierproduct2.pid
and supplier.id=supplierproduct2.sid
and supplier.name='Smith';

-- 8.	Get all Supplier Name whose name contains the string “Ja”

select * from supplier where name like '%jo%';

