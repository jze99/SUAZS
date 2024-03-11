from flet import *

class ButtonStationCard(UserControl):
    def __init__(self, id, liters, amount_of_fuel, maximum_fuel_capacity, name_station, id_type_fuel):
        super().__init__()
        
        self.id = id
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
        self.change_button = IconButton(
            icon=icons.CHANGE_CIRCLE_OUTLINED,
            height=30,
            width=30,
            icon_size=15,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=self.UpdateStationCard
        )
        self.button_delete = IconButton(
            icon=icons.DELETE_OUTLINE,
            height=30,
            width=30,
            icon_size=15,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=self.DeleteStationCard
        )
        
        self.view_type_fuel_text = Text(
            size=10
        )
        self.manufacturer_fuel_text = Text(
            size=10
        )
        self.cost_fuel_text = Text(
            size=10,
            
        )
        
    def UpdateStationCard(self, e):
        from body import body_part
        
        body_part.OpenSetingUpdateStationCard(
            self_column=self.name_station,
            maximum_amount_of_fuel=self.maximum_fuel_capacity,
            selected_amount_of_fuel=self.amount_of_fuel,
            id_type_fuel=self.id_type_fuel,
            id=self.id
        )
    
    def DeleteStationCard(self, e):
        from dataFuel import data_base
        from body import body_part
        from heder import heder_main
        
        data_base.DeleteStationCard(id=self.id)
        
        heder_main.UpdateDataRowStation()
        body_part.OpenSetingColumnCheac(name_column=self.name_station)
        
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
        return Container(
            border_radius=border_radius.all(10),
            padding=0,
            bgcolor="#B85C38",
            content=Row(
                vertical_alignment=CrossAxisAlignment.START,
                spacing=0,
                controls=[
                    Container(
                        padding=6,
                        content = Column(
                            alignment=MainAxisAlignment.START,
                            spacing=0,
                            controls=[
                                self.view_type_fuel_text,
                                self.manufacturer_fuel_text,
                                self.cost_fuel_text
                            ]
                        )
                    ),
                    Container(
                        padding=6,
                        content=Column(
                            alignment=MainAxisAlignment.START,
                            spacing=0,

                            controls=[
                                self.percentages_text,
                                self.liters_text,
                            ]
                        )
                    ),
                    Container(
                        padding=6,
                        content=Column(
                            spacing=0,
                            controls=[
                                self.fullness_scale
                            ]
                        ),    
                    ),
                    Container(
                        
                        width=5,
                        height=75,
                        border_radius=border_radius.all(3),
                        bgcolor="#E0C097"
                    ),
                    Container(
                        padding=6,
                        content=Column(
                            alignment=MainAxisAlignment.START,
                            spacing=0,
                            controls=[
                                self.change_button,
                                self.button_delete
                            ]
                        )
                    ),
                    
                ]
            )
        )     