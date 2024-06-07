import pyodbc
import sqlite3
import pandas as pd
import os

print('Auth from env (E) or input (I)?')
print('For env (E) auth ensure correct variable name')
answer = input('Type E or I: ')
answer = answer.upper()
possible_answers = ['E', 'I']

if answer not in possible_answers:
    print('Wrong input, try again')
    quit()

if answer == possible_answers[0]:
    var = input('Type variable name: ')
    try:
        cred = os.getenv(var)
        var_unpacked = cred.split(';')
        server = var_unpacked[0]
        database = var_unpacked[1]
        username = var_unpacked[2]
        password = var_unpacked[3]
        print('Database connection: Success')   
    except FileNotFoundError as E:
        print('***Auth failed*** Error')
        print(E)
        quit()
else:
    server = input("Insert server name: ")
    database = input("Insert database name: ")
    username = input("Insert login: ")
    password = input("Insert password: ")

# Connect to SQL Server database and execute a query

query = "SELECT dbo.tw__Towar.tw_Nazwa as Nazwa, dbo.tw__Towar.tw_DostSymbol as Symbol, dbo.tw__Towar.tw_StanMin as Stan_Minimalny, dbo.tw_Stan.st_Stan as Stan FROM dbo.tw__Towar JOIN dbo.tw_Stan on dbo.tw_Stan.st_Towid = dbo.tw__Towar.tw_id JOIN dbo.tw_CechaTw on dbo.tw__Towar.tw_id = dbo.tw_CechaTw.cht_IdTowar WHERE tw_StanMin != 0 and cht_IdCecha = 8 and st_MagId = 4;"
cnxn_str = f"DRIVER=SQL Server Native Client 11.0;SERVER={server};DATABASE={database};UID={username};PWD={password}"

try:
    cnxn = pyodbc.connect(cnxn_str)
    df_sqlserver = pd.read_sql(query, cnxn)

    # Save the data to a SQLite database
    conn = sqlite3.connect("DB_compare.db")
    df_sqlserver.to_sql("prod_subiekt", conn, if_exists="replace", index=False)

    # Retrieve the data from the SQLite database
    df_sqlite = pd.read_sql("SELECT * FROM prod_subiekt", conn)

    # Print the retrieved data
    print(df_sqlite)

# Close the connections
    cnxn.close()
    conn.close()

except:
    print('Connection failed, please check server authentication and try again')



