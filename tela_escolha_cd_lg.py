import flet as ft  

def main(page: ft.Page):
 page.bgcolor = '#F8A001'
 page.vertical_alignment = ft.MainAxisAlignment.CENTER
 page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 
 texto = ft.Row(
    controls=[
     ft.Text(
    value= 'Como Você deseja se cadastrar?',
    color= 'black',
    text_align= ft.TextAlign.CENTER,
    size= 20,
    weight= ft.FontWeight.BOLD,
    ),
    
    ],
    
    alignment= ft.MainAxisAlignment.CENTER,
    
    
 )
 btRevendedor = ft.Row(
  controls=[
   ft.Container(
    ft.ElevatedButton(
     bgcolor= '#F8A001',
     width= 400,
     height= 60,
     text= 'Vendedor',
     color= 'black',),

     margin= ft.margin.only(0, 20, 0,0)
   )
  ],
  alignment= ft.MainAxisAlignment.CENTER,
 )
 
 
 btcliente = ft.Row(
  controls=[
   ft.Container(
    ft.ElevatedButton(
     bgcolor= '#F8A001',
     width= 400,
     height= 60,
     text= 'Comprador',
     color= 'black',),

     margin= ft.margin.only(0, 20, 0,0)
   )
  ],
  alignment= ft.MainAxisAlignment.CENTER,
 )

 card_escolha = ft.Container(
  bgcolor= 'white',
  width= 450,
  height= 250,
  border_radius= 30,
  content= ft.Column(
   controls=[
    texto,
    btRevendedor,
    btcliente,
   ]
  )
  )
 foto_cerveja = ft.Container(
        image_src= 'assets/igms/tela_de_login_imgs/cervejas.png',
        width= 450,
        height= 160,
        bgcolor= None,
        margin= ft.margin.only(0,0,0,-20),

    )

        

 main_principal = ft.Column(
    controls=[
     foto_cerveja,
     card_escolha,
     
    ]
 )

 page.add(main_principal)




















ft.app(target=main, assets_dir= 'asstes')
