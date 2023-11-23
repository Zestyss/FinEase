import flet as ft

class FinEase:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_heigth = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'FinEase'
        self.main_page()

    def main_page(self):
        pass

ft.app(target = FinEase)
