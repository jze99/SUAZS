from flet import *

class SetingAddNewViewFuel(UserControl):
        
    def __init__(self):
        super().__init__()
            
        self.new_view_fuel_text = TextField(
            label="Вид топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.seting_new_view_fuel_column = Column(
            controls=[
                Row(
                    controls=[
                        self.new_view_fuel_text
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        IconButton(
                            icon=icons.ADD_BOX_OUTLINED,
                            icon_size=40,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.AddNewView
                        )
                    ]
                )
            ]
        )
        
    def AddNewView(self, e):
        from dataFuel import data_base
        data_base.AddViewFuel([self.new_view_fuel_text.value])
            
    def build(self):
        return self.seting_new_view_fuel_column