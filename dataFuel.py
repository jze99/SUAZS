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
            add_data = ("INSERT INTO type_fuel "
               "(view_fuel, manufacturer_fuel, cost_fuel) "
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
            query = "SELECT * FROM type_fuel"
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
            query = "SELECT * FROM view_fuel"
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
            query = "SELECT * FROM manufacturer_fuel"
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
            add_data = ("INSERT INTO view_fuel "
               "(view) "
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
            add_data = ("INSERT INTO manufacturer_fuel "
               "(manufacturer) "
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
    
    def LoadingTypeFuelId(self, _id:str):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "SELECT * FROM type_fuel WHERE id = %s"
            cursor.execute(query, (_id,))
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            if rows:
                return rows
            else:
                print("нет данных")
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def LoadListFuelType(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # SQL-запрос для получения всех данных из таблицы
            query = "SELECT * FROM type_fuel"
            # Выполнение SQL-запроса
            cursor.execute(query)
            # Получение результатов запроса
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records
        except mysql.connector.Error as err:
            print("Ошибка:", err)
    
    def DeleteViewData(self, _id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "DELETE FROM view_fuel WHERE id = %s"
            cursor.execute(query, (_id,))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)

    def DeleteManufacturerData(self, _id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "DELETE FROM manufacturer_fuel WHERE id = %s"
            cursor.execute(query, (_id,))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def DeleteFuelTypeData(self, _id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "DELETE FROM type_fuel WHERE id = %s"
            cursor.execute(query, (_id,))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def UpdateViewFuelData(self, view, _id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "UPDATE view_fuel SET view = %s WHERE id= %s"
            cursor.execute(query, (view, _id))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def UpdateManufacturerFuelData(self, manufacturer, _id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "UPDATE manufacturer_fuel SET manufacturer = %s WHERE id= %s"
            cursor.execute(query, (manufacturer, _id))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def UpdateTypeFuelData(self,view, manufacturer, cost, _id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "UPDATE type_fuel SET view_fuel = %s, manufacturer_fuel = %s, cost_fuel = %s WHERE id = %s"
            cursor.execute(query, (view, manufacturer, cost, _id))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)

    def LoadListStationColumnCheac(self, name_column):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # SQL-запрос для получения всех данных из таблицы по указанному столбцу
            query = "SELECT * FROM station_card WHERE name_column = %s"
            # Выполнение SQL-запроса с передачей параметра
            cursor.execute(query, (name_column,))
            # Получение результатов запроса
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records
        except mysql.connector.Error as err:
            print("Ошибка:", err)
    
    def LoadListStationTypeFuelCheac(self, id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # SQL-запрос для получения всех данных из таблицы по указанному столбцу
            query = "SELECT * FROM type_fuel WHERE id = %s"
            # Выполнение SQL-запроса с передачей параметра
            cursor.execute(query, (id,))
            # Получение результатов запроса
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def DeleteStationCard(self, id):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "DELETE FROM station_card WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def UpdateStationCard(self, id, amount_of_fuel, maximum_fuel_capacity, id_type_fuel):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            query = "UPDATE station_card SET amount_of_fuel = %s, maximum_fuel_capacity = %s, id_type_fuel = %s WHERE id = %s"
            cursor.execute(query, (amount_of_fuel, maximum_fuel_capacity, id_type_fuel, id))
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def AddCheacBD(self, cost, cost_per_liter, view_fuel, manufacturer_fuel, data_t, time, liters, name_column):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # Выполнение SQL-запроса
            add_data = ("INSERT INTO receipts "
                        "(cost, cost_per_liter, view_fuel, manufacturer_fuel, data, time, liters, column_name) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
            # Данные для добавления
            data = (cost, cost_per_liter, view_fuel, manufacturer_fuel, data_t, time, liters, name_column)
            # Выполнение SQL-запроса
            cursor.execute(add_data, data)
            # Подтверждение изменений
            conn.commit()
            # Закрытие соединения
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print("Ошибка:", err)
            
    def LoadListDataReceipts(self):
        try:
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            # SQL-запрос для получения всех данных из таблицы по указанному столбцу
            query = "SELECT * FROM receipts"
            # Выполнение SQL-запроса с передачей параметра
            cursor.execute(query)
            # Получение результатов запроса
            records = cursor.fetchall()
            cursor.close()
            conn.close()
            return records
        except mysql.connector.Error as err:
            print("Ошибка:", err)
    
data_base = DataBase()
