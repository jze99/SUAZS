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
            on_click=self.OpenMainHome,
            tooltip="Домашная странца"
        )
        
        self.button_type_fuel = Row(
            spacing=0,
            controls=[
                Text(
                    value="Тип Топлива",
                    size=10
                ),
                IconButton(
                    icon=icons.FORMAT_LIST_BULLETED_ADD,
                    icon_size=30,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ), 
                    on_click=self.OpenListTypeFuel,
                    tooltip="Тип топлива"
                )
            ]
        )
        
        self.button_view_fuel = Row(
            spacing=0,
            controls=[
                Text(
                    size=10,
                    value="Виды топлива:"
                ),
                IconButton(
                    icon=icons.TABLE_ROWS,
                    icon_size=30,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ), 
                    on_click=self.OpenListViewFuel,
                    tooltip="Виды топлива"
                )
            ]
        )
        
        self.button_manufacturer_fuel = Row(
            spacing=0,
            controls=[
                Text(
                    size=10,
                    value="Производители топлива:"
                ),
                IconButton(
                    icon=icons.PEOPLE_ALT_OUTLINED,
                    icon_size=30,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ), 
                    on_click=self.OpenListManufacturerFuel,
                    tooltip="Производители топлива"
                )
            ]
        )
        
    def OpenListViewFuel(self, e):
        from body import body_part
        body_part.OpenSetingFuelView()
        
    def OpenListManufacturerFuel(self, e):
        from body import body_part
        body_part.OpenSetingFuelManufacturer()
        
    def OpenMainHome(self, e):
        from body import body_part
        body_part.OpenMainHome()
        
    def OpenListTypeFuel(self, e):
        from body import body_part
        body_part.OpenListTypeFuel()
        
    def build(self):
        return Row(
            scroll=True,
            spacing=3,
            controls=[
                self.button_home,
                self.button_type_fuel,
                self.button_view_fuel,
                self.button_manufacturer_fuel
            ]
        )
    
interactive_menu = InteractiveMenu()
    
    