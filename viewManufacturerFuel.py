from flet import *

class ManufacturerFuel(UserControl):
    
    def __init__(self, id, view):
        super().__init__()
        
        self.id = id
        self.view = view
    
    def DeleteManufacturerFuel(self, e):
        from dataFuel import data_base
        from body import body_part
        from heder import heder_main
        
        data_base.DeleteManufacturerData(_id=self.id)
        heder_main.UpdateDataRowStation()
        body_part.OpenSetingFuelManufacturer()
    
    def build(self):
        return  Row(
            controls=[
                TextButton(
                    text=self.view,
                    height=40,
                    expand=1,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ),
                     
                ),
                IconButton(
                  icon=icons.DELETE_OUTLINED,
                  icon_size=40,
                  style=ButtonStyle(
                      color="#E0C097",
                      shape=RoundedRectangleBorder(radius=10) 
                    ),
                  on_click=self.DeleteManufacturerFuel
                )
            ]
        )