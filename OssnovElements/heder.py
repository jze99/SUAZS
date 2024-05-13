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
      controls=[],
    )
    
  def LoadingDataСolumn(self):
    from dataFuel import data_base
    from Page.columnCard import ColumnCard
    from Page.stationCard import StationCard

    column_data = data_base.LoadingColumnCard()

    if column_data == None:
      return
    
    for colm in column_data:
      column_card = ColumnCard(
        name_column=colm[1],
        statusC=colm[2],
      )
      self.row_column_card.controls.insert(len(self.row_column_card.controls)-1, Card(content=column_card))
      station_card = data_base.LoadingStationCard(column_name=colm[1])
      if station_card: 
        for stat in station_card:
          stat_card = StationCard(
            liters=stat[2],
            amount_of_fuel=stat[2],
            maximum_fuel_capacity=stat[3],
            name_station=stat[1],
            id_type_fuel=stat[4],
          )
          column_card.row_station_card.controls.append(
            Container(
              stat_card
            )
          )
          stat_card.LoadTypeFuelId()
    
  def UpdateDataRowStation(self):
    self.row_column_card.controls.clear()
    self.LoadingDataСolumn()
    import Person
    if Person.Persona.stat == "admin":
      self.row_column_card.controls.append(self.add_fueld_card_button)
    
  def Aplay(self):
    self.UpdateDataRowStation()
    self.row_column_card.update()
            
  
  def AddColumnCardBodySetting(self, e):
    from OssnovElements.body import body_part
    body_part.OpenSettingColumn()
    
  def build(self):
    self.UpdateDataRowStation()
    return self.row_column_card

heder_main = Heder()