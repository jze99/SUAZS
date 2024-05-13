from flet import *

class SetingHome(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.colors = [
            '#8B4513',
            '#A0522D',
            '#CD853F',
            '#D2691E',
            '#8B5A2B',
            '#A0522D',
            '#BC8F8F',
            '#A52A2A',
            '#8B4513',
            '#D2B48C',
            '#A52A2A',
            '#CD853F',
            '#8B4513',
            '#BC8F8F',
            '#A0522D',
            '#D2691E',
            '#8B5A2B',
            '#D2B48C',
            '#BC8F8F',
            '#8B5A2B',
            '#A52A2A',
            '#8B4513',
            '#CD853F',
            '#A0522D',
            '#D2B48C',
            '#8B4513',
            '#A0522D',
            '#BC8F8F',
            '#A52A2A',
            '#D2B48C',
            '#8B4513',
            '#D2691E',
            '#CD853F',
            '#8B5A2B',
            '#BC8F8F',
            '#A0522D',
            '#CD853F',
            '#A52A2A'
        ]
        
        self.list_receipts = []
        self.list_receipts_groop = []
        self.list_receipts_column_group = []
        self.list_receipts_temp = None
        
        self.lit_cost = 0.0
        
        self.earnings_statistics = BarChart(
            interactive=True,
            expand=True,
            bar_groups=[],
            bottom_axis=ChartAxis(),
            border=border.all(1, "#E0C097"),
            
            left_axis=ChartAxis(
                labels_size=40, title_size=40
            ),
            
            horizontal_grid_lines=ChartGridLines(
                color="#E0C097", width=1, dash_pattern=[3, 3]
            ),
        )
        
        self.type_diogram = Dropdown(
        expand=True,
        on_change=self.UpdateTypeData,
        value="Количество продаж по типу топлива",
        options=[
            dropdown.Option("Количество продаж по типу топлива"),
            dropdown.Option("Количество продаж по названию колонки"),
            dropdown.Option("Количество денег с каждого типа топлива"),
            dropdown.Option("Количество денег с каждой колонки"),
            dropdown.Option("Количество литров с каждого типа топлива"),
            dropdown.Option("Количество литров с каждой колонки"),
        ],
    )
        
        self.column_main = Column(
            controls=[
                
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.type_diogram
                    ]
                ),
                Row(
                    controls=[
                        self.earnings_statistics
                    ]
                )
            ]
        )
        
        self.LoadDataReceipts()
        
    def UpdateTypeData(self, e):
        self.earnings_statistics.bar_groups.clear()
        self.LoadBarChart()
        self.earnings_statistics.update()
        
    def LoadDataReceipts(self):
        from dataFuel import data_base
        from Page.receipts import Receipts
        
        list_data = data_base.LoadListDataReceipts()
        
        if not list_data:
            return
        for data in list_data:
            self.list_receipts.append(
                Receipts(
                    cost=data[1],
                    cost_per_liter=data[2],
                    view_fuel=data[3],
                    manufacturer_fuel=data[4],
                    data=data[5],
                    time=data[6],
                    liters=data[7],
                    column_name=data[8]
                )
            )
            
        self.list_receipts_temp = self.list_receipts[:]
        
        self.list_receipts_groop = self.LoadReceiptsGroop(self.list_receipts)
        self.list_receipts_column_group = self.LoadReceiptsGroopColumnName(self.list_receipts)
        self.LoadBarChart()
        
    def MaxSales(self, list):
        max_count = 0
        if not list:
            return
        for i_receipts, receipts_groop in enumerate(list):
            count = len(receipts_groop.receipts)  # Получаем количество элементов в текущем массиве
            if count > max_count:
                max_count = count
                id_max = i_receipts
        return id_max
    
    def LoadReceiptsGroop(self, receipts_list):
        from Page.receipts import ReceiptsGroop
        receipts_groop_dict = {}
        for receipt in receipts_list:
            fuel_type = receipt.type_fuel
            if fuel_type not in receipts_groop_dict:
                receipts_groop_dict[fuel_type] = ReceiptsGroop(type_fuel = fuel_type)
            receipts_groop_dict[fuel_type].AddReceipts(receipts=receipt)

        list_receipts_groop = list(receipts_groop_dict.values())

        return list_receipts_groop
    
    def LoadReceiptsGroopColumnName(self, receipts_list):
        from Page.receipts import ReceiptsGroop
        receipts_groop_dict = {}
        for receipt in receipts_list:
            column_name = receipt.column_name
            if column_name not in receipts_groop_dict:
                receipts_groop_dict[column_name] = ReceiptsGroop(column_name = column_name)
            receipts_groop_dict[column_name].AddReceipts(receipts=receipt)

        list_receipts_groop = list(receipts_groop_dict.values())

        return list_receipts_groop
    
    def LoadBarChart(self):
        if not self.list_receipts_groop:
            return
        
        lit_cost =[]
        temp = 0
        
        match  self.type_diogram.value:
            case "Количество продаж по типу топлива":
                list_data = self.list_receipts_groop
                self.earnings_statistics.max_y=int(len(list_data[self.MaxSales(list_data)].receipts))+2
                
            case "Количество продаж по названию колонки":
                list_data = self.list_receipts_column_group
                self.earnings_statistics.max_y=int(len(list_data[self.MaxSales(list_data)].receipts))+2
                
            case "Количество денег с каждого типа топлива":
                list_data = self.list_receipts_groop
                for cost in list_data:
                    temp = 0
                    for co in cost.receipts:
                        temp += co.cost
                    lit_cost.append(temp)
                self.earnings_statistics.max_y=round(max(lit_cost),0)+10
                self.earnings_statistics.update()
            case "Количество денег с каждой колонки":
                list_data = self.list_receipts_column_group
                for cost in list_data:
                    temp = 0
                    for co in cost.receipts:
                        temp += co.cost
                    lit_cost.append(temp)
                self.earnings_statistics.max_y=round(max(lit_cost),0)+10
                self.earnings_statistics.update()
            case "Количество литров с каждого типа топлива":
                list_data = self.list_receipts_groop
                for cost in list_data:
                    temp = 0
                    for co in cost.receipts:
                        temp += co.liters
                    lit_cost.append(temp)
                self.earnings_statistics.max_y=round(max(lit_cost),0)+10
                self.earnings_statistics.update()
            case "Количество литров с каждой колонки":
                list_data = self.list_receipts_column_group
                for cost in list_data:
                    temp = 0
                    for co in cost.receipts:
                        temp += co.liters
                    lit_cost.append(temp)
                self.earnings_statistics.max_y=round(max(lit_cost),0)+10
                self.earnings_statistics.update()
        if not lit_cost:
            for i_receipts_groop, receipts_groop in enumerate(list_data):
                self.earnings_statistics.bar_groups.append(
                    BarChartGroup(
                        x=i_receipts_groop,
                        bar_rods=[
                            BarChartRod(
                                from_y=0,
                                to_y=len(receipts_groop.receipts),
                                width=10,
                                color=self.colors[i_receipts_groop],
                                tooltip=len(receipts_groop.receipts),
                                border_radius=0,
                             ),
                        ],
                    )
                )
                if receipts_groop.type_fuel != None:
                    self.earnings_statistics.bottom_axis.labels.append(
                        ChartAxisLabel(
                            value=i_receipts_groop,
                            label=Container(Text(value=str(receipts_groop.type_fuel)))
                        )   
                    )
                if receipts_groop.column_name != None:
                    self.earnings_statistics.bottom_axis.labels.append(
                        ChartAxisLabel(
                            value=i_receipts_groop,
                            label=Container(Text(value=str(receipts_groop.column_name)))
                        )   
                    )         
        if lit_cost:
            for i_receipts_groop, receipts_groop in enumerate(list_data):
                self.earnings_statistics.bar_groups.append(
                    BarChartGroup(
                        x=i_receipts_groop,
                        bar_rods=[
                            BarChartRod(
                                from_y=0,
                                to_y=round(lit_cost[i_receipts_groop],2),
                                width=10,
                                color=self.colors[i_receipts_groop],
                                tooltip=round(lit_cost[i_receipts_groop],2),
                                border_radius=0,
                             ),
                        ],
                    )
                )
                if receipts_groop.type_fuel != None:
                    self.earnings_statistics.bottom_axis.labels.append(
                        ChartAxisLabel(
                            value=i_receipts_groop,
                            label=Container(Text(value=str(receipts_groop.type_fuel)))
                        )   
                    )
                if receipts_groop.column_name != None:
                    self.earnings_statistics.bottom_axis.labels.append(
                        ChartAxisLabel(
                            value=i_receipts_groop,
                            label=Container(Text(value=str(receipts_groop.column_name)))
                        )   
                    )         
        pass
        
    def build(self):
        return self.column_main