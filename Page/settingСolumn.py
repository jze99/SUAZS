from flet import *

class SettingColumn(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.name_column = TextField(
            label="Название колонки",
            height=60,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        ) 
        self.add_column_button = IconButton(
            icon=icons.ADD_CARD,
            icon_size=40,
            style=ButtonStyle(
                color="#E0C097",
                shape=RoundedRectangleBorder(radius=10) 
            ),    
            on_click=self.AddColumnButton
        )
        
    def AddColumnButton(self, e):
        from Page.columnCard import ColumnCard
        from OssnovElements.heder import heder_main
        from dataFuel import data_base
        
        data_base.AddDataColumnCardBD(name=self.name_column.value, status=True)
        
        column_card = ColumnCard(name_column=self.name_column.value, statusC=True)
        heder_main.row_column_card.controls.insert(len(heder_main.row_column_card.controls)-1, Card(content=column_card))
        heder_main.row_column_card.update()
    
    def build(self):
        return Column(
            controls=[
                Row(
                    controls=[
                        self.name_column,
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        self.add_column_button
                    ]
                ),
            ]
        )
