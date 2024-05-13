from flet import *

class TypeFuel(UserControl):
    
    def __init__(self, name, manufacturer, cost):
        super().__init__()
        self.name_fuel = Text(
            size=10,
            value=name,
            weight=100
        ) 
        self.manufacturer_fuel = Text(
            size=10,
            value=manufacturer,
            weight=100
        )
        self.cost_fuel = Text(
            size=10,
            value=cost,
            weight=100
        )
        
    def build(self):
        return Container(
            content=Column(
                controls=[
                    Row(
                        controls=[
                            self.name_fuel
                        ]
                    ),
                    Row(
                        controls=[
                            self.manufacturer_fuel
                        ]
                    ),
                    Row(
                        controls=[
                            self.cost_fuel
                        ]
                    )
                ]
            )
        )