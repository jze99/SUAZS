from flet import UserControl, Column, Row
from heder import heder_main
from interactiveMenu import interactive_menu
from body import body_part

class Main(UserControl):
  def __init__(self, page):
    super().__init__()
    self.page = page
    
  def build(self):
    return Column(
        spacing=5,
        controls=[
            heder_main.build(),
            interactive_menu.build(),
            body_part.build()
        ],
    )