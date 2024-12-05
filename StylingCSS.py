from nicegui import ui

ui.icon('thumb_up', color='red').classes('text  32xl')
ui.markdown('This is **Markdown**.')
ui.html('This is <strong>HTML</strong>.')
with ui.row():
    ui.label('Brenda').style('color: #cad18a; font-weight: bold;  font-family: "Georgia";font-size: 32px')
    ui.label('Tailwind').classes('font-serif')
    ui.label('Quasar').classes('q-ml-xl')
ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run()