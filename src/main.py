import flet as ft
from math import pi,sqrt
def main(page: ft.Page):
    semiejeA = ft.TextField(label="Semieje A",hint_text="",keyboard_type=ft.KeyboardType.NUMBER)
    semiejeB = ft.TextField(label="Semieje B",hint_text="",keyboard_type=ft.KeyboardType.NUMBER)
    C = ft.Text(value="")

    def IngresarSemiejes(e):
        x = ((float(semiejeA.value)-float(semiejeB.value)) ** 2) / ((float(semiejeA.value)+float(semiejeB.value))**2)
        raiz=sqrt(4-3*x)
        numerador = 3*x
        denominador = 10 + raiz
        factor = 1 + numerador / denominador
        perimetro = pi * (float(semiejeA.value)+float(semiejeB.value)) * factor 
        C.value = str(perimetro) + "M"
    D = ft.Button(content="Calcular", on_click=IngresarSemiejes)
    page.add(
    ft.Container(
        content=ft.Column(
            controls=[semiejeA, semiejeB, D, C],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        expand=True,
        alignment=ft.Alignment.CENTER,
    )
)
ft.run(main)
