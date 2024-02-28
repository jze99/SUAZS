from flet import *

class InteractiveMenu(UserControl):
    def __init__(self):
        super().__init__()
        
        self.button_home = IconButton(
            icon=icons.HOME_ROUNDED,
            icon_size=30,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ),
            on_click=self.OpenMainHome
        )
        
        self.button_creating_new_type_fuel = IconButton(
            icon=icons.FORMAT_LIST_BULLETED_ADD,
            icon_size=30,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=self.OpenNewTypeFuel
        )
        
    def OpenMainHome(self, e):
        from body import body_part
        body_part.OpenMainHome()
        
    def OpenNewTypeFuel(self, e):
        from body import body_part
        body_part.OpenNewTypeFuel()
        
    def build(self):
        return Row(
            controls=[
                self.button_home,
                self.button_creating_new_type_fuel
            ]
        )
    
interactive_menu = InteractiveMenu()
    
    