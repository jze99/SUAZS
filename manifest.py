from flet import Page, app, AppView
from view import ViewsHendler

def main(page: Page):
    page.window_height = 670
    page.window_width = 400
    page.window_min_height = 670
    page.window_min_width = 400
    page.title = "СУАЗС"
    
    def PageLoading(route):
        print(page.route)
        page.views.clear()
        page.views.append(ViewsHendler(page=page)[page.route])
    page.on_route_change = PageLoading
    page.go("/")
    
app(target=main, assets_dir="assets")
#app(target=main, view=AppView.WEB_BROWSER)

