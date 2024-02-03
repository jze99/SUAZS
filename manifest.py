from flet import *

def main(page: Page):
    page.window_height = 600
    page.window_width = 600
    page.window_min_height = 600
    page.window_min_width = 600
    page.title = "СУАЗС"
    def PageLoading(route):
        print(page.route)
        page.views.clear()
        page.views.append()
    
app(target=main, assets_dir="assets")