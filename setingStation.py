from flet import *

class SetingStation(UserControl):
    def __init__(self, self_column):
        
        super().__init__()
        
        self.column_card = self_column
        
        self.optionsSelectTupeFuelDropdown = []
        
        self.selected_type_fuel = None
        
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
            border_color="#B85C38",
            on_change=self.ChoosingSheetWithTypeFuel
        )
        self.LoadListFuel()
        
    def LoadListFuel(self):# Загруска данных
        from dataFuel import data_base
        from optionsSelectTupeFuelDropdown import OptionsSelectTupeFuelDropdown
        
        list_fuel = data_base.LoadListFuel()
        self.type_of_fuel.options.clear()
        
        if list_fuel:
            for i_list, _list in enumerate(list_fuel):

                self.optionsSelectTupeFuelDropdown.append(OptionsSelectTupeFuelDropdown(
                    _id = _list[0],
                    name_fuel = _list[1],
                    manufacturer_fuel = _list[2],
                    cost_fuel = _list[3]
                ))

                self.type_of_fuel.options.append(self.optionsSelectTupeFuelDropdown[i_list].ReturnData())
            
    def ChoosingSheetWithTypeFuel(self, e):# Выбор листа с видом топлива 
        for list_fuel_type in self.optionsSelectTupeFuelDropdown:
            if(str(list_fuel_type.name_fuel) + ": " + str(list_fuel_type.manufacturer_fuel) + ": " + str(list_fuel_type.cost_fuel)) == self.type_of_fuel.value:
                self.selected_type_fuel = list_fuel_type
                pass
        
    def UpdatingCurrentFuelSlider(self, e):# Обновление данных слайнера
        self.selected_amount_of_fuel.value = round(self.slider_toplivo.value, 0)
        self.selected_amount_of_fuel.update()
   
    def UpdatingFuelValueText(self, e):# Обновление данных текста
        if self.maximum_amount_of_fuel.value != '':
            self.slider_toplivo.value = float(self.selected_amount_of_fuel.value) 
        elif self.maximum_amount_of_fuel.value == '':
            self.slider_toplivo.value = 0
        self.slider_toplivo.update()
    
    def UpdateDataSliderText(self, e):# Обновление данных 
        if self.maximum_amount_of_fuel.value != '':
            self.slider_toplivo.max = float(self.maximum_amount_of_fuel.value) 
        elif self.maximum_amount_of_fuel.value == '':
            self.slider_toplivo.max = 0
        self.slider_toplivo.update()
        
    def AddStationOfcolumn(self, e):# Добавление станции
        from stationCard import StationCard
        from dataFuel import data_base
        
        data_base.AddDataStationCardBD( # Добовление в базу 
            amount_of_fuel = float(self.selected_amount_of_fuel.value),
            maximum_fuel_capacity = float(self.maximum_amount_of_fuel.value),
            name_station = self.column_card.name_column,
            id_fuel_type = self.selected_type_fuel._id
        )
        
        stant_card = StationCard(
            liters=self.selected_amount_of_fuel.value,
            amount_of_fuel=float(self.selected_amount_of_fuel.value),
            maximum_fuel_capacity=float(self.maximum_amount_of_fuel.value),
            name_station=self.column_card.name_column,
            id_type_fuel=self.selected_type_fuel._id
        )
        stant_card.LoadTypeFuelId()   
        
        self.column_card.row_station_card.controls.append( # Добовление в интерфейс 
            Container(
                stant_card
            )
        )
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