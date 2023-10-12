import mysql.connector

class DB:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="abc",
                    password="password"
                )
#print(mydb)
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute("use flight")
        except:
            pass
    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(Destination) FROM flight
        UNION
        SELECT DISTINCT(Source) FROM flight
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city


    def fetch_all_flights(self,source,destination):

        self.mycursor.execute("""
                SELECT Airline,Route,Price,Date_of_Journey FROM flight
                WHERE Source = '{}' AND Destination = '{}'
                """.format(source,destination))

        data = self.mycursor.fetchall()

        return data
    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        SELECT Airline,COUNT(*) FROM flight
        GROUP BY Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency
