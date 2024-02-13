from flet import *

class SetingStation(UserControl):
    def __init__(self, self_column):
        
        super().__init__()
        
        self.column_card = self_column
        
        self.selected_amount_of_fuel = TextField(# выбранный объем топлива
            label="Выброное к. топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="0",
            text_size=16,
            multiline=False,
            expand=1,
            on_change=self.UpdatingFuelValueText
        )
        self.maximum_amount_of_fuel = TextField(
            label="Макс. к. топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="100",
            text_size=16,
            multiline=False,
            expand=1,
            on_change=self.UpdateDataSliderText   
        )
        self.slider_toplivo = Slider(
            height=40,
            expand=1,
            max=100,
            min=0,
            round=2,
            active_color="#B85C38",
            value=0,
            on_change=self.UpdatingCurrentFuelSlider
        )
        self.type_of_fuel = Dropdown(
            label="Топливо",
            height=55,
            expand=1, 
        )
        
    def UpdatingCurrentFuelSlider(self, e):
        self.selected_amount_of_fuel.value = round(self.slider_toplivo.value, 0)
        self.selected_amount_of_fuel.update()
   
    def UpdatingFuelValueText(self, e):
        if self.maximum_amount_of_fuel.value != '':
            self.slider_toplivo.value = float(self.selected_amount_of_fuel.value) 
        elif self.maximum_amount_of_fuel.value == '':
            self.slider_toplivo.value = 0
        self.slider_toplivo.update()
    
    def UpdateDataSliderText(self, e):
        if self.maximum_amount_of_fuel.value != '':
            self.slider_toplivo.max = float(self.maximum_amount_of_fuel.value) 
        elif self.maximum_amount_of_fuel.value == '':
            self.slider_toplivo.max = 0
        self.slider_toplivo.update()
        
    def AddStationOfcolumn(self, e):
        from stationCard import StationCard
        self.column_card.row_station_card.controls.append(Container(StationCard(liters=self.selected_amount_of_fuel.value,
                                                                                )))
        self.column_card.row_station_card.update()
    
    def build(self):
        return Column(
            controls=[
                Row(
                    controls=[
                        self.selected_amount_of_fuel,
                        self.maximum_amount_of_fuel,
                    ]
                ),
                Row(
                    controls=[
                        self.slider_toplivo
                    ]
                ),
                Row(
                    controls=[
                        self.type_of_fuel
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        IconButton(
                            icons.ADD_BOX_OUTLINED,
                            icon_size=30,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.AddStationOfcolumn
                        ),
                    ]
                )
            ]
        )