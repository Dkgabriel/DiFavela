import flet as ft 

def main(page: ft.Page):
    page.bgcolor = '#F8A001'
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.fonts = {
        'popis' : 'assets/fonts/Poppis-SemiBold.tff',
        'aseinia' : 'assets/fonts/aseina-typeface.ttf'
    }
    ...

    foto_cerveja = ft.Container(
        image_src= 'assets/igms/tela_de_login_imgs/cervejas.png',
        width= 450,
        height= 160,
        bgcolor= None,
        margin= ft.margin.symmetric(-36,0)
    )

    
    inputs_cpf_login = ft.TextField(
        label='CPF OU CNPJ', 
        adaptive= True,
        border_color= '#FFA815',
        border_radius= ft.border_radius.all(50),
        border_width= '2',
        max_length= '11',
        color= 'black',
        text_align= ft.TextAlign.CENTER,
        text_vertical_align= ft.VerticalAlignment.CENTER,
        label_style= ft.TextStyle(
            color= '#737373',
            font_family= 'popis',
            size= '17',
            )
        )
    inputs_senha_login = ft.TextField(
        label='Senha', 
        adaptive= True,
        border_color= '#FFA815',
        border_radius= ft.border_radius.all(50),
        border_width= '2',
        color= 'black',
        text_align= ft.TextAlign.CENTER,
        text_vertical_align= ft.VerticalAlignment.CENTER,
        password=True,
        can_reveal_password=True,
        label_style= ft.TextStyle(
            color= '#737373',
            font_family= 'popis',
            size= '17',
            )
        
        
        )
    
    bola_detalhes_top = ft.Row(
        controls=[
            ft.Container(
                bgcolor= '#EBE6E0',
                width= 250,
                height= 250,
                border_radius= ft.border_radius.all(150),
                alignment= ft.alignment.top_left,
                margin= ft.margin.only(-100,-90,0,0)
    )
        ]
    )

    bola_detalhes_bottom = ft.Row(
        controls=[
            ft.Container(
                bgcolor= '#EBE6E0',
                width= 250,
                height= 250,
                border_radius= ft.border_radius.all(150),
                alignment= ft.alignment.bottom_left,
                margin= ft.margin.symmetric(0,-100),),
        ],
        alignment= ft.MainAxisAlignment.END,
        
        
    )   
    
    bottom_login = ft.ElevatedButton(
        text='Logar',
        color= 'black',
        bgcolor= '#FFA815',
        width= 500,
        height= 40,
        

        )
    nome_di_favela = ft.Container(
    margin= ft.margin.only(0,80, 0, 19),
    content= ft.Text(value= 'Di Favela',
        color= 'black',
        size= '45',
        text_align= ft.TextAlign.CENTER,
        font_family= 'aseinia',
     ),
        
    
    )

    text_ja_tenho_login = ft.Row(
        controls=[ 
            ft.Text(spans=[
                ft.TextSpan(text='QUERO CRIAR UMA ',style= ft.TextStyle(color= '#737373',)),
                ft.TextSpan(text='CONTA',style= ft.TextStyle(color='black',)),
            ])
        ],
        alignment= ft.MainAxisAlignment.CENTER,
        
    )
    container_login = ft.Container(
        bgcolor= '#EBE6E0',
        border_radius= ft.border_radius.all(50),
        width= 660,
        height= 350,
        alignment= ft.alignment.center,
        padding= ft.padding.symmetric(40, 20),
        margin= ft.margin.symmetric(0,120), 
       
        
        content= ft.Column(
            controls= [
                inputs_cpf_login,
                inputs_senha_login,
                bottom_login,
                text_ja_tenho_login,
                
            ],
            expand= True,
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            
        )
    )

    ipt_cpf = ft.TextField(label='Cpf'),

    
    principal = ft.Column(
        
        controls=[
            bola_detalhes_top,
            nome_di_favela,
            
            foto_cerveja,
            container_login,
            bola_detalhes_bottom,
           
            ],
        alignment= ft.MainAxisAlignment.CENTER,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,
        
        
       
        
        )


    page.add(principal,)








ft.app(target=main, assets_dir= 'asstes')
