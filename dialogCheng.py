from flet import *

class DialogStation(UserControl):
    def __init__(self):
        self.column_name = TextField(
            label="Название колонки",
            height=60,
            width=300,
            border_color="#B85C38",
            read_only=False,
            value="new colon",
            text_size=20,
            multiline=False,
            expand=1,
            dense=True,
        )
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
            width=400,
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
            width=400, 
        )
        self.dlg_setings = AlertDialog(
        modal=True,
        title=Text("Настройка новой колонки"),
        content=Column(
                controls=[
                self.column_name,
                Text(
                    height=60,
                    width=300,
                    expand=1,
                    value="Текущий запас топлива",
                ),
                Row(
                    expand = 1,
                    controls=[
                        self.selected_amount_of_fuel,
                        self.maximum_amount_of_fuel,
                    ],
                ),
                self.slider_toplivo,
                Text(
                    height=60,
                    width=300,
                    expand=1,
                    value="Текущий вид топлива",
                ),
                self.type_of_fuel,
            ],
            alignment=MainAxisAlignment.START,
            height=300,
            width=400,
        ),
        actions=[
            IconButton(
                icon=icons.ADD,
                icon_size=40,
                style=ButtonStyle(
                    color="#E0C097",
                    shape=RoundedRectangleBorder(radius=10) 
                ),
                on_click=self.AddNewCard,
            ),
            IconButton(
                icon=icons.CLOSE,
                icon_size=40,
                style=ButtonStyle(
                    color="#E0C097",
                    shape=RoundedRectangleBorder(radius=10) 
                ),
                on_click=self.close_dlg,
            ),
        ],
        actions_alignment=MainAxisAlignment.END,
        
    )
        
    def UpdatingCurrentFuelSlider(self, e):
        self.selected_amount_of_fuel.value = round(self.slider_toplivo.value, 2)
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
    
    def AddNewCard(self, e):
        pass
        self.close_dlg(e=e)
    def close_dlg(self, e):
            self.dlg_setings.open = False
            self.dlg_setings.update()
    
dialog_cheg = DialogStation()