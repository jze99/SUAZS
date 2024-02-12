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
        
class ColumnCardData():
    
    def __init__(self):
        self.DataCard = []
        
    def AddData(self, data):
        self.DataCard.append(data)
        
column_card_data = ColumnCardData()