from flet import *

class StationCard(UserControl):
    def __init__(self, liters, amount_of_fuel, maximum_fuel_capacity, name_station, id_type_fuel):
        super().__init__()
        self.name_station = name_station
        self.liters = liters # количество литров
        #self.percentages # количество топлива в процентах
        
        self.id_type_fuel = id_type_fuel # id fuel_type
        self.amount_of_fuel = amount_of_fuel # количество топлива
        self.maximum_fuel_capacity = maximum_fuel_capacity # максимальое количество топлива
        
        self.percentages_text = Text(
            size=10,
            value=str(int(self.PercentageOfFuel()))+"%",
            color="#E0C097"
        )
        self.liters_text = Text(
            value=str(int(self.liters))+"Л", 
            size=10,
            color="#E0C097"
        )
        self.fullness_scale = Container(
            height=60,
            width=15,
            border_radius=border_radius.all(3),
            bgcolor="#5C3D2E",
            alignment=alignment.bottom_center,
            content=Container(
                width=15,
                border_radius=border_radius.all(3),
                bgcolor="#E0C097",
                height=self.FuelPercentageScale(60)
            )
        )
        self.button_delete = IconButton(
            icon=icons.DELETE_OUTLINE,
            icon_size=40,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
        )
        
        self.view_type_fuel_text = Text(
            size=10
        )
        self.manufacturer_fuel_text = Text(
            size=10
        )
        self.cost_fuel_text = Text(
            size=10
        )
        
    def LoadTypeFuelId(self):
        from dataFuel import data_base
        self.selected_type_fuel = data_base.LoadingTypeFuelId(self.id_type_fuel)
        self.view_type_fuel = self.selected_type_fuel[0][1]
        self.manufacturer_fuel = self.selected_type_fuel[0][2]
        self.cost_fuel = self.selected_type_fuel[0][3]
        
        self.view_type_fuel_text.value = self.view_type_fuel
        self.manufacturer_fuel_text.value = self.manufacturer_fuel
        self.cost_fuel_text.value = str(self.cost_fuel)
        pass
        
    def PercentageOfFuel(self):
        return round((self.amount_of_fuel/ self.maximum_fuel_capacity)*100,2)
    
    def FuelPercentageScale(self, maximum_line_width):# ширина контейнера в зависимости от количества топлива 
        return (self.amount_of_fuel/self.maximum_fuel_capacity) * maximum_line_width  
    
    def build(self):
        import Person
        if Person.Persona.stat != "admin":
            self.button_delete.visible = False
        return Container(
            border_radius=border_radius.all(10),
            padding=6,
            bgcolor="#B85C38",
            content=Row(
                controls=[
                    Column(
                        controls=[
                            self.view_type_fuel_text,
                            self.manufacturer_fuel_text,
                            self.cost_fuel_text
                        ]
                    ),
                    Column(
                        controls=[
                            self.percentages_text,
                            self.liters_text,
                        ]
                    ),
                    Column(
                        controls=[
                            self.fullness_scale
                        ]
                    )
                ]
            )
        )     
    
        