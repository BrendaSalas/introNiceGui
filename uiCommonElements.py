from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

ui.button('Haz click', on_click=lambda: ui.notify('Hiciste Click'))
with ui.row():
    ui.checkbox('Verificar', on_change=show)
    ui.switch('Cambiar', on_change=show)
ui.radio(['Rosa', 'Verde', 'Azul'], value='Rosa', on_change=show).props('inline')
with ui.row():
    ui.input('Ingresar Texto', on_change=show)
    ui.select(['Uno', 'Dos'], value='Uno', on_change=show)
ui.link('Ver mas...', '/documentation').classes('mt-8')

ui.run()