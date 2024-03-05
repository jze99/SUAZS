from flet import *

class SetingFuelView(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.column_manufactorer_fuel = Column()
        
        self.LoadViewFuel()
        
    def LoadViewFuel(self):
        from dataFuel import data_base
        from viewFule import ViewFuel
        
        self.column_manufactorer_fuel.controls.clear()
        self.column_manufactorer_fuel.controls.append(Row(alignment=MainAxisAlignment.CENTER,controls=[Text(size=20, value="Вид топлива")]))
        
        view_list = data_base.LoadListViewFuel()
        for view in view_list:
            self.column_manufactorer_fuel.controls.append(Container(ViewFuel(id=view[0],view=view[1])))
    
        self.column_manufactorer_fuel.controls.append(
            Row(
                alignment=MainAxisAlignment.END,
                controls=[
                    IconButton(
                        icon=icons.ADD_BOX_OUTLINED,
                        icon_size=30,
                        style=ButtonStyle(
                            color="#E0C097",
                            shape=RoundedRectangleBorder(radius=10) 
                        ), 
                        on_click=self.AddManufactorerFuel
                    )
                ]
            )
        )
        
    def AddManufactorerFuel(self, e):
        from body import body_part
        body_part.OpenAddNewViewFuel()

    
    def build(self):
        return self.column_manufactorer_fuel