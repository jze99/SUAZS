import mysql.connector        

class DataBase():
    def __init__(self):
        self.config = {
          'user': 'root',
          'host': 'localhost',
          'database': 'suazs',
          'raise_on_warnings': True
        }
        
    def LoadingUsers(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # SQL-запрос для получения всех данных из таблицы
            query = "SELECT * FROM users"
            # Выполнение SQL-запроса
            cursor.execute(query)
            # Получение результатов запроса
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records
        except mysql.connector.Error as err:
            print("Ошибка:", err)
        
        
        
        
    def LoadingColumnCard(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()

            # SQL-запрос для получения всех данных из таблицы
            query = "SELECT * FROM column_card"

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
            add_data = ("INSERT INTO column_card "
               "(column_name, status) "
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
            query = "SELECT * FROM station_card WHERE name_column = %s"
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
            
    def AddDataStationCardBD(self, name_station:str, amount_of_fuel:float, maximum_fuel_capacity:float, id_fuel_type:int):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # Выполнение SQL-запроса
            add_data = ("INSERT INTO station_card "
               "(name_column, amount_of_fuel, maximum_fuel_capacity, id_type_fuel) "
               "VALUES (%s, %s, %s, %s)")
            # Данные для добавления
            data = (name_station, amount_of_fuel, maximum_fuel_capacity, id_fuel_type)
            # Выполнение SQL-запроса
            cursor.execute(add_data, data)
            # Подтверждение изменений
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)

    def AddDataTypeFuel(self, view_fuel, manufacturer, cost):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # Выполнение SQL-запроса
            add_data = ("INSERT INTO fuel_type "
               "(name_fuel, manufacturer_fuel, cost_fuel) "
               "VALUES (%s, %s, %s)")
            # Данные для добавления
            data = (view_fuel, manufacturer, cost)
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
            
    def LoadListViewFuel(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # SQL-запрос для получения всех данных из таблицы
            query = "SELECT * FROM name_fuel"
            # Выполнение SQL-запроса
            cursor.execute(query)
            # Получение результатов запроса
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def LoadListManufacturerFuel(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # SQL-запрос для получения всех данных из таблицы
            query = "SELECT * FROM fuel_manufacturer"
            # Выполнение SQL-запроса
            cursor.execute(query)
            # Получение результатов запроса
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def AddViewFuel(self, view):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # Выполнение SQL-запроса
            add_data = ("INSERT INTO name_fuel "
               "(fuel) "
               "VALUES (%s)")
            # Данные для добавления
            data = (view)
            # Выполнение SQL-запроса
            cursor.execute(add_data, data)
            # Подтверждение изменений
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
    
    def AddManufacturerFuel(self, manufacturer):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # Выполнение SQL-запроса
            add_data = ("INSERT INTO fuel_manufacturer "
               "(fuel_manufacturer) "
               "VALUES (%s)")
            # Данные для добавления
            data = (manufacturer)
            # Выполнение SQL-запроса
            cursor.execute(add_data, data)
            # Подтверждение изменений
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
    
data_base = DataBase()
