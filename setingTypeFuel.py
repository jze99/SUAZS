from flet import *

class SetingTypeFuel(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.type_fuel_column = Column()
        
        self.name_fuel_text = TextField(
            label="Тип топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.manufacturer_fuel_text = TextField(
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
                    controls=[self.name_fuel_text]
                ),
                Row(
                    controls=[self.manufacturer_fuel_text]
                ),
                Row(
                    controls=[self.cost_fuel_text]
                )
            ]
        )
    
    def AddTypeFuelCard(self):
        from dataFuel import data_base
        
    def build(self):
        return self.seting_new_fuel_column