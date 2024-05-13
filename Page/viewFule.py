from flet import *

class ViewFuel(UserControl):
    
    def __init__(self, id:int, view):
        super().__init__()
        
        self.id = id
        self.view = view
    
    def UpdateViewFuel(self, e):
        from OssnovElements.body import body_part
        body_part.OpenSetingUpdateViewFuel(_id=self.id, view=self.view)
        
    
    def DeleteViewFuel(self, e):
        from dataFuel import data_base
        from OssnovElements.body import body_part
        from OssnovElements.heder import heder_main
        
        data_base.DeleteViewData(_id=self.id)
        heder_main.Aplay()
        body_part.OpenSetingFuelView()
    
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
                    on_click=self.UpdateViewFuel
                ),
                IconButton(
                  icon=icons.DELETE_OUTLINED,
                  icon_size=40,
                  style=ButtonStyle(
                      color="#E0C097",
                      shape=RoundedRectangleBorder(radius=10) 
                    ),
                  on_click=self.DeleteViewFuel
                )
            ]
        )
                        