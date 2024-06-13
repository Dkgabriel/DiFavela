import flet as ft 

def main(page: ft.Page):
    page.bgcolor = '#EBE6E0'
    page.fonts = {
        'popis' : 'assets/fonts/Poppis-SemiBold.tff',
        'aseinia' : 'assets/fonts/aseina-typeface.ttf'
    }
    image_fundo = ft.Container(
        ft.Image(src='assets/igms/tela_de_login_imgs/cervejafundo.png', repeat= ft.ImageRepeat.REPEAT,
        width= 10,         
        ),
        width= 800, height= 700,
        margin= ft.margin.all(-450)
    )

    header = ft.Row(
        controls=[
            
            ft.Container(
                width= 200,
                height= 200,
                bgcolor= '#F8A001',
                border_radius= 100,
                
                margin= ft.margin.only(-120,-80,40,0),
            ),
            ft.Text(
            value='Criar Conta de Vendedor', 
            color='black',
            text_align= ft.TextAlign.CENTER,
            size= 25,
            font_family= 'popis',
            weight= ft.FontWeight.BOLD,
            
            
            
            ),
            
        ],
        

    )
#parte cadastro

    image_cerveja = ft.Row(controls=[ft.Container(
       image_src= 'assets/igms/tela_de_login_imgs/cervejas.png',
       width= 100,
       height= 200,
       margin= ft.margin.only(230,-1820,0,0)
    )],
    alignment=ft.MainAxisAlignment.START,
    vertical_alignment= ft.CrossAxisAlignment.START,
    )
 #inputs
    inputs_cnpj_cadastro = ft.Container( ft.TextField(
        label='CNPJ', 
        adaptive= True,
        border_color= '#FFA815',
        border_radius= ft.border_radius.all(50),
        border_width= '2',
        max_length= '14',
        color= 'black',
        text_align= ft.TextAlign.CENTER,
        text_vertical_align= ft.VerticalAlignment.CENTER,
        label_style= ft.TextStyle(
            color= '#737373',
            font_family= 'popis',
            size= '17',
        ),),
        margin= ft.margin.only(0,40,0,0)
    )
    inputs_cpf_cadastro = ft.Container(ft.TextField(
        label='CPF', 
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
        ),
        margin= ft.margin.only(0,20,0,0)

        )

    inputs_email_cadastro = ft.Container( ft.TextField(
        label='Gmail', 
        adaptive= True,
        border_color= '#FFA815',
        border_radius= ft.border_radius.all(50),
        border_width= '2',
        color= 'black',
        text_align= ft.TextAlign.CENTER,
        text_vertical_align= ft.VerticalAlignment.CENTER,
        
        label_style= ft.TextStyle(
            color= '#737373',
            font_family= 'popis',
            size= '17',
            )
        ),
        margin= ft.margin.only(0,20,0,10),

    )

    inputs_senha_cadastro = ft.Container(ft.TextField(
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
            )),
            margin= ft.margin.only(0,20,0,10),
            )

    inputs_tell_cadastro = ft.Container(ft.TextField(
        label='Telefone', 
        adaptive= True,
        border_color= '#FFA815',
        border_radius= ft.border_radius.all(50),
        border_width= '2',
        color= 'black',
        text_align= ft.TextAlign.CENTER,
        text_vertical_align= ft.VerticalAlignment.CENTER,
        
        label_style= ft.TextStyle(
            color= '#737373',
            font_family= 'popis',
            size= '17',
            )
        ),
        margin= ft.margin.only(0,20,0,10),
        )
    
    ja_tenho_conta = ft.Container(
        ft.Text(
            spans=[
                ft.TextSpan(text='Já tem uma conta ? Venha fazer ', style= ft.TextStyle(
                    color='black', size= 19,
                )),
                ft.TextSpan(text='Login', style= ft.TextStyle(
                    color= '#F8A001', size= 19,
                ))
            ]

        ),
        alignment= ft.alignment.center,
    )
    bottom_cadastrar = ft.Container(
        ft.ElevatedButton(
        text='Cadastrar',
        color= 'black',
        bgcolor= '#F8A001',
        width= 400,
        height= 50,

        

        ),
        alignment= ft.alignment.center,
        margin= ft.margin.only(0,20,0,0)
    )
#container
    container_cadastro = ft.Container(
        height=900,
        width= 630,
        bgcolor= 'white',
        border_radius= ft.border_radius.only(50,50,0,0),
        shadow= ft.BoxShadow( color='black', blur_radius='10',),
        content= ft.Column(
            controls=[
                inputs_cnpj_cadastro,
                inputs_cpf_cadastro,
                inputs_email_cadastro,
                inputs_senha_cadastro,
                inputs_tell_cadastro,
                ja_tenho_conta,
                bottom_cadastrar,
            ],
            
        ),
        padding= ft.padding.all(20)
        
        
    )

    main = ft.Column(
        controls=[
            image_fundo,
            header,
            
            container_cadastro,
            image_cerveja,
        ],
        expand= True,
        alignment= ft.MainAxisAlignment.CENTER,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,     
        
        
    )

    page.add(main,)



   






ft.app(target=main, assets_dir= 'asstes')
