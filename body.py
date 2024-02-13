from flet import *

class Body(UserControl):
    def __init__(self):
        super().__init__()
        
        self.column_name = TextField(
            label="Название колонки",
            height=60,
            expand = 1,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
        )
        
        self.body_part = Container(
            bgcolor="#5C3D2E",
            border_radius=border_radius.all(3),
            padding=10,
        )
    
    def OpenSettingColumn(self):
        from settingСolumn import SettingColumn
        self.body_part.content = Container(SettingColumn())
        self.body_part.update()
        
    def OpenSettingStation(self, _self):
        from setingStation import SetingStation
        self.body_part.content = Container(SetingStation(self_column=_self))
        self.body_part.update()
    
    def build(self):
        return self.body_part

body_part = Body()