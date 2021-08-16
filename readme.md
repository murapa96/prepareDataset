# Speech Dataset Generator

Esta aplicación permite crear _datasets_ para entrenar sintetizadores de _text to speech_. Fue desarrollado por la comunidad Deep-ESP.

## Requisitos

- Python 3
- Python packages (Podés instalarlos haciendo algo asi: `python -m pip install -r requirements.txt`)

## Ejemplo de uso

### 1. Descargar videos y sus subtitulos

Cargar en urls.txt los videos que queres descargar, estos deberían tener subtitulos.

Luego ejecutar `python main.py download urls.txt`

### 2. Corregir en audacity manualmente

Abrir los audios descargados en audacity, tambien importar los subtitulos yendo a File -> Import -> Labels. Corregir el timing de los labels.

### 3. Cortar audios y generar dataset final

Ya podemos cortar los audios y obtener el dataset final

Comando: `python main.py cut AUDIOS_FOLDER LABELS_FOLDER`

Ejemplo: `python main.py cut output labels`