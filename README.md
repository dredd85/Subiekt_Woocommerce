
# WooSub DataSync

Early-stage project that involves analyzing a local database from Subiekt using T-SQL and comparing it to the database in Woocommerce, which uses MySQL. To gather the data, T-SQL will be directly extracted from the local database, while the data from Woocommerce will be obtained through its API.

The primary objective of this project is to identify any discrepancies between the two databases and develop solutions to streamline data management processes. As the project progresses, I'll update this README file to provide more details on the approach taken and the outcomes achieved. Stay tuned for further updates!

This project consists of multiple scripts that compare data between different databases. The scripts utilize various libraries and APIs to perform the necessary operations.

## Installation

To run these scripts, make sure you have the following dependencies installed:

- pyodbc
- sqlite3
- pandas
- woocommerce
- json

You can install these dependencies using pip:

```
pip install pyodbc sqlite3 pandas woocommerce
```

## Usage

1. **Script 1: SQL Server to SQLite Database**

   - Run the script and provide the required information when prompted:
     - SQL Server details (server name, database name, login, and password)
   - The script will connect to the SQL Server database, execute a query to retrieve data, and save the data to a SQLite database named "DB_compare.db."
   - The retrieved data can be accessed and printed from the SQLite database.

2. **Script 2: Woocommerce API Data Fetch**

   - Run the script and provide the required information when prompted:
     - Woocommerce site URL, consumer key, and secret key
   - The script will connect to the Woocommerce site using the provided API credentials.
   - It will fetch both in-stock and out-of-stock products from the Woocommerce site using the Woocommerce API.
   - The retrieved data will be stored in the "prod_woo" table of the SQLite database "DB_compare.db."

3. **Script 3: Reports**

   - Run the script to compare the data in SQLITE database between the Woocommerce table ("prod_woo") and the local Subiekt("prod_subiekt").
   - The script will execute SQL queries to identify differences in stock levels, out-of-stock products, and overall product count.
   - Any differences found will be reported, including products with low stock levels, out-of-stock products, and discrepancies in overall product count.
  
4. **Script 3.1: Auto Update**

   - This script checks and compares the products with an "out of stock" status between WooCommerce and the local Subiekt database.
   - After the initial check, the script displays which products should be updated online.   
   - The script then prompts the user for confirmation before proceeding with the update.
