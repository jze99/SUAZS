from flet import *

class SetingColumnCheac(UserControl):
    
    def __init__(self, name_column):
        super().__init__()
        
        self.name_column = name_column
        
        self.options = None
        
        self.optionsSelectTupeFuelDropdown = []
        
        self.cost_text = TextField(# цена за топливо
            label="Выброное ц. топлива",
            height=60,
            width=1300,
            border_color="#B85C38",
            read_only=False,
            value="0",
            text_size=16,
            multiline=False,
            on_change=self.ChengCost
        )
        
        self.type_of_fuel = Dropdown(
            label="Топливо",
            height=55,
            width=1300, 
            border_color="#B85C38",
            on_change=self.SetDropdawn
        )
        
        self.number_liters_text = TextField(# выбранный объем топлива
            label="Выброное к. топлива",
            height=60,
            width=1300,
            border_color="#B85C38",
            read_only=False,
            value="0",
            text_size=16,
            multiline=False,
            on_change=self.SetText
        )
        
        self.number_liters_slider = Slider(
            height=40,
            width=1300,
            max=0,
            min=0,
            round=2,
            active_color="#B85C38",
            value=0,
            on_change=self.SetSlider
        )
        
        self.button_cheng = IconButton(
            icon=icons.ATTACH_MONEY_ROUNDED,
            icon_size=40,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ), 
            on_click=self.IssueReceipt
        )
        
        self.column_station = Column(
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.AUTO,
            height=350,
            controls=[
                
            ]
        )
        
        self.column_view = Row(
                    vertical_alignment=CrossAxisAlignment.START,
                    controls=[
                        Container(
                            expand=True,
                            content=Column(
                                
                                alignment=MainAxisAlignment.CENTER,
                                controls=[
                                    self.type_of_fuel,
                                    self.number_liters_text,
                                    self.number_liters_slider,
                                    self.cost_text,
                                    Row(
                                        alignment=MainAxisAlignment.END,
                                        vertical_alignment=CrossAxisAlignment.END,
                                        controls=[
                                            self.button_cheng
                                        ]
                                    )
                                ]
                            )
                        ),
                        Container(
                            content=self.column_station
                        )
                    ]
                )
        
        self.LoadListFuel()
        self.LoadingStationCard()
        
    def IssueReceipt(self, e):#выпустить чек
        from dataFuel import data_base
        import datetime
        from OssnovElements.body import body_part
        from OssnovElements.heder import heder_main
        
        now = datetime.datetime.now()
        
        data_base.AddCheacBD(
            cost=float(self.cost_text.value),
            cost_per_liter=float(self.options.cost_fuel),
            view_fuel=self.options.name_fuel,
            manufacturer_fuel=self.options.manufacturer_fuel,
            data_t=str(now.day)+": "+str(now.month)+": "+str(now.year),
            time=str(now.hour)+": "+str(now.minute)+": "+str(now.second),
            liters=round(float(self.number_liters_slider.value),2),
            name_column=self.options.name_column
        )    
    
        data_base.UpdateStationCard(
            id=self.options._id,
            amount_of_fuel=round(float(self.options.amount_fuel),2) - round(float(self.number_liters_slider.value),2),
            maximum_fuel_capacity=self.options.amount_fuel,
            id_type_fuel=self.options.id_type_fuel
        )
        
        heder_main.Aplay()
        body_part.OpenMainHome()
    
    def LoadingStationCard(self):
        from dataFuel import data_base
        from Page.buttonStationCard import ButtonStationCard
        
        station_card = data_base.LoadingStationCard(column_name=self.name_column)
        if station_card: 
          for stat in station_card:
            stat_card = ButtonStationCard(
                id=stat[0],
                liters=stat[2],
                amount_of_fuel=stat[2],
                maximum_fuel_capacity=stat[3],
                name_station=stat[1],
                id_type_fuel=stat[4],
            )
            self.column_station.controls.append(
                Container(
                  stat_card
                )
            )
            stat_card.LoadTypeFuelId()
            
    def ChengCost(self, e):
        try:
            if self.options == None or self.number_liters_text == '':
                return
            self.number_liters_slider.value = round(float(self.cost_text.value)/self.options.cost_fuel,2)
            self.number_liters_text.value = round(float(self.cost_text.value)/self.options.cost_fuel,2)
            self.number_liters_slider.update()
            self.number_liters_text.update()
        except ValueError:
            return
        
    def LoadingCost(self):
        try:
            if self.options == None or self.number_liters_text == '':
                return
            self.cost_text.value = str(round(self.number_liters_slider.value * self.options.cost_fuel, 2))
            self.cost_text.update()
        except ValueError:
            return
        
    def SetDropdawn(self, e):
        for options in self.optionsSelectTupeFuelDropdown:
            if options.ReturnIf() == self.type_of_fuel.value:
                self.options = options
                self.number_liters_slider.max = options.amount_fuel
                self.LoadingCost()
                self.number_liters_slider.update()            
        
    def SetText(self, e):
        if self.number_liters_text!="":
            self.number_liters_slider.value = self.number_liters_text.value
        if self.number_liters_text == "":
            self.number_liters_slider.value = 0
        self.LoadingCost()
        self.number_liters_slider.update()
        
    def SetSlider(self, e):
        self.number_liters_text.value = str(round(self.number_liters_slider.value, 2))
        self.LoadingCost()
        self.number_liters_text.update()

    def LoadListFuel(self):# Загруска данных
        from dataFuel import data_base
        from Page.optionsSelectColumnCheacDropdown import OptionsSelectColumnCheacDropdown
        
        list_fuel = data_base.LoadListStationColumnCheac(name_column=self.name_column)
        
        self.optionsSelectTupeFuelDropdown.clear()
        self.type_of_fuel.options.clear()
        
        if list_fuel:
            for i_list, _list in enumerate(list_fuel):
                
                list_type_fuel = data_base.LoadListStationTypeFuelCheac(id=_list[4])
                
                for type_fuel in list_type_fuel:
                    
                    self.optionsSelectTupeFuelDropdown.append(OptionsSelectColumnCheacDropdown(
                        _id=_list[0],
                        name_fuel=type_fuel[1],
                        manufacturer_fuel=type_fuel[2],
                        cost_fuel=type_fuel[3],
                        amount_fuel=_list[2],
                        id_type_fuel=_list[4],
                        name_column=_list[1]
                    ))

                self.type_of_fuel.options.append(self.optionsSelectTupeFuelDropdown[i_list].ReturnData())
            
    
    def build(self):
        return self.column_view