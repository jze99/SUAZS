from flet import *

class ColumnCard(UserControl):
    def __init__(self, name_column, statusC):
        super().__init__()
        
        
        self.name_column = name_column # название колонки
        self.statusC = statusC # статус колонки
        self.row_station_card = Row()
        
        self.name_column_text = Text(
            value=self.name_column,
            size=10,
            color="#E0C097",
        )
        
        self.addBox = IconButton(
            icon=icons.ADD_BOX_OUTLINED,
            icon_size=30,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=self.AddStation,
        )
    
    def AddStation(self, e):
        from OssnovElements.body import body_part
        body_part.OpenSettingStation(_self= self)
        
    def OpenColumnChec(self, e):
        from OssnovElements.body import body_part
        body_part.OpenSetingColumnCheac(name_column=self.name_column)
    
    def build(self):
        import Person
        if Person.Persona.stat != "admin":
            self.addBox.visible = False
        
        return Container(
            # задний фон карточки
            bgcolor="#5C3D2E",
            border_radius=10,
            padding=0,
            margin=0,
            content=TextButton(
                style = ButtonStyle(
                    shape=RoundedRectangleBorder(radius=10),
                    ),
                on_click=self.OpenColumnChec,
                content=Container(
                    content=Column(
                        alignment=MainAxisAlignment.START,
                        controls=[
                            self.name_column_text,
                            self.row_station_card,
                            Row(
                                alignment=MainAxisAlignment.END,
                                controls=[
                                    self.addBox
                                ],
                            ),
                        ],
                    )
                )
            )
        )