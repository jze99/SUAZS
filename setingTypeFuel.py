from flet import *

class SetingTypeFuel(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.type_fuel_cont = Container()
        
        self.name_fuel_text = Dropdown(
            label="Тип топлива",
            height=55,
            expand=1, 
            border_color="#B85C38",
        )
        
        self.manufacturer_fuel_text = Dropdown(
            label="Производитель топлива",
            height=55,
            expand=1, 
            border_color="#B85C38",
            
        )
        
        self.cost_fuel_text = TextField(
            label="Стоимость за литр",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.seting_new_fuel_column = Column(
            controls=[
                Row(
                    controls=[
                        self.name_fuel_text,
                        IconButton(
                            icon=icons.ADD_BOX_OUTLINED,
                            icon_size=40,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.OpenAddViewFuel
                        )
                    ]
                ),
                Row(
                    controls=[
                        self.manufacturer_fuel_text,
                        IconButton(
                            icon=icons.ADD_BOX_OUTLINED,
                            icon_size=40,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.OpenAddManufacturerFuel
                        )
                    ]
                ),
                Row(
                    controls=[self.cost_fuel_text]
                )
            ]
        )
        
        self.new_manufacturer_fuel_text = TextField(
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
        
        self.seting_new_manufacturer_fuel_column = Column(
            controls=[
                Row(
                    controls=[
                        self.new_manufacturer_fuel_text
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        IconButton(
                            icon=icons.ADD_BOX_OUTLINED,
                            icon_size=40,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.AddNewManufacturer
                        )
                    ]
                )
            ]
        )
        
        self.type_fuel_cont = Container(
            content=self.seting_new_fuel_column
        )
        
        self.LoadInfoFuel()
        
        
        
    def OpenAddViewFuel(self, e):
        from body import body_part
        body_part.OpenAddNewViewFuel()
        
    def OpenAddManufacturerFuel(self, e):
        self.type_fuel_cont.content = self.seting_new_manufacturer_fuel_column
        self.type_fuel_cont.update()
        
    def AddNewManufacturer(self, e):
        from dataFuel import data_base
        data_base.AddManufacturerFuel([self.new_manufacturer_fuel_text.value])
        self.LoadInfoFuel()
        
    def LoadInfoFuel(self):
        from dataFuel import data_base
        
        list_view = data_base.LoadListViewFuel()
        self.name_fuel_text.options.clear()
        for view in list_view:
            self.name_fuel_text.options.append(dropdown.Option(str(view[1])))
        
        list_manufacturer = data_base.LoadListManufacturerFuel()
        self.manufacturer_fuel_text.options.clear()
        for manufacturer in list_manufacturer:
            self.manufacturer_fuel_text.options.append(dropdown.Option(str(manufacturer[1])))
    
    def AddTypeFuelCard(self):
        from dataFuel import data_base
        
    def build(self):
        return self.type_fuel_cont
    
class SetingAddNewViewFuel(UserControl):
        
    def __init__(self):
        super().__init__()
            
        self.new_view_fuel_text = TextField(
            label="Вид топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.seting_new_view_fuel_column = Column(
            controls=[
                Row(
                    controls=[
                        self.new_view_fuel_text
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        IconButton(
                            icon=icons.ADD_BOX_OUTLINED,
                            icon_size=40,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.AddNewView
                        )
                    ]
                )
            ]
        )
        
    def AddNewView(self, e):
        from dataFuel import data_base
        data_base.AddViewFuel([self.new_view_fuel_text.value])
            
    def build(self):
        return self.seting_new_view_fuel_column