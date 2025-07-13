import sqlite3
import sys

def database(data, query):
    # Start a sqlite3 connection
    con = sqlite3.connect(":memory:")
    # con = sqlite3.connect("flights.db")
    cur = con.cursor()

    # Execute a query to create a table in the flights.db file
    cur.execute('''CREATE TABLE IF NOT EXISTS flights (
        year INTEGER,
        country TEXT,
        iata_code TEXT,
        icao_code TEXT,
        total_passengers INTEGER
    )
    ''')
    con.commit()


    # Test if the table was created correctly
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='flights'")
    if cur.fetchone() is None:
        print("Table does not exist")
        sys.exit(1)
    else:
        print("Table exists")

    # Insert data to table
    for flight in data:
        for airport in flight["airports"]:
            cur.execute('''
                INSERT INTO flights (year, country, iata_code, icao_code, total_passengers)
                VALUES(?, ?, ?, ?, ?)
            ''', 
            (flight["year"], flight["country"], airport["iata_code"], airport["icao_code"], airport["total_passengers"])
            )
    con.commit()

    # Execute query to sum passangers by country
    try:
        res = cur.execute(query)
    except Exception as e:
        print("Query failed: ", query, e)

    # Print results
    rows = res.fetchall()
    for row in rows:
        print(row)

    con.close()
