from flet import *

class SetingTypeFuel(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.list_fuel_type = Column()
        
        self.LoadFuelTypeList()
        
    def AddNewTypeFuel(self, e):
        from body import body_part
        body_part.OpenNewTypeFuel()
    
    def LoadFuelTypeList(self):
        from dataFuel import data_base
        from viewFuelType import ViewFuelType
        
        list_fuel_type = data_base.LoadListFuelType()
        
        self.list_fuel_type.controls.append(
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Text(
                        value="Тип топлива",
                        size=20
                    )
                ]
            )
        )
        
        for fuel_type in list_fuel_type:
            self.list_fuel_type.controls.append(
                Container(
                    content= ViewFuelType(
                        _id=fuel_type[0],
                        view=fuel_type[1],
                        manufacturer=fuel_type[2],
                        cost=fuel_type[3]
                    )
                )
            )
        self.list_fuel_type.controls.append(
            Row(
                alignment=MainAxisAlignment.END,
                controls=[
                    IconButton(
                        icon=icons.ADD_BOX_OUTLINED,
                        icon_size=40,
                        style=ButtonStyle(
                            color="#E0C097",
                            shape=RoundedRectangleBorder(radius=10) 
                        ), 
                        on_click=self.AddNewTypeFuel
                    )
                ]
            )
        )
        
    def build(self):
        return self.list_fuel_type