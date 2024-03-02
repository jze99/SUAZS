from flet import *

class Login(UserControl):
    def __init__(self, page):
      super().__init__()
      self.page = page

      self.name_user = TextField(# Поле ввода логина
          label="Введите имя",
          height=60,
          width=30,
          border_color="#B85C38",
          read_only=False,
          value="",
          text_size=16,
          multiline=False,
          expand=1,
      )

      self.passworg_user = TextField(# Поле ввода пароля
          label="Введите пароль",
          height=60,
          width=30,
          border_color="#B85C38",
          read_only=False,
          value="",
          text_size=16,
          multiline=False,
          expand=1,
      )

    def Login(self, e):
        from dataFuel import data_base
        users_list = data_base.LoadingUsers()
        for user in users_list:
            if user[1] == self.name_user.value and user[5] == self.passworg_user.value:
                print("ура")
                return
        print("нет таких пользователей")

    def build(self):
      return Column(
          spacing=20,
          controls=[
              Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Text(
                          size=15,
                          value="Вход в учётную запись"
                      )
                    ]
              ),
              Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.name_user
                    ]
              ),
              Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.passworg_user
                    ]
              ),
              Row(
                  alignment=MainAxisAlignment.END,
                  controls=[
                        IconButton(
                        icon=icons.ARROW_RIGHT_ROUNDED,
                        icon_size=40,
                        style=ButtonStyle(
                            color="#E0C097",
                            shape=RoundedRectangleBorder(radius=10) 
                          ),
                        on_click=self.Login
                    )
                  ]
              ),
          ],
      )