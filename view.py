from flet import View
from main import Main
from login import Login

def ViewsHendler(page):
    return{
        "/":View(
            route="/",
            controls=[
                Main(page=page),
            ],
            bgcolor="#2D2424",
            scroll=True,
        ),
        "/log":View(
            route="/log",
            controls=[
                Login(page=page)
            ],
            bgcolor="#2D2424",
            scroll=True,
        )
    }