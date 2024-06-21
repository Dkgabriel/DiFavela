import flet as ft 

def main(page: ft.Page):
    page.bgcolor = '#EBE6E0'
    page.fonts = {
        'popis' : 'assets/fonts/Poppis-SemiBold.tff',
        'aseinia' : 'assets/fonts/aseina-typeface.ttf'
    }
    

    image_fundo = ft.Container(
        image_src='assets/igms/tela_principal/fundocerveja.png',
        width= 900,
        height= 1900,
        image_repeat= ft.ImageRepeat.REPEAT,

    )
    infosbar = ft.Container(
        width= 100,
        height= 1100,
        bgcolor= '#F8A001',
        margin= ft.margin.only(-10,-10,0,-10)
    )
    #topo 

    DifavelaNome= ft.Text(
        value='DiFavela',
        color= 'black',
        size= 60,
        text_align= ft.TextAlign.CENTER,
        font_family= 'aseinia'
        
    )
    bolsaMarket = ft.Container(
        image_src='assets/igms/tela_principal/bolsaMarket.png',
        width= 50,
        height= 50,
        margin= ft.margin.only(100)
    )

    topo = ft.Row(
        controls=[DifavelaNome, bolsaMarket],
        width= 200,
        alignment= ft.MainAxisAlignment.CENTER,

        
    )
    #card de mais vendidos
    card_mais_vendidos = ft.Row(
        controls=[
            ft.Container(
                bgcolor= '#F8A001',
                width= 400,
                height= 300,
                margin= ft.margin.all(10),
                border_radius= ft.border_radius.all(20),
                content= ft.Text(value=' Card de Mais vendidos')
        ),
        ],
        width= 150,
        alignment= ft.MainAxisAlignment.CENTER,
    )

    #card de vendaas
    card_vendas = ft.Row(
        controls=[
            bg_cardVendas,
            img_cardVendas,
        ],
        width=200,
        height=100,
    )
    bg_cardVendas = ft.Container(
        bgcolor='#F8A001'
    )
    img_cardVendas =  ft.Container(
        bgcolor='white'
    )
    
    #conteudo principal
    conteudoprincipal = ft.Container(
        image_src='assets/igms/tela_principal/fundocerveja.png',
        width= 1500,
        image_repeat= ft.ImageRepeat.REPEAT,
        content= ft.Column(
            controls=[ 
                topo,
                card_mais_vendidos,
                card_vendas,
            ],
            expand= True,
        ),
        margin= ft.margin.only(-10,-10,-10,-10)
        
       
    )

    #estrutura da tela 

    mainprincipal = ft.Row(
        controls=[
            infosbar,
            conteudoprincipal,

        ],
        expand= True,
    )


    page.add(mainprincipal)
   






ft.app(target=main, assets_dir= 'asstes')
