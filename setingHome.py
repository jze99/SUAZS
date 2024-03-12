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
        self.list_receipts_temp = None
        
        self.max_sales_id = None
        
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
        
        self.column_main = Column(
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text(value="Общее количество продаж топлива", size=40, expand=True, )
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
        
    def LoadDataReceipts(self):
        from dataFuel import data_base
        from receipts import Receipts
        
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
                    liters=data[7]
                )
            )
            
        self.list_receipts_temp = self.list_receipts[:]
        
        self.list_receipts_groop = self.LoadReceiptsGroop(self.list_receipts)
        self.MaxSales()
        self.LoadBarChart()
        
    def MaxSales(self):
        max_count = 0
        if not self.list_receipts_groop:
            return
        for i_receipts, receipts_groop in enumerate(self.list_receipts_groop):
            count = len(receipts_groop.receipts)  # Получаем количество элементов в текущем массиве
            if count > max_count:
                max_count = count
                id_max = i_receipts
        self.max_sales_id=id_max
    
    def LoadReceiptsGroop(self, receipts_list):
        from receipts import ReceiptsGroop
        receipts_groop_dict = {}
        for receipt in receipts_list:
            fuel_type = receipt.type_fuel
            if fuel_type not in receipts_groop_dict:
                receipts_groop_dict[fuel_type] = ReceiptsGroop(fuel_type)
            receipts_groop_dict[fuel_type].AddReceipts(receipts=receipt)

        list_receipts_groop = list(receipts_groop_dict.values())

        return list_receipts_groop
    
    def LoadBarChart(self):
        if not self.list_receipts_groop:
            return
        self.earnings_statistics.max_y=int(len(self.list_receipts_groop[self.max_sales_id].receipts))+2
        for i_receipts_groop, receipts_groop in enumerate(self.list_receipts_groop):
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
            self.earnings_statistics.bottom_axis.labels.append(
                ChartAxisLabel(
                    value=i_receipts_groop,
                    label=Container(Text(value=str(receipts_groop.type_fuel)))
                )   
            )
        pass
        
    def build(self):
        return self.column_main