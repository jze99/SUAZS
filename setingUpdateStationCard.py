from flet import *

class SetingUpdateStation(UserControl):
    def __init__(self, self_column, maximum_amount_of_fuel, selected_amount_of_fuel, id_type_fuel, id):
        
        super().__init__()
        
        self.column_card = self_column
        self.maximum_amount_of_fuel = maximum_amount_of_fuel
        self.selected_amount_of_fuel = selected_amount_of_fuel
        self.id_type_fuel = id_type_fuel
        self.id = id
        
        self.optionsSelectTupeFuelDropdown = []
        
        self.selected_type_fuel = None
        
        self.selected_amount_of_fuel_text = TextField(# выбранный объем топлива
            label="Выброное к. топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value=self.selected_amount_of_fuel,
            text_size=16,
            multiline=False,
            expand=1,
            on_change=self.UpdatingFuelValueText
        )
        self.maximum_amount_of_fuel_text = TextField(
            label="Макс. к. топлива",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value=self.maximum_amount_of_fuel,
            text_size=16,
            multiline=False,
            expand=1,
            on_change=self.UpdateDataSliderText   
        )
        self.slider_toplivo = Slider(
            height=40,
            expand=1,
            max=float(self.maximum_amount_of_fuel),
            min=0,
            round=2,
            active_color="#B85C38",
            value=float(self.selected_amount_of_fuel),
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
                
                if self.id_type_fuel == _list[0]:
                    self.selected_type_fuel = self.optionsSelectTupeFuelDropdown[i_list]
                    self.type_of_fuel.value = str(self.selected_type_fuel.ReturnText())
                     

                self.type_of_fuel.options.append(self.optionsSelectTupeFuelDropdown[i_list].ReturnData())
            
    def ChoosingSheetWithTypeFuel(self, e):# Выбор листа с видом топлива 
        for list_fuel_type in self.optionsSelectTupeFuelDropdown:
            if(str(list_fuel_type.name_fuel) + ": " + str(list_fuel_type.manufacturer_fuel) + ": " + str(list_fuel_type.cost_fuel)) == self.type_of_fuel.value:
                
                self.selected_type_fuel = list_fuel_type
        
    def UpdatingCurrentFuelSlider(self, e):# Обновление данных слайнера
        self.selected_amount_of_fuel_text.value = round(self.slider_toplivo.value, 0)
        self.selected_amount_of_fuel_text.update()
   
    def UpdatingFuelValueText(self, e):# Обновление данных текста
        if self.maximum_amount_of_fuel_text.value != '':
            self.slider_toplivo.value = float(self.selected_amount_of_fuel_text.value) 
        elif self.maximum_amount_of_fuel_text.value == '':
            self.slider_toplivo.value = 0
        self.slider_toplivo.update()
    
    def UpdateDataSliderText(self, e):# Обновление данных 
        if self.maximum_amount_of_fuel_text.value != '':
            self.slider_toplivo.max = float(self.maximum_amount_of_fuel_text.value) 
        elif self.maximum_amount_of_fuel_text.value == '':
            self.slider_toplivo.max = 0
        self.slider_toplivo.update()
        
    def UpdateStationOfcolumn(self, e):# Добавление станции
        from dataFuel import data_base
        from body import body_part
        from heder import heder_main
        
        data_base.UpdateStationCard(
            id=self.id,
            amount_of_fuel=float(self.selected_amount_of_fuel_text.value),
            maximum_fuel_capacity=float(self.maximum_amount_of_fuel_text.value),
            id_type_fuel=self.selected_type_fuel._id
        )
        
        heder_main.UpdateDataRowStation()
        body_part.OpenSetingColumnCheac(name_column=self.column_card)
    
    def build(self):
        return Column(
            controls=[
                Row(
                    controls=[
                        self.selected_amount_of_fuel_text,
                        self.maximum_amount_of_fuel_text,
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
                            icon=icons.CHANGE_CIRCLE_OUTLINED,
                            icon_size=30,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ), 
                            on_click=self.UpdateStationOfcolumn
                        ),
                    ]
                )
            ]
        )