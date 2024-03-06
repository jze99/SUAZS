from flet import *

class ViewFuelType(UserControl):
    def __init__(self, _id, view, manufacturer, cost):
        super().__init__()
        
        self.id = _id
        self.view = view
        self.manufacturer = manufacturer
        self.cost = cost
        
    def UpdateTypeFuel(self,e):
        from body import body_part
        body_part.OpenSetingUpdateTypeFuel(
            _id=self.id,
            view=self.view,
            manufacturer=self.manufacturer,
            cost=self.cost
        )
    
    def DeleteTypeFuel(self, e):
        from dataFuel import data_base
        from body import body_part
        from heder import heder_main
        
        data_base.DeleteFuelTypeData(_id=self.id)
        heder_main.UpdateDataRowStation()
        body_part.OpenListTypeFuel()
    
    def build(self):
        return Row(
            controls=[
                TextButton(
                    text=str(self.view)+": "+str(self.manufacturer)+": "+str(self.cost),
                    height=40,
                    expand=1,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ),
                    on_click=self.UpdateTypeFuel
                ),
                IconButton(
                  icon=icons.DELETE_OUTLINED,
                  icon_size=40,
                  style=ButtonStyle(
                      color="#E0C097",
                      shape=RoundedRectangleBorder(radius=10) 
                    ),
                  on_click=self.DeleteTypeFuel
                )
            ]
        )