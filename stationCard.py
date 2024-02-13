from flet import *

class StationCard(UserControl):
    def __init__(self, liters, percentages, view, amount_of_fue, maximum_fuel_capacity):
        super().__init__()
        
        self.liters = liters # количество литров
        self.percentages = percentages # количество топлива в процентах
        self.view = view # вид топлива
        self.amount_of_fue = amount_of_fue # количество топлива
        self.maximum_fuel_capacity = maximum_fuel_capacity # максимальое количество топлива
        
        
        self.view_text = Text(
            value=self.view,
            size=10,
            color="#E0C097",
        )
        self.percentages_text = Text(
            value=self.percentages,
            size=10,
            color="#E0C097"
        )
        self.liters_text = Text(
            value=self.liters,
            size=10,
            color="#E0C097"
        )
        self.fullness_scale = Container(
            content=Container,
        )
        
    def percentage_of_fuel(self):
        return round((self.amount_of_fuel/ self.maximum_fuel_capacity)*100,2)
    
    def fuel_percentage_scale(self, maximum_line_width):# ширина контейнера в зависимости от количества топлива 
        return (self.amount_of_fuel/self.maximum_fuel_capacity) * maximum_line_width  
    
    def build(self):
        return Container(
            height=50,
            width=50,
            bgcolor="#000000"
        )       
    
        