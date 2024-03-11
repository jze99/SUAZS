from flet import *

class OptionsSelectColumnCheacDropdown(UserControl):

    def __init__(self, _id, name_fuel, manufacturer_fuel, cost_fuel, amount_fuel):
            super().__init__()

            self._id = _id
            self.name_fuel = name_fuel
            self.manufacturer_fuel = manufacturer_fuel
            self.cost_fuel = cost_fuel
            self.amount_fuel = amount_fuel
        
    def ReturnIf(self):
        return (str(self.name_fuel) + ": " + str(self.manufacturer_fuel) + ": " + str(self.cost_fuel) + "р : " + str(self.amount_fuel) + "л")
    
    def ReturnData(self):
        return dropdown.Option(str(self.name_fuel) + ": " + str(self.manufacturer_fuel) + ": " + str(self.cost_fuel) + "р : " + str(self.amount_fuel) + "л")
    