import flet as ft 

def main(page: ft.Page) -> None: 
    page.title = "Signup"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 400
    page.window.height= 400
    page.window_resizable = False

    #Setup our Fields 
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, pasword=True)
    checkbox_sign: Checkbox = Checkbox(label='i agree to stuff', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Sign Up', width=200, disabled=True)

    def validate(e: ControlEvent0) -> None: 
        if all([text_username.value, text_password.value, checkbox_sign.value]):
            button_submit.disabled = False
        else: 
            button_submit.disabled = True
        page.update()
    
    def submit(e: ControlEvent) -> None: 
        print("Username:", text_username.value)
        print("Password:", text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    checkbox_sign.on_change = validate
    text_username.on_change = validate 
    text_password.on_change = validate 
    button_submit.on_click = submit

    #Render the page sign-up page

    page.add(
        Row (
            controls = [
                Column (
                    [text_username,
                     text_password,
                     checkbox_sign,
                     button_submit]
                )
            ]
        )
    )



