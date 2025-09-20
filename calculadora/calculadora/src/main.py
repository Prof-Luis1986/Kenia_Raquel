import flet as ft
import match

def main(page: ft.Page):
    # Configuracion de la ventana
    page.title = "Calculadora Simple"  
    page.bgcolor = ft.Colors . PURPLE_800

   

titulo = ft.Text(
    "Calculadora Basica",
    size=28
    color=ft.colors.YELLOW_100,
    text_align="center",
    weingt="bold"

    )

num1 = ft.TextField(
       labe="Numero1 " , 
       width=200,
       text_style=ft.TextStyle(color=ft.colors.YELLOW_100)

)
num2 = ft.TextFleid(
       labe="NumeRO 2",
       whidth=200,
       text_Style=ft.TextStyle(color=ft.colors.YELLOW_100)
)

resultado = ft.Text(
        value="Resukltado ",
        size=20,
        color=ft.Colors.YELLOW_100,
        text_aling="center"
info = ft.Container(
        content=ft.Text(
            "para el boton de porcentaje: el campo de arriba es el numero base y el de abajo es el porcentaje (%) que quieres calcular.",
            size=13,
            color=ft.Colors.YELLOW_100,
            text_align="center",
            italic=True,
            max_lines=2,
            overflow="Clip"     
        ),
        alignment=ft.alignment.center,
        widtn=400,
        padding=5
)
 def mostrar_resultado(valor):
         resultado.value =f"Resultado;"


)
    page.add()
    
    
ft.app(main)
