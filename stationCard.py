from flet import *

class StationCard(UserControl):
    def __init__(self, liters, amount_of_fuel, maximum_fuel_capacity, name_column):
        super().__init__()
        
        self.name_column = name_column
        self.liters = liters # количество литров
        #self.percentages # количество топлива в процентах
        #self.view = view # вид топлива
        self.amount_of_fuel = amount_of_fuel # количество топлива
        self.maximum_fuel_capacity = maximum_fuel_capacity # максимальое количество топлива
        
        
        self.view_text = Text(
            #value=self.view,
            size=10,
            color="#E0C097",
        )
        self.percentages_text = Text(
            size=10,
            value=str(int(self.percentage_of_fuel()))+"%",
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
                height=self.fuel_percentage_scale(60)
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
        
    def percentage_of_fuel(self):
        return round((self.amount_of_fuel/ self.maximum_fuel_capacity)*100,2)
    
    def fuel_percentage_scale(self, maximum_line_width):# ширина контейнера в зависимости от количества топлива 
        return (self.amount_of_fuel/self.maximum_fuel_capacity) * maximum_line_width  
    
    def build(self):
        return Container(
            border_radius=border_radius.all(10),
            padding=6,
            bgcolor="#B85C38",
            content=Row(
                controls=[
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
    
        