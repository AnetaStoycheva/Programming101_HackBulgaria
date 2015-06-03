-- List all employees with their first name, last name and title
SELECT FirstName, LastName, Title
FROM Employees


-- List all employees from Seattle.
SELECT FirstName, LastName, Title
FROM Employees
WHERE City = 'Seattle'


-- List all employees from London.
SELECT FirstName, LastName, Title
FROM Employees
WHERE City = 'London'


-- List all employees that work in the Sales department.
SELECT FirstName, LastName, Title
FROM Employees
WHERE Title LIKE '%Sales%'


-- List all females employees that work in the Sales department.
SELECT FirstName, LastName, Title, TitleOfCourtesy
FROM Employees
WHERE Title LIKE '%Sales%'
AND TitleOfCourtesy LIKE '%s%'
-- AND TitleOfCourtesy IN ('Ms.', 'Mrs.')


-- List the 5 oldest employees.
SELECT FirstName, LastName, BirthDate
FROM Employees
ORDER BY BirthDate ASC
LIMIT 5
-- ASC - vry6ta v namalqva6t red
-- ima LIMIT 2, 5 -> t.e. pyrvite 5, zapo4vajki ot vtoriq


-- List the first 5 hires of the company.
SELECT FirstName, LastName, HireDate
FROM Employees
ORDER BY HireDate
LIMIT 5


-- List the employee who reports to no one (the boss)
SELECT FirstName, LastName, ReportsTo
FROM Employees
WHERE ReportsTo IS NULL


-- List all employes by their first and last name, and the first and last name of the employees that they report to.
SELECT e.FirstName, e.LastName, e.ReportsTo, managers.FirstName, managers.LastName
FROM Employees AS e
JOIN Employees AS managers
ON e.ReportsTo = managers.EmployeeID
-- WHERE e.ReportsTo IS NOT NULL  -> 6efyt go nqma v rezultata taka ili ina4e, za6toto st-ta mu e Null


-- Count all female employees.
SELECT COUNT(EmployeeID)
FROM Employees
WHERE TitleOfCourtesy
IN ('Ms.', 'Mrs.')


-- Count all male employees.
SELECT COUNT(EmployeeID)
FROM Employees
WHERE TitleOfCourtesy NOT LIKE '%s%'


-- Count how many employees are there from the different cities. For example, there are 4 employees from London.
-- V COUNT moje da slojim vmesto City - Employee ID
SELECT City, COUNT(City)
FROM Employees
GROUP BY City


-- List all OrderIDs and the employees (by first and last name) that have created them.
SELECT FirstName, LastName, OrderID
FROM Employees
JOIN Orders
ON Orders.EmployeeID = Employees.EmployeeID


-- List all OrderIDs and the shipper name that the order is going to be shipped via.
SELECT OrderID, CompanyName
FROM Orders
JOIN Shippers
ON ShipVia = ShipperID


-- List all contries and the total number of orders that are going to be shipped there.
SELECT ShipCountry, COUNT(OrderID) AS OrdersNumbers
FROM Orders
GROUP BY ShipCountry


-- Find the employee that has served the most orders.
SELECT Orders.EmployeeID, FirstName, LastName, COUNT(OrderID) AS order_count
FROM Orders
JOIN Employees
ON Employees.EmployeeID = Orders.EmployeeID
GROUP BY Employees.EmployeeID
ORDER BY order_count DESC
LIMIT 1


-- Find the customer that has placed the most orders.
SELECT Orders.CustomerID, COUNT(*) AS order_count, CompanyName
FROM Orders
JOIN Customers
ON Customers.CustomerID = Orders.CUstomerID
GROUP BY Customers.CustomerID
ORDER BY order_count DESC
LIMIT 1


-- List all orders, with the employee serving them and the customer, that has placed them.
SELECT Employees.EmployeeId, FirstName, LastName, Orders.ShipName, Customers.CompanyName
FROM Orders
JOIN Customers
ON Customers.CustomerID = Orders.CUstomerID
JOIN Employees
ON Employees.EmployeeID = Orders.EmployeeID


-- List for which customer, which shipper is going to deliver the order.
SELECT Customers.CompanyName AS Customer, Shippers.CompanyName AS Shipper
FROM Customers
JOIN Orders
ON Customers.CustomerID = Orders.CUstomerID
JOIN Shippers
ON ShipperID = ShipVia
