from flet import *

def ViewsHendler(page):
    return{
        "/":View(
            route="/",
            controls=[
                Container(
                    height=30,
                    width=30,
                    bgcolor=""
                ),
            ],
        )
    }