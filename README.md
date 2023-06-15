<p></p>
<h1 align="center">Fiador 1.0</h1>
<img src="https://lpitac.github.io/exposicion/assets/img/captura_portada.svg" alt="">
<h3 align="center">La forma más sencilla de crear una exposición virtual a partir de una colección de objetos digitales y un CSV con sus metadatos.</h3>

<h4 align="center"><a href="#demo">Demo</a> &ensp;&bull;&ensp; <a href="#como">Cómo empezar</a> &ensp;&bull;&ensp; <a href="#tecnologias">Tecnologías empleadas</a> &ensp;&bull;&ensp; <a href="#licencia">Metadatos</a> &ensp;&bull;&ensp; <a href="#licencia">Licencia de uso</a></h4>

# Fiador 1.0
__Fiador__ es un software libre escrito en [Python](https://www.python.org) que permite hilar una colección de objetos digitales con su metadatos en formato CSV para crear una exposición virtual en formato web, lista para publicar, basándose en la plantilla [__Exposición__ __Virtual__](https://github.com/lpitac/exposicion).
El sitio web resultante se puede alojar en cualquier carpeta compartida de una red, en un servidor web básico (local o de internet) y en [GitHub](https://github.com/) (haciendo uso de [GitHub Actions Jekyll](https://jekyllrb.com/docs/continuous-integration/github-actions/) ).

## Exposición Virtual

__Exposición__ __Virtual__ es un _fork_ de [CollectionBuilder](https://collectionbuilder.github.io/), una __plantilla__ basada en [Jekyll](https://jekyllrb.com/) que permite crear un sitio web estático a partir de una colección de objetos digitales y un CSV con sus metadatos.

<a name="demo"></a>
# Demo
<p align="center">Exposición virtual de demostración:</p> 
<h3 align="center"><a href="https://lpitac.github.io/exposicion/" target="_blank">https://lpitac.github.io/exposicion/</a></h3>

----
<a name="como"></a>
# Cómo empezar
Hay dos formas de utilizar __Fiador__ junto con la plantilla __Exposición Virtual__: 
1. __Exposición de prueba__ : utiliza __los objetos digitales__ y el __CSV__ con sus metadatos incluidos en la __plantilla__ (podrás cambiarlos posteriormente).
2. __Exposición personalizada__: permite __definir los objetos digitales y el CSV__ que se utilizarán para generar el sitio web.

## | Opción 1 | Exposición de prueba
1. Descarga y ejecuta el instalador de [Fiador 1.0.](https://udcgal-my.sharepoint.com/:u:/g/personal/l_pitac_udc_es/EZV8a3fDB11MjyJX_hW9j4kBonbKsP6gluycy_odu1MKQA?e=jGuWOX) 
2. Pulsa sobre el botón __"Exposición de prueba"__.
3. Indica el __directorio__ donde deseas albergar los archivos de la exposición.
4. Pulsa sobre el botón __"Generar"__.

El proceso dará comienzo; puede tardar hasta 3 minutos en completarse. Una vez listo, se mostrará el mensaje __"Exposición creada correctamente"__. Al pulsar sobre el botón __"Ok"__ se abrirá automáticamente una ventana del navegador predeterminado en la página de inicio del sitio web generado.

<h4 align="center">¡Listo! Puedes navegar a través del sitio de forma local como si estuviese publicado en Internet.</h4>

## | Opción 2 | Exposición personalizada
1. Prepara los __metadatatos__ de tu colección siguiendo la __plantilla__ __de__ __prueba__ publicada en [Google Sheets](https://docs.google.com/spreadsheets/d/1nN_k4JQB4LJraIzns7WcM3OXK-xxGMQhW1shMssflNM/edit?usp=sharing). 
	 La forma más sencilla de utilizarla es haciendo una copia que deberás guardar en una cuenta de Google Drive. De este modo podrás editarla en línea, lo cual te resultará muy sencillo ya que se ha optimizado para facilitar su uso (campos desplegables, relleno automático, ...)
2. Reune en una carpeta todos los __objetos__ __digitales__ __descritos__ en el __CSV__.
3. Descarga, instala y ejecuta [Fiador 1.0.](https://udcgal-my.sharepoint.com/:u:/g/personal/l_pitac_udc_es/EZV8a3fDB11MjyJX_hW9j4kBonbKsP6gluycy_odu1MKQA?e=jGuWOX) 

---
<a name="tecnologias"></a>
# Tecnologías empleadas
La generación de las páginas necesarias para construir la exposición virtual basada en __HTML__, __CSS__ y __JavaScript__ se lleva a cabo con [Jekyll](https://jekyllrb.com/).  

## Tema de la plantilla 
El diseño del sitio web hace uso de [Bootstrap](https://getbootstrap.com/) un framework de código abierto que facilita la creación de interfaces web basadas en __HTML__, __CSS__ y __JavaScript__.

## Bibliotecas JavaScript
Para crear las distintas visualizaciones e interaciones sobre los objetos y sus metadatos se emplean las siguientes bibliotecas JavaScript: 

- __Galería de imágenes__: [Spotlight gallery](https://github.com/nextapps-de/spotlight)
- __Cargador de imágenes__: [lazysizes](https://github.com/aFarkas/lazysizes)
- __Tablas__: [DataTables](https://datatables.net/)
- __Mapas__: [Leafletjs](http://leafletjs.com/)
- __Buscador frontend__: [Lunr.js](https://lunrjs.com/)

<a name="metadatos"></a>
## Metadatos
Los metadatos utilizados de ejemplo cumplen los estándares [Schema.org](http://schema.org) y [Open Graph protocol](http://ogp.me/).

---
<a name="licencia"></a>
# Licencia
__Fiador__ está publicado bajo licencia [GNU General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.html).
---
2023 - Lorena P.C.