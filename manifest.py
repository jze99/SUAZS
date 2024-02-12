from flet import Page, app
from view import ViewsHendler
from dialogCheng import *

def main(page: Page):
    page.window_height = 670
    page.window_width = 400
    page.window_min_height = 670
    page.window_min_width = 400
    page.title = "СУАЗС"
    page.dialog = dialog_cheg.dlg_setings
    
    def PageLoading(route):
        print(page.route)
        page.views.clear()
        page.views.append(ViewsHendler(page=page)[page.route])
    page.on_route_change = PageLoading
    page.go("/")
    
app(target=main, assets_dir="assets")