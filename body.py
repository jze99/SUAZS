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
        from settingСolumn import setting_column
        self.body_part.content = Container(setting_column)
        self.body_part.update()
    
    def build(self):
        return self.body_part

body_part = Body()