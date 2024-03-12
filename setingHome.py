from flet import *

class SetingHome(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.colors = [
            '#FF0000', # Красный
            '#00FF00', # Зеленый
            '#0000FF', # Синий
            '#FFFF00', # Желтый
            '#FF00FF', # Фиолетовый
            '#00FFFF', # Бирюзовый
            '#800000', # Темно-красный
            '#008000', # Темно-зеленый
            '#000080', # Темно-синий
            '#FFA500', # Оранжевый
            '#A52A2A', # Коричневый
            '#800080', # Пурпурный
            '#DC143C', # Карминный
            '#808000', # Оливковый
            '#FFD700', # Золотой
            '#800080', # Фиолетовый
            '#008080', # Бирюзовый
            '#FF6347', # Морковный
            '#C71585', # Ягодный
            '#2E8B57', # Морской
            '#4682B4', # Стальной синий
            '#F0E68C', # Хаки
            '#D2B48C', # Светло-коричневый
            '#800000', # Темно-красный
            '#B22222', # Огненный кирпич
            '#808080', # Серый
            '#F0F8FF', # Очень светло-голубой
            '#FFD700', # Золотой
            '#4B0082', # Индиго
            '#696969', # Темно-серый
            '#8A2BE2', # Изумрудный
            '#ADFF2F', # Зеленый светлячок
            '#CD5C5C', # Индийский красный
            '#FF4500', # Огненно-красный
            '#9370DB', # Фиолетовый
            '#483D8B', # Темно-синевато-фиолетовый
            '#6A5ACD', # Синевато-фиолетовый
            '#4B0082', # Индиго
            '#008080'  # Бирюзовый
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
        
        #self.LoadReceiptsGroop()
        self.list_receipts_groop = self.LoadReceiptsGroop(self.list_receipts)
        self.MaxSales()
        self.LoadBarChart()
        
    def MaxSales(self):
        max_count = 0
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
    
    #def LoadReceiptsGroop(self):
    #    from receipts import Receipts, ReceiptsGroop
    #    
    #    if self.list_receipts_groop:
    #        for receipts_groop in self.list_receipts_groop:
    #            if self.list_receipts_temp:
    #                for receipts in self.list_receipts_temp:
    #                    if receipts_groop.type_fuel == receipts.type_fuel:
    #                            receipts_groop.AddReceipts(receipts=receipts)
    #                            self.list_receipts_temp.remove(receipts)
    #                            
    #                    else:
    #                        temp = ReceiptsGroop(receipts.type_fuel)
    #                        temp.AddReceipts(receipts=receipts)
    #                        self.list_receipts_groop.append(temp)
    #                        self.list_receipts_temp.remove(receipts)
    #                        self.LoadReceiptsGroop()               
    #    else:
    #        temp = ReceiptsGroop(self.list_receipts_temp[0].type_fuel)
    #        temp.AddReceipts(receipts=self.list_receipts_temp[0])
    #        self.list_receipts_groop.append(temp)
    #        self.list_receipts_temp.remove(self.list_receipts_temp[0])
    #        self.LoadReceiptsGroop()
    
    def LoadBarChart(self):
        
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