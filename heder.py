from flet import *

class Heder(UserControl):
  def __init__(self):
    super().__init__()
    
    self.add_fueld_card_button = IconButton(
      icon=icons.ADD,
      icon_size=40,
      style=ButtonStyle(
          color="#E0C097",
          shape=RoundedRectangleBorder(radius=10) 
      ),
      on_click=self.AddColumnCardBodySetting
    )
    self.row_column_card = Row(
      scroll=True,
      alignment=CrossAxisAlignment.END,
      #height=140,
      auto_scroll=True,
      controls=[
          self.add_fueld_card_button,
      ],
    )
    
    self.LoadingDataСolumn()
    
  def LoadingDataСolumn(self):
        from dataFuel import data_base
        from columnCard import ColumnCard
        from stationCard import StationCard
        
        column_data = data_base.LoadingColumnCard()
        
        for colm in column_data:
          column_card = ColumnCard(
            name_column=colm[1],
            status=colm[2]
          )
          
          self.row_column_card.controls.insert(len(self.row_column_card.controls)-1, Card(content=column_card))
          
          station_card = data_base.LoadingStationCard(column_name=colm[1])
          if station_card: 
            for stat in station_card:
              column_card.row_station_card.controls.append(
                Container(
                  StationCard(
                    liters=stat[2],
                    amount_of_fuel=stat[2],
                    maximum_fuel_capacity=stat[3],
                    name_station=stat[1],
                    id_type_fuel=[4]
                  )
                )
              )
  
  def AddColumnCardBodySetting(self, e):
    from body import body_part
    body_part.OpenSettingColumn()
    
  def build(self):
    return self.row_column_card
  
heder_main = Heder()