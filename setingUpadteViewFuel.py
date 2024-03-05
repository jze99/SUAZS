from flet import *

class SetingUpadteViewFuel(UserControl):
        
    def __init__(self):
        super().__init__()
            
        self.update_view_fuel_text = TextField(
            label="Производитель топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.seting_update_view_fuel_column = Column(
            controls=[
                Row(
                    controls=[
                        self.update_view_fuel_text
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        IconButton(
                            icon=icons.UPDATE_ROUNDED,
                            icon_size=40,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.UpdateView
                        )
                    ]
                )
            ]
        )
        
    def UpdateView(self, e):
        from dataFuel import data_base
        data_base.UpdateViewFuelData(view=self.update_view_fuel_text.value)
            
    def build(self):
        return self.seting_update_view_fuel_column