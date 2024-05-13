from flet import *
from Page.setingHome import SetingHome

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
        from Page.settingСolumn import SettingColumn
        self.body_part.content = Container(SettingColumn())
        self.body_part.update()
        
    def OpenSettingStation(self, _self):
        from Page.setingAddStation import SetingAddStation
        self.body_part.content = Container(SetingAddStation(self_column=_self))
        self.body_part.update()
        
    def OpenMainHome(self):
        from Page.setingHome import SetingHome
        self.body_part.content = Container(SetingHome())
        self.body_part.update()
        
    def OpenNewTypeFuel(self):
        from Page.setingAddDataTypeFuel import SetingAddDataTypeFuel
        self.body_part.content = Container(SetingAddDataTypeFuel())
        self.body_part.update()
        
    def OpenListTypeFuel(self):
        from Page.setingTypeFuel import SetingTypeFuel
        self.body_part.content = Container(SetingTypeFuel())
        self.body_part.update()
        
    def OpenSetingFuelView(self):
        from Page.setingFuelView import SetingFuelView
        self.body_part.content = Container(SetingFuelView())
        self.body_part.update()
    
    def OpenAddNewViewFuel(self):
        from Page.setingAddNewViewFuel import SetingAddNewViewFuel
        self.body_part.content = Container(SetingAddNewViewFuel())
        self.body_part.update()
        
    def OpenAddNewManufacturerFuel(self):
        from Page.setingAddNewManufacturerFuel import SetingAddNewManufacturerFuel
        self.body_part.content = Container(SetingAddNewManufacturerFuel())
        self.body_part.update()

    def OpenSetingFuelManufacturer(self):
        from Page.setingFuelManufacturer import SetingFuelManufactorer
        self.body_part.content = Container(SetingFuelManufactorer())
        self.body_part.update()
        
    def OpenSetingUpdateViewFuel(self, _id, view):
        from Page.setingUpdateViewFuel import SetingUpadteViewFuel
        test = SetingUpadteViewFuel()
        self.body_part.content = test
        self.body_part.update()
        test.LoadData(_id=_id, view=view)
        
    def OpenSetingUpdateManufacturerFuel(self, _id, manufacturer):
        from Page.setingUpdateManufacturerFuel import SetingUpadteManufacturerFuel
        test = SetingUpadteManufacturerFuel()
        self.body_part.content = test
        self.body_part.update()
        test.LoadData(_id=_id, manufacturer=manufacturer)
        
    def OpenSetingUpdateTypeFuel(self, _id, view, manufacturer, cost):
        from Page.setingUpdateTypeFuel import SetingUpdateTypeFuel
        test = SetingUpdateTypeFuel()
        self.body_part.content = test
        self.body_part.update()
        test.LoadData(_id=_id, view=view, manufacturer=manufacturer, cost=cost)
        
    def OpenSetingColumnCheac(self, name_column:str):
        from Page.setingColumnCheac import SetingColumnCheac
        self.body_part.content=SetingColumnCheac(name_column=name_column)
        self.body_part.update()
        
    def OpenSetingUpdateStationCard(self, self_column, maximum_amount_of_fuel, selected_amount_of_fuel, id_type_fuel, id):
        from Page.setingUpdateStationCard import SetingUpdateStation
        
        self.body_part.content = SetingUpdateStation(
            self_column=self_column,
            maximum_amount_of_fuel=maximum_amount_of_fuel,
            selected_amount_of_fuel=selected_amount_of_fuel,
            id_type_fuel=id_type_fuel,
            id=id
        )
        self.body_part.update()
        
    def OpenPeopleList(self):
        from Page.setingNewPeopleLogin import People
        self.body_part.content = People()
        self.body_part.update()
    
    def OpenChengPeople(self):
        from Page.setingNewPeopleLogin import PeopleChenge
        self.body_part.content = PeopleChenge()
        self.body_part.update()
        
    def OpenNewPeopl(self):
        from Page.setingNewPeopleLogin import NewPeople
        self.body_part.content = NewPeople()
        self.body_part.update()
        
    def Exit(self):
        from main import Main
        Main.page.go("/log")
        
    def build(self):
        return self.body_part

body_part = Body()