from flet import *

class ColumnCard(UserControl):
    def __init__(self, name_column, status):
        super().__init__()
        
        self.name_column = name_column # название колонки
        self.status = status # статус колонки
        self.row_station_card = []
        
        
        self.name_column_text = Text(
            value=self.name_column,
            size=10,
            color="#E0C097",
        )
        self.status_text = Text(
            value=self.status,
            size=10,
            color="#E0C097"
        )
    
    def add_station(self, row_station_card):
        self.row_station_card = row_station_card
    
    def build(self):
        return Container(
            # задний фон карточки
            height=250,
            width=300,
            bgcolor="#5C3D2E",
            border_radius=10,
            padding=0,
            margin=0,
            content=TextButton(
                style = ButtonStyle(
                    shape=RoundedRectangleBorder(radius=10),
                    ),
                content=Container(
                    content=Column(
                        controls=[
                            self.name_column_text,
                            self.status_text,
                        ],
                    )
                )
            )
        )