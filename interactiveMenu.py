from flet import *

class InteractiveMenu(UserControl):
    def __init__(self):
        super().__init__()
        
        self.button_home = IconButton()
        
        self.button_creating_new_type_fuel = IconButton(
            icon=icons.FORMAT_LIST_BULLETED_ADD,
            icon_size=30,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
        )
        
    def build(self):
        return self.button_creating_new_type_fuel
    
interactive_menu = InteractiveMenu()
    
    