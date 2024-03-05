from flet import *

class SetingAddNewManufacturerFuel(UserControl):
        
    def __init__(self):
        super().__init__()
            
        self.new_manufacturer_fuel_text = TextField(
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
        
        self.seting_new_manufacturer_fuel_column = Column(
            controls=[
                Row(
                    controls=[
                        self.new_manufacturer_fuel_text
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
                            on_click=self.AddNewManufacturer
                        )
                    ]
                )
            ]
        )
        
    def AddNewManufacturer(self, e):
        from dataFuel import data_base
        data_base.AddManufacturerFuel([self.new_manufacturer_fuel_text.value])
            
    def build(self):
        return self.seting_new_manufacturer_fuel_column