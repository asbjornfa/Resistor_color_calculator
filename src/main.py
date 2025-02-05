from tkinter.constants import CENTER

import flet as ft
from flet.core.safe_area import SafeArea


def main(page: ft.Page) -> None:
    page.adaptive = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "GridView Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.update()


    colors: list[list[str]] = [
        ["black", "black", "black", "black"],
        ["brown", "brown", "brown", "brown"],
        ["red", "red", "red", "red"],
        ["orange", "orange", "orange", "orange"],
        ["yellow", "yellow", "yellow", "yellow"],
        ["green", "green", "green", "green"],
        ["blue", "blue", "blue", "blue"],
        ["purple", "purple", "purple", "purple"],
        ["grey", "grey", "grey", "grey"],
        ["white", "white", "white", "white"]]

    b_values: list[list[str]]= [
        ["0", "0", "1", "0"],
        ["1", "1", "10", "1"],
        ["2", "2", "100", "2"],
        ["3", "3", "1k", "0"],
        ["4", "4", "10k", "0"],
        ["5", "5", "100k", "0.5"],
        ["6", "6", "1000k", "0.25"],
        ["7", "7", "10000k", "0.1"],
        ["8", "8", "0", "0.05"],
        ["9", "9", "0", "0"]]

    buttons = ft.GridView(
        expand=2,
        child_aspect_ratio=1.0,
        runs_count=4,
        run_spacing=10,
        spacing=10,
    )

    page.add(buttons)
    for row in range(10):
        for col in range(4):
            buttons.controls.append(
                ft.Container(
                ft.CupertinoButton(
                    content=ft.Text(
                        b_values[row][col],
                        color=ft.CupertinoColors.WHITE,
                        size= 12
                    ),
                    padding=20,
                    alignment=ft.alignment.center,
                    bgcolor=colors[row][col],
                    opacity_on_click=0.3,
                    border_radius=2,
                    on_click=lambda e, value=b_values[row][col]: print(f"{value}")
                ),
                )
            )


    page.add(buttons)
    page.update()


ft.app(main)
