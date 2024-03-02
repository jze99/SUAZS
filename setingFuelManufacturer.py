from flet import *

class SetingFuelManufactorer(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.column_name_fuel = Column()
        
        self.LoadViewFuel()
        
    def LoadViewFuel(self):
        from dataFuel import data_base
        from viewFule import ViewFuel
        
        self.column_name_fuel.controls.clear()
        self.column_name_fuel.controls.append(Row(alignment=MainAxisAlignment.CENTER,controls=[Text(size=20, value="Виды топлива")]))
        
        view_list = data_base.LoadListManufacturerFuel()
        for view in view_list:
            self.column_name_fuel.controls.append(Container(ViewFuel(id=view[0],view=view[1])))
    
        self.column_name_fuel.controls.append(
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
        body_part.OpenAddNewManufacturerFuel()

    
    def build(self):
        return self.column_name_fuel