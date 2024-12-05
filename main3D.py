#!/usr/bin/env python3
from nicegui import app, ui

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=800) as scene:
    scene.spot_light(distance=100, intensity=0.1).move(-10, 0, 10)
    scene.stl('/stl/pikachu.stl').move(x=-0.5).scale(0.06)
    #scene.stl('/stl/utochka.stl').move(x=-0.5).scale(0.06)
    #const modelo = escena.getObjectByName('/stl/utochka.stl');
    #modelo.material.color.set(ffe58f);

ui.run()

# !/usr/bin/env python3
from nicegui import app, ui

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=800) as scene:
    scene.spot_light(distance=100, intensity=0.1).move(-10, 0, 10)

    # Carga el archivo STL y mueve el modelo
    model = scene.stl('/stl/utochka.stl').move(x=-0.5).scale(0.06)

    # Cambia el color del modelo (material del modelo)
    model.material({'color': '#E7DDFF'})  # Color hexadecimal amarillo claro
    #model.material(MeshBasicMaterial(color='#ffe58f'))  # Amarillo claro

ui.run()


'''

#!/usr/bin/env python3
from nicegui import app, ui

app.add_static_files('/stl', 'static')

with ui.scene(width=1024, height=800) as scene:
    scene.spot_light(distance=100, intensity=0.5).move(-10, 0, 10)

    # Cargar el archivo STL como malla
    model = scene.stl('/stl/utochka.stl').move(x=-0.5).scale(0.06)

    # Función para aplicar el color después de que el modelo se cargue
    def change_color():
        # Obtener el objeto Three.js y cambiar su material
        model.native_object.traverse(lambda obj: setattr(obj, 'material',
                                                         scene.material({'color': '#ffe58f'})))

    # Llamar a la función después de que el modelo se cargue completamente
    ui.timer(1, change_color)  # Espera 1 segundo antes de cambiar el color

ui.run()'''

