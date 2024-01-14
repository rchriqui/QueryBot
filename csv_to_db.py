import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('best_countries_2024.db')
cursor = conn.cursor()

# Create a table in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS best_countries_2024 (
        population_2024 INTEGER,
        population_growthRate REAL,
        land_area INTEGER,
        country TEXT,
        region TEXT,
        unMember BOOLEAN,
        population_density REAL,
        population_densityMi REAL,
        share_borders TEXT,
        Hdi2021 REAL,
        Hdi2020 REAL,
        WorldHappiness2022 TEXT
    )
''')
conn.commit()

# Read CSV and insert data into the database
with open('best_countries_2024.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO best_countries_2024 (
                population_2024,
                population_growthRate,
                land_area,
                country,
                region,
                unMember,
                population_density,
                population_densityMi,
                share_borders,
                Hdi2021,
                Hdi2020,
                WorldHappiness2022
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['population_2024'],
            row['population_growthRate'],
            row['land_area'],
            row['country'],
            row['region'],
            row['unMember'],
            row['population_density'],
            row['population_densityMi'],
            row['share_borders'],
            row['Hdi2021'],
            row['Hdi2020'],
            row['WorldHappiness2022']
        ))

conn.commit()
conn.close()
