from flet import View
from main import Main

def ViewsHendler(page):
    return{
        "/":View(
            route="/",
            controls=[
                Main(page=page),
            ],
            bgcolor="#2D2424",
            scroll=True,
        )
    }