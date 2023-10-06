import requests
from bs4 import BeautifulSoup
import sqlite3

dbName = "OlympicsData.db"
con = sqlite3.connect(dbName)
cursor = con.cursor()

query="SELECT * FROM SummerOlympics WHERE DONE_OR_NOT_DONE=1"
cursor.execute(query)
rows = cursor.fetchall()
if len(rows)==8:
    print("All rows are populated")

    # Choosing Years
    print("Years Chosen :")
    query = "SELECT Year FROM SummerOlympics"
    result=cursor.execute(query)
    for i in result:
        print(i)

    # Calculating avrage number of atheletes

    print("Average number of Atheletes :")

    query="SELECT AVG(Athletes) FROM SummerOlympics"
    result=cursor.execute(query)

    for row in result:
        print(row)

    #Calculation 2nd query

    query="WITH CountryRanks AS (SELECT Rank_1_nation AS Country, Year FROM SummerOlympics WHERE Rank_1_nation IS NOT NULL UNION ALL SELECT Rank_2_nation AS Country, Year FROM SummerOlympics WHERE Rank_2_nation IS NOT NULL UNION ALL SELECT Rank_3_nation AS Country, Year FROM SummerOlympics WHERE Rank_3_nation IS NOT NULL) SELECT Country AS YearsInTop3 FROM CountryRanks GROUP BY Country ORDER BY YearsInTop3 DESC LIMIT 1;"

    result=cursor.execute(query)
    for row in result:
        print(row)
    