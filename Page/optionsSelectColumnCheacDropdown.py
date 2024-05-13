from flet import *

class OptionsSelectColumnCheacDropdown(UserControl):

    def __init__(self, _id, name_fuel, manufacturer_fuel, cost_fuel, amount_fuel, id_type_fuel, name_column):
            super().__init__()

            self._id = _id
            self.name_fuel = name_fuel
            self.manufacturer_fuel = manufacturer_fuel
            self.cost_fuel = cost_fuel
            self.amount_fuel = amount_fuel
            self.id_type_fuel=id_type_fuel
            self.name_column = name_column
        
    def ReturnIf(self):
        return (str(self.name_fuel) + ": " + str(self.manufacturer_fuel) + ": " + str(self.cost_fuel) + "р : " + str(self.amount_fuel) + "л")
    
    def ReturnData(self):
        return dropdown.Option(str(self.name_fuel) + ": " + str(self.manufacturer_fuel) + ": " + str(self.cost_fuel) + "р : " + str(self.amount_fuel) + "л")
    