class Receipts():
    
    def __init__(self, cost, cost_per_liter, view_fuel, manufacturer_fuel, data, time, liters):
        
        self.cost = cost
        self.cost_per_liter = cost_per_liter
        self.view_fuel = view_fuel
        self.manufacturer_fuel = manufacturer_fuel
        self.data = data
        self.time = time
        self.liters = liters
        
        self.type_fuel = str(self.view_fuel)+": "+str(self.manufacturer_fuel)
        
class ReceiptsGroop():
    
    def __init__(self, type_fuel):
        
        self.receipts = []
        self.type_fuel = type_fuel
    
    def AddReceipts(self,receipts):
        
        self.receipts.append(receipts)
        
        