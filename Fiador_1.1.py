##########################
#                        #    
#      Fiador 1.1        #
#   2023 - Lorena P.C.   # 
#                        # 
##########################

import PySimpleGUI as sg
import urllib.request
import zipfile
import os
import shutil
import yaml
import socket
import subprocess
import threading
import webbrowser
import sys
import win32com.client
from win32com.shell import shell, shellcon

def main():
    # Establecer el tema de PySimpleGUI en "Default"
    sg.theme('Default')
    # Crear una ventana PySimpleGUI
    layout = [[sg.Col([[sg.Text()],
          [sg.Text('¡Bienvenid@ a Fiador!', font=('Cooper Black', 15), text_color='darkblue')],
          [sg.Text('Fiador le ayudará a crear y administrar una exposición virtual a partir de sus objetos digitales y un CSV con los metadatos.', size=(45, 2))],
          [sg.Button('Generar exposición', key='boton_generar_0', size=(15, 2), pad=((10, 10), (10, 10))), sg.Button('Editar exposición', key='boton_editar', size=(15, 2), pad=((0, 10), (10, 10))), sg.Button('Abrir exposición', key='boton_abrir_1', size=(15, 2), pad=((0, 10), (10, 10)))],
          [sg.Cancel('Cerrar', key='boton_cancelar_0', size=(10, 1), pad=((0, 0), (10, 10)))],
          [sg.Text('2023 | Lorena P.C.', text_color='darkblue', font=('Bookman Old Style', 10))]], element_justification='c')]] 

    window = sg.Window('Fiador', layout) # Título de la ventana

    while True:
        event, _ = window.read()
        if event in (sg.WINDOW_CLOSED, 'boton_cancelar_0'):
            break
        # BOTÓN "Generar exposición"
        elif event == 'boton_generar_0':
            # Cerrar la ventana actual
            window.close()
            # Crear una nueva ventana PySimpleGUI
            layout = [[sg.Col([[sg.Text()],
                [sg.Text('| Tipo de instalación |', size=(32, 1), text_color='darkblue', justification='center', font=('Bookman Old Style', 11))],
                [sg.Text('Puede comenzar con una instalación de prueba (con datos de ejemplo) o definir los suyos propios. En ambos casos podrá editarlos posteriormente.', size=(50, 3), justification='center')],
                [sg.Button('De prueba', key='boton_prueba', size=(15, 2), pad=((15, 0), (10, 10))), sg.Button('Personalizada', key='boton_personalizada', size=(15, 2), pad=((15, 0), (10, 10)))]], element_justification='c')]]

            window = sg.Window('Fiador - Generar exposición', layout) # Título de la ventana

            while True:
                event, _ = window.read()
                if event in (sg.WINDOW_CLOSED, 'boton_cancelar_1'):
                    break
                # BOTÓN "De prueba"
                elif event == 'boton_prueba':
                    # Cerrar la ventana actual
                    window.close()
                    # Crear una nueva ventana PySimpleGUI
                    layout = [
                        [sg.Text('')],
                        [sg.Text('| Exposición de prueba |', size=(43, 1), text_color='darkblue', justification='center', font=('Bookman Old Style', 11))],
                        [sg.Text('A continuación se generará una exposición con los datos incluidos en la plantilla "Exposición virtual".', size=(50, 2), justification='center')],
                        [sg.Text('Seleccione el directorio de instalación, pulse sobre el botón "Generar" y espere a que se complete el proceso.', size=(50, 2), justification='center')],
                        [sg.Text('Una vez finalizado, la exposición se abrirá automáticamente en una ventana del navegador.', size=(50, 2), justification='center')],
                        [sg.Text('Directorio de instalación:', text_color='darkblue')],
                        [sg.InputText(), sg.FolderBrowse('Examinar', key='directorio_instalacion')],
                        [sg.Button('Generar', key='boton_generar_1'), sg.Cancel('Cancelar', key='boton_cancelar_2')],
                        [sg.Text('', key='texto_estado')]  # Agregar elemento de texto para el estado
                    ]

                    window = sg.Window('Fiador - Generar exposición de prueba', layout) # Título de la ventana

                    while True:
                        event, values = window.read()
                        if event in (sg.WINDOW_CLOSED, 'boton_cancelar_2'):
                            window.close()
                            break
                        elif event == 'boton_generar_1':
                            if not values['directorio_instalacion']:
                                sg.popup('Debe seleccionar el directorio de instalación.')
                                continue
                            directorio_instalacion = values['directorio_instalacion']
                            carpeta_raiz = os.path.join(directorio_instalacion, 'exposicion-main')

                            # 1. INSTALAR PRERREQUISITOS
                            # URL de descarga de Ruby with Devkit 3.1.3-1-x64
                            url_ruby = 'https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.1.3-1/rubyinstaller-devkit-3.1.3-1-x64.exe'

                            # Nombre del fichero de instalación de Ruby with Devkit 3.1.3-1-x64
                            instalador = 'rubyinstaller-devkit-3.1.3-1-x64.exe'

                            # Descargar Ruby with Devkit 3.1.3-1-x64
                            window['texto_estado'].update('1/4: Descargando Ruby with Devkit 3.1.3-1-x64...')
                            window.refresh()  # Actualizar la ventana para mostrar el texto anterior
                            urllib.request.urlretrieve(url_ruby, instalador)

                            # Instalación desatendida de Ruby with Devkit 3.1.3-1-x64 sin MSYS2
                            window['texto_estado'].update('2/4: Instalando Ruby with Devkit 3.1.3-1-x64...')
                            window.refresh()  # Actualizar la ventana para mostrar el texto anterior
                            subprocess.call([f'{instalador}', '/tasks="assocfiles,modpath"', '/verysilent', '/norestart', '/no-ridk'])

                            # Eliminar archivo de instalación de Ruby with Devkit 3.1.3-1-x64
                            os.remove(instalador)

                            # 2. DESCARGAR PLANTILLA "EXPOSICIÓN VIRTUAL"
                            # URL de descarga de la plantilla
                            url_plantilla = "https://github.com/lpitac/exposicion/archive/refs/heads/main.zip"

                            # Nombre del fichero de la plantilla
                            nombre_fichero = "main.zip"

                            # Ruta completa de la ubicación de descarga
                            ruta_descarga = os.path.join(directorio_instalacion, nombre_fichero)

                            # Descargar la plantilla
                            window['texto_estado'].update('3/4: Descargando colección base...')
                            window.refresh()
                            urllib.request.urlretrieve(url_plantilla, ruta_descarga)

                            # Descomprimir el archivo descargado en la misma ubicación
                            with zipfile.ZipFile(ruta_descarga, 'r') as zip_ref:
                                zip_ref.extractall(os.path.dirname(ruta_descarga))

                            # 3. CONFIGURACIÓN BÁSICA
                            # Crear la ruta completa del archivo _config.yml
                            ruta_config = os.path.join(carpeta_raiz, '_config.yml').replace('\\', '/')

                            # Leer el archivo _config.yml
                            with open(ruta_config, 'r') as f:
                                config = yaml.safe_load(f)

                            # Modificar url y baseurl
                            baseurl = (carpeta_raiz).replace(os.path.abspath(''), '')[1:].replace('\\', '/').lstrip(':') + '/_site'
                            config['baseurl'] = baseurl
                            hostname = socket.gethostname()
                            url = '/''/' + hostname
                            config['url'] = url

                            # Escribir las variables en el archivo _config.yml
                            with open(ruta_config, 'w') as f:
                                yaml.dump(config, f)

                            # 4. GENERAR COLECCIÓN
                            window['texto_estado'].update('4/4: Generando colección...')
                            window.refresh()  # Actualizar la ventana para mostrar el texto anterior
                            process = None  # Declarar la variable process
                            os.chdir(carpeta_raiz) # Cambiar al directorio raíz de la colección

                            try:
                                # Instalar Jekyll (generador de sitios estáticos) y Bundler (gestor de dependencias de Ruby)
                                subprocess.call(['gem.cmd', 'install', 'jekyll', 'bundler'], stdout=subprocess.PIPE, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW)

                                # Ejecutar el servidor Jekyll
                                process = subprocess.Popen(['bundle.bat', 'exec', 'jekyll', 'serve'], stdout=subprocess.PIPE, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW)

                                while True:
                                    output = process.stdout.readline().strip()
                                    if output == '' and process.poll() is not None:
                                        break
                                    if "Server running... press ctrl-c to stop." in output:
                                        sg.popup('¡Exposición generada correctamente!')

                                        # Obtener la ruta completa a los archivos index.html y Fiador.exe
                                        ruta_index_html = os.path.join(carpeta_raiz, '_site', 'index.html')
                                        ruta_fiador_exe = os.path.join(carpeta_raiz, 'Fiador.exe')

                                        # Obtener la carpeta del escritorio
                                        ruta_escritorio = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0)

                                        # Crear un acceso directo al archivo index.html en el escritorio
                                        shortcut_index = win32com.client.Dispatch("WScript.Shell").CreateShortcut(os.path.join(ruta_escritorio, "Exposición virtual.lnk"))
                                        shortcut_index.TargetPath = ruta_index_html
                                        shortcut_index.Save()

                                        # Crear un acceso directo a Fiador.exe en el escritorio
                                        shortcut_fiador = win32com.client.Dispatch("WScript.Shell").CreateShortcut(os.path.join(ruta_escritorio, "Fiador.lnk"))
                                        shortcut_fiador.TargetPath = ruta_fiador_exe
                                        shortcut_fiador.Save()

                                        # Abrir en el navegador index.html
                                        webbrowser.open_new_tab(carpeta_raiz + '/_site/index.html')
                                        break
                            except subprocess.CalledProcessError as e:
                                sg.popup(f'Error al generar colección: {e}')
                            finally:
                                if process is not None and process.poll() is None:
                                    # Terminar el proceso bundle exec jekyll serve
                                    process.terminate()
                                # Terminar el proceso ruby.exe
                                subprocess.run(['taskkill', '/im', 'ruby.exe', '/f'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                            window.close()
                            break
                # BOTÓN "Personalizada"
                elif event == 'boton_personalizada':
                    # Cerrar la ventana actual
                    window.close()
                    # Crear una nueva ventana PySimpleGUI para ingresar la información personalizada
                    layout = [[sg.Text('| Exposición personalizada |', size=(43, 1), text_color='darkblue', justification='center', font=('Bookman Old Style', 11))],
                        [sg.Text('Indique a continuación los datos con los que generar la exposición.', size=(50, 2), justification='center')],
                        [sg.Text('Directorio de instalación *')],
                        [sg.InputText(), sg.FolderBrowse('Examinar', key='directorio_instalacion')],
                        [sg.Text('CSV con los metadatos')],
                        [sg.InputText(), sg.FileBrowse('Examinar', key='csv_metadatos')],
                        [sg.Text('Ubicación de los objetos digitales')],
                        [sg.InputText(), sg.FolderBrowse('Examinar', key='carpeta_objetos')],
                        [sg.Text('Imagen de portada')],
                        [sg.InputText(), sg.FileBrowse('Examinar', key='portada')],
                        [sg.Text('Título de la exposición')],
                        [sg.InputText(key='titulo')],
                        [sg.Text('Subtítulo de la exposición')],
                        [sg.InputText(key='subtitulo')],
                        [sg.Text('Descripción')],
                        [sg.InputText(key='descripcion')],
                        [sg.Text('Autor')],
                        [sg.InputText(key='autor')],
                        [sg.Button('Generar', key='boton_generar_2'), sg.Cancel('Cancelar', key='boton_cancelar_3')],
                        [sg.Text('* Campo obligatorio')],
                        [sg.Text('', key='texto_estado')]  # Agregar elemento de texto para el estado
                    ]

                    window = sg.Window('Fiador - Exposición personalizada', layout) # Título de la ventana

                    while True:
                        event, values = window.read()
                        if event in (sg.WINDOW_CLOSED, 'boton_cancelar_3'):
                            window.close()
                            break
                        elif event == 'boton_generar_2':
                            if not values['directorio_instalacion']:
                                sg.popup('Debe seleccionar el directorio de instalación.')
                                continue
                            directorio_instalacion = values['directorio_instalacion']
                            carpeta_raiz = os.path.join(directorio_instalacion, 'exposicion-main')

                            # 1. INSTALAR PRERREQUISITOS
                            # URL de descarga de Ruby with Devkit 3.1.3-1-x64
                            url_ruby = 'https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.1.3-1/rubyinstaller-devkit-3.1.3-1-x64.exe'

                            # Nombre del fichero de instalación de Ruby with Devkit 3.1.3-1-x64
                            instalador = 'rubyinstaller-devkit-3.1.3-1-x64.exe'

                            # Descargar Ruby with Devkit 3.1.3-1-x64
                            window['texto_estado'].update('1/4: Descargando Ruby with Devkit 3.1.3-1-x64...')
                            window.refresh()  # Actualizar la ventana para mostrar el texto anterior
                            urllib.request.urlretrieve(url_ruby, instalador)

                            # Instalación desatendida de Ruby with Devkit 3.1.3-1-x64 sin MSYS2
                            window['texto_estado'].update('2/4: Instalando Ruby with Devkit 3.1.3-1-x64...')
                            window.refresh()  # Actualizar la ventana para mostrar el texto anterior
                            subprocess.call([f'{instalador}', '/tasks="assocfiles,modpath"', '/verysilent', '/norestart', '/no-ridk'])

                            # Eliminar archivo de instalación de Ruby with Devkit 3.1.3-1-x64
                            os.remove(instalador)

                            # 2. DESCARGAR PLANTILLA "EXPOSICIÓN VIRTUAL"
                            # URL de descarga de la plantilla
                            url_plantilla = "https://github.com/lpitac/exposicion/archive/refs/heads/main.zip"

                            # Nombre del fichero de la plantilla
                            nombre_fichero = "main.zip"

                            # Ruta completa de la ubicación de descarga
                            ruta_descarga = os.path.join(directorio_instalacion, nombre_fichero)

                            # Descargar la plantilla
                            window['texto_estado'].update('3/4: Descargando colección base...')
                            window.refresh()
                            urllib.request.urlretrieve(url_plantilla, ruta_descarga)

                            # Descomprimir el archivo descargado en la misma ubicación
                            with zipfile.ZipFile(ruta_descarga, 'r') as zip_ref:
                                zip_ref.extractall(os.path.dirname(ruta_descarga))

                            # 3. CONFIGURACIÓN BÁSICA
                            
                            if values['portada']:
                                # Definir ubicación origen y nombre de la portada
                                ruta_origen_portada = values['portada']       
                                nombre_portada = "/" + os.path.basename(ruta_origen_portada)
                                
                                # Copiar el fichero de la portada a la carpeta raíz de la colección
                                shutil.copy(ruta_origen_portada, carpeta_raiz)
                                
                                # Crear la ruta completa del archivo theme.yml
                                ruta_theme = os.path.join(carpeta_raiz, '_data', 'theme.yml').replace('\\', '/')
                                
                                # Leer el archivo theme.yml
                                with open(ruta_theme, 'r') as f:
                                    config = yaml.safe_load(f)

                                # Modificar las variables con los valores introducidos por el usuario
                                config['featured-image'] = "/" + nombre_portada

                                # Escribir los cambios en el archivo theme.yml
                                with open(ruta_theme, 'w') as f:
                                    yaml.dump(config, f)
                            
                            # Crear la ruta completa del archivo _config.yml
                            config_path = os.path.join(carpeta_raiz, '_config.yml').replace('\\', '/')
                        
                            # Leer el archivo _config.yml
                            with open(config_path, 'r') as f:
                                config = yaml.safe_load(f)
                            
                            # Obtener el valor introducido por el usuario en el campo "titulo"
                            titulo = values['titulo']

                            # Verificar si se introdujo un valor en el campo "titulo"
                            if titulo.strip():
                                # Asignar el valor del campo "titulo" a "title"
                                config['title'] = titulo
                        
                            # Modificar las variables con los valores introducidos por el usuario
                            config['tagline'] = values['subtitulo']
                            config['description'] = values['descripcion']
                            config['author'] = values['autor']
                            baseurl = (carpeta_raiz).replace(os.path.abspath(''), '')[1:].replace('\\', '/').lstrip(':') + '/_site'
                            config['baseurl'] = baseurl
                            hostname = socket.gethostname()
                            url = '/''/' + hostname
                            config['url'] = url

                            # Escribir las variables en el archivo _config.yml
                            with open(config_path, 'w') as f:
                                yaml.dump(config, f)
                            
                            if values['csv_metadatos']:
                                # Definir ubicación origen y destino del CSV con los metadatos
                                ruta_origen_csv = values['csv_metadatos']
                                ruta_destino_csv = os.path.join(carpeta_raiz, '_data').replace('\\', '/')
                                
                                # Copiar el archivo CSV a la carpeta destino
                                shutil.copy2(ruta_origen_csv, ruta_destino_csv)
                            
                            if values['carpeta_objetos']:
                                # Definir ubicación origen y destino de los objetos digitales
                                ruta_origen_objetos = values['carpeta_objetos'] 
                                ruta_destino_objetos = os.path.join(carpeta_raiz, 'objects').replace('\\', '/')
                                
                                # Obtener la lista de archivos en la carpeta de origen
                                archivos = os.listdir(ruta_origen_objetos)

                                # Copiar cada archivo individualmente a la carpeta destino
                                for archivo in archivos:
                                    ruta_archivo_origen = os.path.join(ruta_origen_objetos, archivo)
                                    ruta_archivo_destino = os.path.join(ruta_destino_objetos, archivo)
                                    shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)
                            
                            # REGENERAR COLECCIÓN
                            process = None  # Declarar la variable process
                            os.chdir(carpeta_raiz)  # Cambiar a la carpeta raíz de la colección
                            window['texto_estado'].update('Guardando los cambios...')
                            window.refresh()  # Actualizar la ventana para mostrar el texto anterior
                           
                            try:
                                # Compilar la colección (ejecutar rake deploy)
                                process = subprocess.Popen(['rake.bat', 'deploy'], stdout=subprocess.PIPE, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW)

                                while True:
                                  output = process.stdout.readline().strip()
                                  if output == '' and process.poll() is not None:
                                      break
                                  if "Auto-regeneration: " in output:
                                      sg.popup('Cambios guardados correctamente')
                                      # Abrir en el navegador index.html
                                      webbrowser.open_new_tab(carpeta_raiz + '/_site/index.html')
                                      break   

                            except subprocess.CalledProcessError as e:
                                sg.popup_error(f'Error al generar colección: {e}')
                            finally:
                                if process is not None and process.poll() is None:
                                    # Terminar el proceso rake deploy
                                    process.terminate()
                                # Terminar el proceso ruby.exe
                                subprocess.run(['taskkill', '/im', 'ruby.exe', '/f'], creationflags=subprocess.CREATE_NO_WINDOW)

                                # Cerrar la ventana
                                window.close()
               
        #BOTÓN "Editar exposición"
        elif event == 'boton_editar': 
            # Cerrar la ventana actual
            window.close()
            # Crear una ventana PySimpleGUI
            layout = [
                [sg.Text('| CONFIGURACIÓN DE LA EXPOSICIÓN |', text_color='darkblue')],
                [sg.Text('Directorio raíz de la colección')],
                [sg.InputText(), sg.FolderBrowse('Examinar', key='carpeta_raiz')],
                [sg.Text('CSV con los metadatos')],
                [sg.InputText(), sg.FileBrowse('Examinar', key='csv_metadatos')],
                [sg.Text('Objetos digitales')],
                [sg.InputText(), sg.FolderBrowse('Examinar', key='carpeta_objetos')],
                [sg.Text('Imagen de portada')],
                [sg.InputText(), sg.FileBrowse('Examinar', key='portada')],
                [sg.Text('Título de la exposición')],
                [sg.InputText(key='titulo')],
                [sg.Text('Subtítulo de la exposición')],
                [sg.InputText(key='subtitulo')],
                [sg.Text('Descripción')],
                [sg.InputText(key='descripcion')],
                [sg.Text('Autor')],
                [sg.InputText(key='autor')],
                [sg.Button('Guardar', key='boton_guardar'), sg.Cancel('Cancelar', key='boton_cancelar_4')],
                [sg.Text('', key='texto_estado')]  # Agregar elemento de texto para el estado
            ]

            window = sg.Window('Fiador - Editar exposición', layout) # Título de la ventana

            while True:
                event, values = window.read()
                if event in (sg.WINDOW_CLOSED, 'boton_cancelar_4'):
                    window.close()
                    break
                elif event == 'boton_guardar':
                    # Obtener la ruta de la carpeta raiz de la exposición
                    carpeta_raiz = values['carpeta_raiz']
                if values['portada']:
                    # Definir ubicación origen y nombre de la portada
                    ruta_origen_portada = values['portada']       
                    nombre_portada = "/" + os.path.basename(ruta_origen_portada)
                    
                    # Copiar el fichero de la portada a la carpeta raíz de la colección
                    shutil.copy(ruta_origen_portada, carpeta_raiz)
                    
                    # Crear la ruta completa del archivo theme.yml
                    ruta_theme = os.path.join(carpeta_raiz, '_data', 'theme.yml').replace('\\', '/')
                    
                    # Leer el archivo theme.yml
                    with open(ruta_theme, 'r') as f:
                        config = yaml.safe_load(f)

                    # Modificar las variables con los valores introducidos por el usuario
                    config['featured-image'] = "/" + nombre_portada

                    # Escribir los cambios en el archivo theme.yml
                    with open(ruta_theme, 'w') as f:
                        yaml.dump(config, f)
                
                # Crear la ruta completa del archivo _config.yml
                config_path = os.path.join(carpeta_raiz, '_config.yml').replace('\\', '/')
            
                # Leer el archivo _config.yml
                with open(config_path, 'r') as f:
                    config = yaml.safe_load(f)
                
                # Obtener el valor introducido por el usuario en el campo "titulo"
                titulo = values['titulo']

                # Verificar si se introdujo un valor en el campo "titulo"
                if titulo.strip():
                    # Asignar el valor del campo "titulo" a "title"
                    config['title'] = titulo
            
                # Modificar las variables con los valores introducidos por el usuario
                config['tagline'] = values['subtitulo']
                config['description'] = values['descripcion']
                config['author'] = values['autor']
                baseurl = (carpeta_raiz).replace(os.path.abspath(''), '')[1:].replace('\\', '/').lstrip(':') + '/_site'
                config['baseurl'] = baseurl
                hostname = socket.gethostname()
                url = '/''/' + hostname
                config['url'] = url

                # Escribir las variables en el archivo _config.yml
                with open(config_path, 'w') as f:
                    yaml.dump(config, f)
                
                if values['csv_metadatos']:
                    # Definir ubicación origen y destino del CSV con los metadatos
                    ruta_origen_csv = values['csv_metadatos']
                    ruta_destino_csv = os.path.join(carpeta_raiz, '_data').replace('\\', '/')
                    
                    # Copiar el archivo CSV a la carpeta destino
                    shutil.copy2(ruta_origen_csv, ruta_destino_csv)
                
                if values['carpeta_objetos']:
                    # Definir ubicación origen y destino de los objetos digitales
                    ruta_origen_objetos = values['carpeta_objetos'] 
                    ruta_destino_objetos = os.path.join(carpeta_raiz, 'objects').replace('\\', '/')
                    
                    # Obtener la lista de archivos en la carpeta de origen
                    archivos = os.listdir(ruta_origen_objetos)

                    # Copiar cada archivo individualmente a la carpeta destino
                    for archivo in archivos:
                        ruta_archivo_origen = os.path.join(ruta_origen_objetos, archivo)
                        ruta_archivo_destino = os.path.join(ruta_destino_objetos, archivo)
                        shutil.copy2(ruta_archivo_origen, ruta_archivo_destino)
                
                # REGENERAR COLECCIÓN
                process = None  # Declarar la variable process
                os.chdir(carpeta_raiz)  # Cambiar a la carpeta raíz de la colección
                window['texto_estado'].update('Guardando los cambios...')
                window.refresh()  # Actualizar la ventana para mostrar el texto anterior
               
                try:
                    # Compilar la colección (ejecutar rake deploy)
                    process = subprocess.Popen(['rake.bat', 'deploy'], stdout=subprocess.PIPE, universal_newlines=True, creationflags=subprocess.CREATE_NO_WINDOW)

                    while True:
                      output = process.stdout.readline().strip()
                      if output == '' and process.poll() is not None:
                          break
                      if "Auto-regeneration: " in output:
                          sg.popup('Cambios guardados correctamente')
                          # Abrir en el navegador index.html
                          webbrowser.open_new_tab(carpeta_raiz + '/_site/index.html')
                          break   

                except subprocess.CalledProcessError as e:
                    sg.popup_error(f'Error al generar colección: {e}')
                finally:
                    if process is not None and process.poll() is None:
                        # Terminar el proceso rake deploy
                        process.terminate()
                    # Terminar el proceso ruby.exe
                    subprocess.run(['taskkill', '/im', 'ruby.exe', '/f'], creationflags=subprocess.CREATE_NO_WINDOW)

                    # Cerrar la ventana
                    window.close()
                      
        #BOTÓN "Abrir exposición"
        elif event == 'boton_abrir_1':
            # Cerrar la ventana actual
            window.close()
            # Crear una ventana PySimpleGUI
            layout = [
                [sg.Text('Seleccione el directorio raíz de la colección')],
                [sg.InputText(), sg.FolderBrowse('Examinar', key='directorio_raiz')],
                [sg.Button('Abrir', key='boton_abrir_2'), sg.Cancel('Cancelar', key='boton_cancelar_5')],
            ]

            window = sg.Window('Fiador - Abrir exposición', layout) # Título de la ventana

            while True:
                event, values = window.read()
                if event in (sg.WINDOW_CLOSED, 'boton_cancelar_5'):
                    window.close()
                    break
                elif event == 'boton_abrir_2':
                  if not values['directorio_raiz']:
                     sg.popup('Debe seleccionar el directorio raiz de la exposición.')
                     continue
                  directorio_raiz = values['directorio_raiz']
                  # Abrir en el navegador index.html
                  webbrowser.open_new_tab(directorio_raiz + '/_site/index.html')
                  # Cerrar la ventana
                  window.close()
if __name__ == '__main__':
    
    main()              
