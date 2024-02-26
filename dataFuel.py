import mysql.connector


class DataFuel():
    def __init__(self):
        self.colonfuel
        
class DataColumnFuel():
    def __init__(self, name_column, liters, percentages, view, status):
        self.name_column = name_column
        self.liters = liters
        self.percentages = percentages
        self.view = view
        self.status = status         

class DataBase():
    def __init__(self):
        self.config = {
          'user': 'root',
          'host': 'localhost',
          'database': 'sazs',
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
    
    def AddDataColumnCard(self, name, status):
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

data_base = DataBase()

        
class ColumnCardData():
    
    def __init__(self):
        self.DataCard = []
        
    def AddDataBD(self, data):
        data_base.AddDataColumnCard(data.name_column, data.status)
        
    def AddData(self, data):
        self.DataCard.append(data)
        self.AddDataBD(data)
        
        
class StationCardData():
    
    def __init__(self):
        self.DataStation = []
        
    def AddData(self, data):
        self.DataStation.append(data)
        
station_card_data = StationCardData()
column_card_data = ColumnCardData()