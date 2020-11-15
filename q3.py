import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="root")

cursor = db.cursor()

cursor.execute("use supplierProduct")

# -- 2.	Display the names of the products that are supplied
sql2 = """SELECT distinct name, id FROM supplierproduct.product;"""

ans2 = cursor.execute(sql2)
# [('Nut',), ('Bolt',), ('Screw',), ('Cam',), ('Cog',)]
ans2 = [k for (k,v) in cursor.fetchall()]
print("products names that are supplied")
print("------------")
for product in set(ans2):
    print(product)


# -- 3.	Display the names of products that are supplied in more than 400 units
sql3 = """SELECT distinct product.name, id
          from product, supplierproduct2
          where product.id=supplierproduct2.pid
          and supplierproduct2.qty>400;"""

ans3 = cursor.execute(sql3)
ans3 = [k for (k,v) in cursor.fetchall()]
print("products that are supplied in more than 400 units")
print("------------")
for product in set(ans3):
    print(product)

# -- 4.	Write a query to count the number of suppliers
sql4 = """select count(*), 1 from supplier;"""
ans4 = cursor.execute(sql4)
ans4 = [k for (k,v) in cursor.fetchall()]
print("count the number of suppliers")
print("------------")
for supplier in set(ans4):
    print(supplier)

# -- 5.	Display the total number of products
sql5 = """select count(*), 1 from product;"""
ans5 = cursor.execute(sql5)
ans5 = [k for (k,v) in cursor.fetchall()]
print("Number of products")
print("------------")
for product in set(ans5):
    print(product)

# -- 6.	Count the total number of suppliers that are offering product P1

sql6 = """select count(distinct supplierproduct2.sid) as N_suppliers, 1
          from supplierproduct2
          where supplierproduct2.pid='P1';"""
ans6 = cursor.execute(sql6)
ans6 = [k for (k,v) in cursor.fetchall()]
print("Number of products")
print("------------")
for supplier in set(ans6):
    print(supplier)

# -- 7.	Write a query to display the names of products that smith is offering.
sql7 = """select product.name, 1
          from product, supplier, supplierproduct2
          where product.id=supplierproduct2.pid
          and supplier.id=supplierproduct2.sid
          and supplier.name='Smith'"""
ans7 = cursor.execute(sql7)
ans7 = [k for (k,v) in cursor.fetchall()]
print("names of products that smith is offering")
print("------------")
for product in set(ans7):
    print(product)
# -- 8.	Get all Supplier Name whose name contains the string “Ja”
sql8 = """select name, 1 from supplier where name like '%jo%';"""
ans8 = cursor.execute(sql8)
ans8 = [k for (k,v) in cursor.fetchall()]
print("Name whose name contains the string “Jo”")
print("------------")
for supplier_name in set(ans8):
    print(supplier_name)


