from flet import *

class SetingUpadteManufacturerFuel(UserControl):
        
    def __init__(self):
        super().__init__()    
        
        self.update_manufacturer_fuel_text = TextField(
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
        
        self.seting_update_manufacturer_fuel_column = Column(
            controls=[
                Row(
                    controls=[
                        self.update_manufacturer_fuel_text
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
        
    def LoadData(self, _id, manufacturer):
        self._id = _id
        self.manufacturer = manufacturer
        
        self.update_manufacturer_fuel_text.value = self.manufacturer
        self.update_manufacturer_fuel_text.update()
        
    def UpdateView(self, e):
        from dataFuel import data_base
        from OssnovElements.body import body_part
        from OssnovElements.heder import heder_main
        
        data_base.UpdateManufacturerFuelData(manufacturer=self.update_manufacturer_fuel_text.value, _id=self._id)
        
        body_part.OpenSetingFuelManufacturer()   
        
        heder_main.Aplay()
            
    def build(self):
        return self.seting_update_manufacturer_fuel_column