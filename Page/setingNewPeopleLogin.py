from flet import *

class PeopleRow(UserControl):
    paswC = ""
    nameC = ""
    statC = ""
    idPeople = ""
    
    def __init__(self, name, pasw, stat, idPeople):
        super().__init__()
 
        self.pasw = pasw
        self.name = name
        self.stat = stat
        self.idPeople = idPeople
        
        self.rowPeople = Row(
            controls=[
                Container(
                    height=60,
                    bgcolor="#B85C38",
                    border_radius=10,
                    expand=True,
                    content=Row(
                        controls=[
                            TextButton(
                                on_click=self.ChengClic,
                                height=60,
                                expand=True,
                                content=Row(
                                    controls=[Text(name), Text(stat)]
                                ),
                                style=ButtonStyle(
                                    color="#E0C097",
                                    shape=RoundedRectangleBorder(radius=10) 
                                ),
                            ),
                        ]
                    )
                )
            ]
        )
    
    def ChengClic(self, e):
        from OssnovElements.body import body_part
        PeopleRow.paswC = self.pasw
        PeopleRow.nameC = self.name
        PeopleRow.statC = self.stat
        PeopleRow.idPeople = self.idPeople
        body_part.OpenChengPeople()
        
    def build(self):
        return self.rowPeople
    
class People(UserControl):
    
    def __init__(self):
        super().__init__()
        self.column = Column(
            controls=[]
        )
        self.LoadListPeople()
        
    def LoadListPeople(self):
        from dataFuel import data_base
        
        self.column.controls.clear()
        temp = data_base.loadPeople()
        for user in temp:
            self.column.controls.append(PeopleRow(idPeople=user[0], name=user[1],pasw=user[2], stat=user[3]))
    
    def build(self):
        return self.column
    
class PeopleChenge(UserControl):
    def __init__(self):
        super().__init__()
        
        self.name = TextField(
            label="Имя",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value=PeopleRow.nameC,
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.pasw = TextField(
            label="Пароль",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value=PeopleRow.paswC,
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.status = Dropdown(
            label="Производитель топлива",
            height=55,
            expand=1, 
            border_color="#B85C38",
            options=[
                dropdown.Option("admin"),
                dropdown.Option("salesman"),
            ],
            value=str(PeopleRow.statC)
        )
        
        self.column = Column(
            controls=[
                Row(
                    controls=[
                        self.name
                    ]
                ),
                Row(
                    controls=[
                        self.pasw
                    ]
                ),
                Row(
                    controls=[
                        self.status
                    ]
                ),
                Row(
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        IconButton(
                            height=50,
                            on_click=self.DeletePeople,
                            icon_size=30,
                            icon=icons.DELETE,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ),
                        ),
                        IconButton(
                            on_click=self.ChengPeople,
                            height=50,
                            icon_size=30,
                            icon=icons.CHANGE_CIRCLE_OUTLINED,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ),
                        )
                    ]
                )
            ]
        )
    
    def ChengPeople(self, e):
        from dataFuel import data_base
        from OssnovElements.body import body_part
        data_base.ChengPeople(name=self.name.value, pasw=self.pasw.value, stat=self.status.value, idPep=PeopleRow.idPeople)
        body_part.OpenPeopleList()
        
    def DeletePeople(self, e):
        from dataFuel import data_base
        from OssnovElements.body import body_part
        data_base.DeletePeople(id=PeopleRow.idPeople)
        body_part.OpenPeopleList()
        
    def build(self):
        return self.column
    
class NewPeople(UserControl):
    
    def __init__(self):
        super().__init__()
        
        self.name = TextField(
            label="Имя",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.pasw = TextField(
            label="Пароль",
            height=60,
            width=30,
            border_color="#B85C38",
            read_only=False,
            value="",
            text_size=16,
            multiline=False,
            expand=1,
        )
        
        self.status = Dropdown(
            label="Производитель топлива",
            height=55,
            expand=1, 
            border_color="#B85C38",
            options=[
                dropdown.Option("admin"),
                dropdown.Option("salesman"),
            ]
        )
        
        self.column = Column(
            controls=[
                Row(
                    controls=[self.name]
                ),
                Row(
                    controls=[self.pasw]
                ),
                Row(
                    controls=[self.status]
                ),
                Row(
                    alignment=MainAxisAlignment.END,
                    controls=[
                        IconButton(
                            on_click=self.AddNewPeople,
                            height=50,
                            icon_size=30,
                            icon=icons.ADD,
                            style=ButtonStyle(
                                color="#E0C097",
                                shape=RoundedRectangleBorder(radius=10) 
                            ),
                        )
                    ]
                )
            ]
        )
    
    def AddNewPeople(self,e):
        from OssnovElements.body import body_part
        from dataFuel import data_base
        data_base.AddPeople(name=self.name.value, pasw=self.pasw.value, stat=self.status.value)    
        body_part.OpenPeopleList()
    def build(self):
        return self.column

