import mysql.connector        

class DataBase():
    def __init__(self):
        self.config = {
          'user': 'root',
          'host': 'localhost',
          'database': 'sauzs',
          'raise_on_warnings': True
        }
        
    def LoadingColumnCard(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()

            # SQL-запрос для получения всех данных из таблицы
            query = "SELECT * FROM columncards"

            # Выполнение SQL-запроса
            cursor.execute(query)

            # Получение результатов запроса
            records = cursor.fetchall()

            cursor.close()
            conn.close()

            return records

        except mysql.connector.Error as err:
            print("Ошибка:", err)
    
    def AddDataColumnCardBD(self, name:str, status:bool):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()

            # Выполнение SQL-запроса
            add_data = ("INSERT INTO columncards "
               "(Name, Status) "
               "VALUES (%s, %s)")

            # Данные для добавления
            data = (name, status)

            # Выполнение SQL-запроса
            cursor.execute(add_data, data)

            # Подтверждение изменений
            conn.commit()

            # Закрытие соединения
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
            
    def LoadingStationCard(self, column_name:str):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()


            query = "SELECT * FROM stationcard WHERE name_station = %s"
            cursor.execute(query, (column_name,))
            rows = cursor.fetchall()
            
            cursor.close()
            conn.close()
            
            if rows:
                return rows
            else:
                print("нет данных")

        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def AddDataStationCardBD(self, name_station:str, amount_of_fuel:float, maximum_fuel_capacity:float):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()

            # Выполнение SQL-запроса
            add_data = ("INSERT INTO stationcard "
               "(name_station, amount_of_fuel, maximum_fuel_capacity) "
               "VALUES (%s, %s, %s)")

            # Данные для добавления
            data = (name_station, amount_of_fuel, maximum_fuel_capacity)

            # Выполнение SQL-запроса
            cursor.execute(add_data, data)

            # Подтверждение изменений
            conn.commit()

            # Закрытие соединения
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def AddDataTypeFuelBD(self, name_fuel:str, manufacturer_fuel:str, cost_fuel:float):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()

            # Выполнение SQL-запроса
            add_data = ("INSERT INTO type_fuel "
               "(name_station, amount_of_fuel, maximum_fuel_capacity) "
               "VALUES (%s, %s, %s)")

            # Данные для добавления
            data = (name_fuel, manufacturer_fuel, cost_fuel)

            # Выполнение SQL-запроса
            cursor.execute(add_data, data)

            # Подтверждение изменений
            conn.commit()

            # Закрытие соединения
            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            print("Ошибка:", err)

    def LoadListFuel(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()

            # SQL-запрос для получения всех данных из таблицы
            query = "SELECT * FROM fuel_type"

            # Выполнение SQL-запроса
            cursor.execute(query)

            # Получение результатов запроса
            records = cursor.fetchall()

            cursor.close()
            conn.close()

            return records

        except mysql.connector.Error as err:
            print("Ошибка:", err)
    
data_base = DataBase()
