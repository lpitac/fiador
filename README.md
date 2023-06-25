<p></p>
<h1 align="center">Fiador</h1>

<h1 align="center"><img src="https://github.com/lpitac/fiador/blob/main/portada_fiador.svg"></h1>

> <h3 align="center">La forma más sencilla de crear una exposición virtual a partir de una colección de objetos digitales y un CSV con sus metadatos.</h3>

<h3 align="center"><a href="#demo">Demo</a> &ensp;&bull;&ensp; <a href="#como">Cómo empezar</a> &ensp;&bull;&ensp; <a href="#funcionamiento">Cómo funciona</a> &ensp;&bull;&ensp; <a href="#tecnologias">Tecnologías empleadas</a> &ensp;&bull;&ensp; <a href="#licencia">Licencia</a></h3>

# Fiador
__Fiador__ es un software libre escrito en [Python](https://www.python.org) que permite _hilar_ una __colección de objetos digitales__ y sus __metadatos__ en formato __CSV__, para crear un sitio web basado en la plantilla [___Exposición Virtual___](https://github.com/lpitac/exposicion).

El sitio web resultante se puede alojar en un servidor web básico (local o de internet) o en [GitHub](https://github.com/) (haciendo uso de [GitHub Actions Jekyll](https://jekyllrb.com/docs/continuous-integration/github-actions/)).

__Fiador__ ha sido desarrollado bajo principios de __computación mínima__, con el objetivo de que su uso requiera de los __mínimos recursos__ de __hardware__, __software__ y __conocimientos informáticos__.

<div align="center">
  <h3>
    <img src="https://github.com/lpitac/fiador/blob/main/iconos/descargar.png" alt="Icono de Descargar" style="vertical-align: middle;">
    <a href="https://purl.org/fiador/exe">Descargar Fiador</a>
  </h3>
</div>

<a name="demo"></a>
# Demo
<h3 align="center">Exposición virtual de demostración</h3> 
<img src="https://github.com/lpitac/fiador/blob/main/capturas/captura_portada.png" alt="">
<h3 align="center"><a href="https://lpitac.github.io/exposicion/" target="_blank">https://lpitac.github.io/exposicion/</a></h3>

----
<a name="como"></a>
# Cómo empezar
[__Fiador 1.1__](https://purl.org/fiador/exe) ofrece tres funcionalidades:
1. Generar una exposición.
2. Editarla.
3. Abrirla.

<h1 align="center"><img src="https://github.com/lpitac/fiador/blob/main/capturas/ventana_ppal_fiador.png"></h1>

## Generar una exposición
Hay dos formas de utilizar [__Fiador 1.1__](https://purl.org/fiador/exe) junto con la plantilla [___Exposición Virtual___](https://github.com/lpitac/exposicion): 
1. __Exposición de prueba__: utiliza __los objetos digitales__ y el __CSV__ con sus metadatos incluidos en la __plantilla__.
2. __Exposición personalizada__: permite __definir los objetos digitales y el CSV__ que se utilizarán para generar el sitio web. 

En ambos casos podrás editar los datos posteriormente.

<p align="center"><img src="https://github.com/lpitac/fiador/blob/main/capturas/ventana_generar_expo.png"></p>

### | Opción 1 | Exposición de prueba
1. Descarga y ejecuta [__Fiador 1.1__](https://purl.org/fiador/exe).
2. Pulsa sobre el botón __"Generar exposición"__.
3. Pulsa sobre el botón __"Exposición de prueba"__.
4. Indica el __directorio__ donde deseas albergar los archivos de la exposición.
5. Pulsa sobre el botón __"Generar"__.

El proceso puede tardar __varios minutos__ en completarse. Una vez listo, se mostrará el mensaje __"¡Exposición generada correctamente!"__. 

<p align="center"><img src="https://github.com/lpitac/fiador/blob/main/capturas/ventana_ok.png"></p>

Al pulsar sobre el botón __"Ok"__ la exposición se abrirá automáticamente en una ventana del navegador.

> <h3 align="center">¡Listo! Ya puedes navegar a través de la exposición web generada.</h3>

<p></p>

### | Opción 2 | Exposición personalizada
1. Prepara los __metadatatos__ de tu colección en formato __CSV__ siguiendo la __plantilla__ __de__ __prueba__ publicada en [Google Sheets](https://docs.google.com/spreadsheets/d/1nN_k4JQB4LJraIzns7WcM3OXK-xxGMQhW1shMssflNM/edit?usp=sharing). | Wiki -[¿Cómo utilizar la plantilla de prueba](https://github.com/lpitac/fiador/wiki/Metadatos) |
2. Reúne en una carpeta todos los __objetos__ __digitales__ __descritos__ en el __CSV__. | Wiki - [Formatos compatibles](https://github.com/lpitac/fiador/wiki/Objetos-digitales) |
3. Descarga y ejecuta [__Fiador 1.1__](https://purl.org/fiador/exe) 
4. Pulsa sobre el botón __"Generar exposición"__.
5. Pulsa sobre el botón __"Exposición personalizada"__.
	- Selecciona el __directorio__ donde deseas albergar los archivos de la exposición.
	- Selecciona el __directorio__ donde se encuentra el __CSV__ con los __metadatos__.
	- Selecciona el __directorio__ donde se encuentran los __objetos digitales__.
	- Cubre el resto de parámetros solicitados (__título__, __descripción__, ...).
8. Pulsa sobre el botón __"Generar"__.

El proceso puede tardar __varios minutos__ en completarse. Una vez listo, se mostrará el mensaje __"¡Exposición generada correctamente!"__. 

<p align="center"><img src="https://github.com/lpitac/fiador/blob/main/capturas/ventana_ok.png"></p>

Al pulsar sobre el botón __"Ok"__ la exposición se abrirá automáticamente en una ventana del navegador.

> <h3 align="center">¡Listo! Ya puedes navegar a través de la exposición web generada.</h3>

<p></p>

----

<a name="funcionamiento"></a>
# Cómo funciona Fiador
__Fiador__ simplifica la creación de una exposición virtual en formato web haciendo uso de [Jekyll](https://jekyllrb.com/), un generador de sitios webs estáticos escrito en [Ruby](https://www.ruby-lang.org/es/), y de la plantilla [___Exposición virtual___](https://github.com/lpitac/exposicion), un _fork_ de [CollectionBuilder](https://collectionbuilder.github.io/).
De este modo una vez ejecutado el instalador __se llevará a cabo automáticamente todo el proceso de generación de la exposición virtual__, que consta de cuatro fases:

### 1. Instalación de prerrequisitos</h3></summary>

- Descarga de [Ruby with Devkit 3.1.3-1-x64](https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-3.1.3-1/rubyinstaller-devkit-3.1.3-1-x64.exe).
- Ejecución del instalador `rubyinstaller-devkit-3.1.3-1-x64.exe` de forma desatendida sin MSYS2.
- Descarga de la plantilla [___Exposición virtual___](https://github.com/lpitac/coleccion-base/archive/refs/heads/main.zip) en la ubicación seleccionada por el usuario.
- Descompresión del archivo en la misma ubicación.

### 2. Configuración básica</h3></summary>
		
- Copia del archivo de la __portada__ indicada por el usuario a la carpeta raíz de la exposición.
- Modificación del valor de ___featured-image___ en el archivo ___/_data/theme.yml___, con la ruta al archivo de la portada en la carpeta raíz de la exposición.
- Modificación en el archivo ____config.yml___ del valor de los siguientes parámetros por los indicados por el usuario: 
	- ___title___
	- ___subtitle___
	- ___description___
	- ___author___
	- ___base___: se genera automáticamente tomando la ubicación de la carpeta raíz seleccionada por el usuario.
	- ___baseurl___: se genera automáticamente tomando la ubicación de la carpeta raíz seleccionada por el usuario.
			
### 3. Carga de los datos

- Copia de los __objetos digitales__ de la ubicación indicada por el usuario a la carpeta ___objects___, ubicada en la raíz de la exposición.
- Copia del __CSV__ con los metadatos de la ubicación indicada por el usuario a la carpeta  ____data___, ubicada en la raíz de la exposición.
		
### 4. Generación de la exposición

- Instalación de [Jekyll](https://www.jekyll.com.cn/tutorials/using-jekyll-with-bundler/) y [Bundle](https://www.jekyll.com.cn/tutorials/using-jekyll-with-bundler/).
- Ejecución del servidor [Jekyll](https://jekyllrb.com/docs/step-by-step/01-setup/).
- Apertura de ___index.html___ en el navegador.

<a name="tecnologias"></a>
# Tecnologías empleadas
La generación de las páginas necesarias para construir la exposición virtual se basa en __HTML__, __CSS__ y __JavaScript__ y se lleva a cabo con [Jekyll](https://jekyllrb.com/).  

## Tema de la plantilla 
El diseño del sitio web hace uso de [Bootstrap](https://getbootstrap.com/) un framework de código abierto que facilita la creación de interfaces web basadas en __HTML__, __CSS__ y __JavaScript__.

## Bibliotecas JavaScript
Para crear las distintas visualizaciones e interaciones sobre los objetos y sus metadatos se emplean las siguientes bibliotecas JavaScript: 

- __Galería de imágenes__: [Spotlight gallery](https://github.com/nextapps-de/spotlight)
- __Cargador de imágenes__: [lazysizes](https://github.com/aFarkas/lazysizes)
- __Tablas__: [DataTables](https://datatables.net/)
- __Mapas__: [Leafletjs](http://leafletjs.com/)
- __Buscador frontend__: [Lunr.js](https://lunrjs.com/)

## Metadatos
Los metadatos utilizados de ejemplo cumplen los estándares [Schema.org](http://schema.org) y [Open Graph protocol](http://ogp.me/).

---
<a name="licencia"></a>
# Licencia

__Fiador__ está publicado bajo licencia [GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.html).

---
2023 - Lorena P.C.
