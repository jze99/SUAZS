from flet import *

class SetingAddDataTypeFuel(UserControl):
    
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
                            on_click=self.AddDataFuelType
                        )
                    ]
                )
            ]
        )
        
        self.type_fuel_cont = Container(
            content=self.seting_new_fuel_column
        )
        
        self.LoadInfoFuel()
    
    def AddDataFuelType(self, e):
        from dataFuel import data_base
        try:           
            data_base.AddDataTypeFuel(
                view_fuel=self.name_fuel_text.value,
                manufacturer=self.manufacturer_fuel_text.value,
                cost=float(self.cost_fuel_text.value)
            )
        except ValueError:
            self.cost_fuel_text.value = "Только цифры"
            self.cost_fuel_text.update()
        
    def OpenAddViewFuel(self, e):
        from OssnovElements.body import body_part
        body_part.OpenAddNewViewFuel()
        
    def OpenAddManufacturerFuel(self, e):
        from OssnovElements.body import body_part
        body_part.OpenAddNewManufacturerFuel()
        
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
        if list_manufacturer:
            for manufacturer in list_manufacturer:
               self.manufacturer_fuel_text.options.append(dropdown.Option(str(manufacturer[1])))
        
    def build(self):
        return self.type_fuel_cont
    