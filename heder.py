from flet import *
from dialogCheng import *

class Heder(UserControl):
  def __init__(self):
    super().__init__()
    
    self.add_fueld_card_button = IconButton(
      icon=icons.ADD,
      icon_size=40,
      style=ButtonStyle(
          color="#E0C097",
          shape=RoundedRectangleBorder(radius=10) 
      ),
      on_click=self.AddColumnCardBodySetting
    )
    self.row_column_card = Row(
      scroll=True,
      alignment=CrossAxisAlignment.END,
      height=140,
      auto_scroll=True,
      controls=[
          self.add_fueld_card_button,
      ],
    )
  
  def AddColumnCardBodySetting(self, e):
    from body import body_part
    body_part.OpenSettingColumn()
    
  def build(self):
    return self.row_column_card
  
heder_main = Heder()