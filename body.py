from flet import *
from setingHome import SetingHome

class Body(UserControl):
    def __init__(self):
        super().__init__()
        
        self.column_name = TextField(
            label="Название колонки",
            height=60,
            expand = 1,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
        )
        
        self.body_part = Container(
            bgcolor="#5C3D2E",
            border_radius=border_radius.all(3),
            padding=10,
            content=Container(SetingHome())
        )
    
    
    
    def OpenSettingColumn(self):
        from settingСolumn import SettingColumn
        self.body_part.content = Container(SettingColumn())
        self.body_part.update()
        
    def OpenSettingStation(self, _self):
        from setingStation import SetingStation
        self.body_part.content = Container(SetingStation(self_column=_self))
        self.body_part.update()
        
    def OpenMainHome(self):
        from setingHome import SetingHome
        self.body_part.content = Container(SetingHome())
        self.body_part.update()
        
    def OpenNewTypeFuel(self):
        from setingAddDataTypeFuel import SetingAddDataTypeFuel
        self.body_part.content = Container(SetingAddDataTypeFuel())
        self.body_part.update()
        
    def OpenListTypeFuel(self):
        from setingTypeFuel import SetingTypeFuel
        self.body_part.content = Container(SetingTypeFuel())
        self.body_part.update()
        
    def OpenSetingFuelView(self):
        from setingFuelView import SetingFuelView
        self.body_part.content = Container(SetingFuelView())
        self.body_part.update()
    
    def OpenAddNewViewFuel(self):
        from setingAddNewViewFuel import SetingAddNewViewFuel
        self.body_part.content = Container(SetingAddNewViewFuel())
        self.body_part.update()
        
    def OpenAddNewManufacturerFuel(self):
        from setingAddNewManufacturerFuel import SetingAddNewManufacturerFuel
        self.body_part.content = Container(SetingAddNewManufacturerFuel())
        self.body_part.update()

    def OpenSetingFuelManufacturer(self):
        from setingFuelManufacturer import SetingFuelManufactorer
        self.body_part.content = Container(SetingFuelManufactorer())
        self.body_part.update()
        
    def OpenSetingUpdateViewFuel(self, _id, view):
        from setingUpdateViewFuel import SetingUpadteViewFuel
        test = SetingUpadteViewFuel()
        self.body_part.content = test
        self.body_part.update()
        test.LoadData(_id=_id, view=view)
        
    def OpenSetingUpdateManufacturerFuel(self, _id, manufacturer):
        from setingUpdateManufacturerFuel import SetingUpadteManufacturerFuel
        test = SetingUpadteManufacturerFuel()
        self.body_part.content = test
        self.body_part.update()
        test.LoadData(_id=_id, manufacturer=manufacturer)
        
    def OpenSetingUpdateTypeFuel(self, _id, view, manufacturer, cost):
        from setingUpdateTypeFuel import SetingUpdateTypeFuel
        test = SetingUpdateTypeFuel()
        self.body_part.content = test
        self.body_part.update()
        test.LoadData(_id=_id, view=view, manufacturer=manufacturer, cost=cost)
        
    def build(self):
        return self.body_part

body_part = Body()