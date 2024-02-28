from flet import *

class ViewFuel(UserControl):
    
    def __init__(self, id, view):
        super().__init__()
        
        self.id = id
        self.view = view
        
    def build(self):
        return Row(
            expand=1,
            controls=[
                TextButton(
                    text=self.view,
                    height=40,
                    expand=1,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ), 
                )
            ]
        )