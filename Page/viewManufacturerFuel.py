from flet import *

class ManufacturerFuel(UserControl):
    
    def __init__(self, id, view):
        super().__init__()
        
        self.id = id
        self.manufacturer = view
        
    def UpdateManufacturerFuel(self, e):
        from OssnovElements.body import body_part
        body_part.OpenSetingUpdateManufacturerFuel(_id=self.id, manufacturer=self.manufacturer)
    
    def DeleteManufacturerFuel(self, e):
        from dataFuel import data_base
        from OssnovElements.body import body_part
        from OssnovElements.heder import heder_main
        
        data_base.DeleteManufacturerData(_id=self.id)
        heder_main.Aplay()
        body_part.OpenSetingFuelManufacturer()
    
    def build(self):
        return  Row(
            controls=[
                TextButton(
                    text=self.manufacturer,
                    height=40,
                    expand=1,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ),
                    on_click=self.UpdateManufacturerFuel
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