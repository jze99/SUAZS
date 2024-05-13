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
        
        self.button_people = Row(
            spacing=0,
            controls=[
                Text(
                    size=10,
                    value="сотрудники:"
                ),
                IconButton(
                    icon=icons.PEOPLE_ALT_OUTLINED,
                    icon_size=30,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ), 
                    on_click=self.OpenPeople,
                    tooltip="сотрудники"
                )
            ]
        )
        
        self.button_new_people = Row(
            spacing=0,
            controls=[
                Text(
                    size=10,
                    value="создать сотрудника:"
                ),
                IconButton(
                    icon=icons.PEOPLE_ALT_OUTLINED,
                    icon_size=30,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ), 
                    on_click=self.OpenNewPeople,
                    tooltip="сотрудники"
                )
            ]
        )
        
        self.exit = Row(
            spacing=0,
            controls=[
                Text(
                    size=10,
                    value="выйти"
                ),
                IconButton(
                    icon=icons.EXIT_TO_APP,
                    icon_size=30,
                    style=ButtonStyle(
                        color="#E0C097",
                        shape=RoundedRectangleBorder(radius=10) 
                    ), 
                    on_click=self.Exit,
                    tooltip="выход"
                )
            ]
        )
        
    def OpenListViewFuel(self, e):
        from OssnovElements.body import body_part
        body_part.OpenSetingFuelView()
        
    def OpenListManufacturerFuel(self, e):
        from OssnovElements.body import body_part
        body_part.OpenSetingFuelManufacturer()
        
    def OpenMainHome(self, e):
        from OssnovElements.body import body_part
        body_part.OpenMainHome()
        
    def OpenListTypeFuel(self, e):
        from OssnovElements.body import body_part
        body_part.OpenListTypeFuel()
        
    def OpenPeople(self,e):
        from OssnovElements.body import body_part
        body_part.OpenPeopleList()

    def OpenNewPeople(self, e):
        from OssnovElements.body import body_part
        body_part.OpenNewPeopl()
        
    def Exit(self,e):
        from OssnovElements.body import body_part
        body_part.Exit()
        
    def build(self):
        import Person
        if Person.Persona.stat == "admin":
            return Row(
                scroll=True,
                spacing=3,
                controls=[
                    self.button_home,
                    self.button_type_fuel,
                    self.button_view_fuel,
                    self.button_manufacturer_fuel,
                    self.button_people,
                    self.button_new_people,
                    self.exit
                ]
            )
        if Person.Persona.stat != "admin":
            return Row(
                scroll=True,
                spacing=3,
                controls=[
                    self.button_home,
                    self.exit
                ]
            )
    
interactive_menu = InteractiveMenu()
    
    