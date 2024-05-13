from flet import UserControl, Column, Row
from OssnovElements.heder import heder_main
from OssnovElements.interactiveMenu import interactive_menu
from OssnovElements.body import body_part

class Main(UserControl):
  page = None
  def __init__(self, page):
    super().__init__()
    self.page = page
    Main.page = self.page
    
  def build(self):
    return Column(
        spacing=5,
        controls=[
            heder_main.build(),
            interactive_menu.build(),
            body_part.build()
        ],
    )