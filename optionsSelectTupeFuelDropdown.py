from flet import *

class OptionsSelectTupeFuelDropdown(UserControl):
    
    def __init__(self, _id, name_fuel, manufacturer_fuel, cost_fuel):
        super().__init__()
        
        self._id = _id
        self.name_fuel = name_fuel
        self.manufacturer_fuel = manufacturer_fuel
        self.cost_fuel = cost_fuel
        
    def ReturnText(self):
        return (str(self.name_fuel) + ": " + str(self.manufacturer_fuel) + ": " + str(self.cost_fuel))
        
    def ReturnData(self):
        return dropdown.Option(str(self.name_fuel) + ": " + str(self.manufacturer_fuel) + ": " + str(self.cost_fuel))
    