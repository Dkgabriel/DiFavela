import flet as ft
from flet import colors


botoes = [
    {'operador': 'AC','fonte':colors.BLACK,'fundo':colors.BLUE_GREY_100},
    {'operador': '+-','fonte':colors.BLACK,'fundo':colors.BLUE_GREY_100},
    {'operador': '%','fonte':colors.BLACK,'fundo':colors.BLUE_GREY_100},
    {'operador': '/','fonte':colors.WHITE,'fundo':colors.ORANGE_300},
    {'operador': '7','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '8','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '9','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '*','fonte':colors.WHITE,'fundo':colors.ORANGE_300},
    {'operador': '4','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '5','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '6','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '-','fonte':colors.WHITE,'fundo':colors.ORANGE_300},
    {'operador': '1','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '2','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '3','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '+','fonte':colors.WHITE,'fundo':colors.ORANGE_300},
    {'operador': ',','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '0','fonte':colors.WHITE,'fundo':colors.GREY_800},
    {'operador': '=','fonte':colors.WHITE,'fundo':colors.ORANGE_300},


    #{'operador': '9','fonte':colors.WHITE,'fundo':colors.GREY_800},


]

def main(page: ft.Page):
    page.bgcolor = 'black'
    page.window_resizable = False
    page.window_width = 300
    page.window_height = 380
    page.title = 'calculadora'
    page.window_always_on_top = True


    result = ft.Text(
        value='0', 
        color='white',
        size=20,
    )
    def calculate():
        pass

    def select(e):
        value_at = result.value if result.value != '0' else ''
        value = e.control.contente.value

        if value.issdigt():
            value = value_at = value
        elif value == 'AC':
            value = '0'
        else: 
            if value_at and value_at[-1] in ('/','*','-','+','.'):
                value_at = value_at[-1]
            
            value = value_at + value

            if value[-1] in ('=','%','+-'):
                value = calculate()
            
        result.value = value
        result.update()

    display = ft.Row(
        width= 250,
        controls=[result],
        alignment= 'end',
    )

    btn = [ft.Container(
        content= ft.Text(value=btn['operador'], color=btn['fonte']),
        width= 50,
        height= 50,
        bgcolor=btn['fundo'],
        border_radius= 100,
        alignment= ft.alignment.center,
        on_click=select,
        )for btn in botoes]
    
    
    keyboard = ft.Row(
        width= 250,
        wrap= True,
        controls=btn,
        alignment= 'end',
    )

    page.add(display, keyboard)






    

ft.app(target= main)