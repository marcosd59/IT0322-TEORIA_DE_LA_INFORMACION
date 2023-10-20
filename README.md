
## <font color="red"> **Actualización: "Se agregan 4 codificaciones de compresion de datos"** </font>

# Esquema de comunicación

Se realizara un programa en Python que simule un esquema de comunicación con los sigueintes puntos:

1. **Fuente de información:** Selecciona el mensaje deseado de un conjunto de mensajes posibles.

2. **Transmisor:** Transforma o codifica esta información en una forma apropiada al canal.
3. **Canal:** Medio a través del cual las señales son transmitidas al punto de recepción.
4. **Receptor:** Decodifica o vuelve a transformar la señal transmitida en el mensaje original o en una aproximación de este haciéndolo llegar a su destino.
5. **Destino de información:** Muestra el mensaje decodificado.


---



#### **1. Fuente de información**
El primer paso en nuestro esquema de comunicacion es la fuente de infomacion, osea el mensaje.

- En esta etapa, crearemos un archivo de texto llamado "fuente.txt" que contendrá la información que servirá como fuente de datos en nuestro sistema de comunicación.

- Luego, se implementará una función para leer y extraer el contenido de este archivo.

Hay que tener en cuenta que para crear el archivo "fuente.txt" manualmente, podemos utilizar un editor de texto y guardarlo en la misma ubicación donde se encuentra el script de Python. Luego, podemos usar el código en Python para leerlo.

```
# Se uso a chatGPT para generar la funcion para poder leer un archivo de texto.
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return ""
```
---
#### **2. Transmisor**
Es el emisor técnico, esto es el que transforma el mensaje emitido en un conjunto de señales o códigos que serán adecuados al canal encargado de transmitirlos.

En este caso, vamos a utilizar el archivo de texto y convertir su contenido a código ASCII y luego a representación binaria para la transmisión.

Ahora explicare mas a detalle esta parte:

1. Leer contenido del archivo de texto:

Inicialmente, hemos leído el contenido del archivo de texto llamado "fuente.txt" en la etapa de la "Fuente de Información". Este contenido se almacena en la variable contenido_fuente que sera el mensaje.

2. Convertir a código ASCII:

En la etapa de la "Fuente de Información", hemos convertido el contenido del archivo de texto en una lista de códigos ASCII utilizando la función texto_a_ascii. Cada carácter del texto se representó como su correspondiente valor ASCII.

3. Convertir a representación binaria (Adicional):

Para llevar a cabo la conversión a una representación binaria, podemos agregar una función adicional para realizar esta conversión. Por ejemplo:

```
def texto_a_ascii(texto):
    ascii_codigos = [ord(char) for char in texto]
    return ascii_codigos
```

---
#### **3. Canal**
Es el medio técnico que debe transportar las señales codificadas por el transmisor. Este medio será, en este caso la simulación de, cables, fibra óptica o por aire.

A continuación, explicare cómo planeo simular esta parte:

1. Agregar Ruido al Mensaje Transmitido:

En el código podemos agregar un ruido aleatorio al mensaje transmitido. Para esto podemos crear una funcion llamada agregar_ruido.

2. Probabilidad de Ruido:

Debemos ajustar la variable "probabilidad_ruido" para controlar la cantidad de ruido que deseamos simular en el canal de comunicación. Un valor más alto de "probabilidad_ruido" significa más ruido y una mayor probabilidad de errores.

3. Función para Agregar Ruido:

Aquí está una version beta de como seria esta funcion en Python:

```
def agregar_ruido(mensaje, probabilidad):
    mensaje_con_ruido = ""
    for bit in mensaje:
        if random.random() < probabilidad:
            # Simulamos un error al cambiar el bit con probabilidad 'probabilidad'
            mensaje_con_ruido += '1' if bit == '0' else '0'
        else:
            mensaje_con_ruido += bit
    return mensaje_con_ruido

```

---
#### **4. Receptor**

La actividad del receptor es la inversa de la del transmisor. Su función consiste en decodificar el mensaje transmitido y conducirlo por el canal, para transcribirlo en un lenguaje comprensible por el verdadero receptor que es llamado destinatario.

1. Recepción del Mensaje Transmitido:

El receptor comienza recibiendo el mensaje transmitido. En el código existente, esto se logra mediante la variable "mensaje_con_ruido", que contiene el mensaje afectado por el ruido.

2. Decodificación:

El receptor decodifica la señal para obtener la información en su forma original. Si en el "Transmisor" convertimos la información a representación binaria, debemos realizar la conversión inversa para obtener los códigos ASCII o el formato original de los datos.

```
def binario_a_ascii(binario):
    # Divide la cadena binaria en segmentos de 8 bits y conviértelos a valores ASCII
    ascii_codigos = [int(binario[i:i+8], 2) for i in range(0, len(binario), 8)]

    # Convierte los códigos ASCII a caracteres y forma el mensaje de texto
    mensaje_texto = "".join(chr(codigo) for codigo in ascii_codigos)

    return mensaje_texto
```
---
#### **5. Destino de información**

El "Destino de Información" o "Destinatario," simplemente recibe el mensaje procesado y lo utiliza según su aplicación específica. En este caso el destinatario simplemente imprimirá el mensaje en su forma original (texto ASCII).

Codigo:

```
# 5. Destino de Información (Destinatario)
mensaje_destino = mensaje_recibido  # En este ejemplo, el mensaje en su forma original

# Imprimir el mensaje en el destinatario
mensaje_texto = "".join(chr(int(mensaje_destino[i:i+8], 2)) for i in range(0, len(mensaje_destino), 8))
print("Mensaje en el Destinatario: ", mensaje_texto)

```

- "mensaje_recibido" es el mensaje que ha sido procesado y que ahora se encuentra en su forma recuperada después de haber pasado por el "Receptor."

- Luego, convertimos la representación binaria nuevamente a texto ASCII. Suponemos que el mensaje original estaba en formato ASCII y, por lo tanto, cada conjunto de 8 bits se interpreta como un carácter ASCII. Usamos chr para convertir estos valores numéricos en caracteres ASCII.

- Finalmente, el mensaje en su forma original se imprime en el destinatario.

> # <font color="4169E1"> **Códificación Huffman** </font>


La codificación Huffman es un método ampliamente utilizado en la compresión de datos. Su objetivo es representar un texto en binario de una manera más eficiente que la codificación estándar ASCII, asignando códigos binarios más cortos a caracteres más comunes y códigos más largos a caracteres menos comunes. Esto resulta en una reducción significativa en la cantidad de bits necesarios para representar el texto.

A continuación, se explicará cómo se implementó la codificación Huffman en el esquema de comunicación y se proporcionarán fragmentos de código para ilustrar cada paso del proceso.

## **1. Fuente de Información**

El primer paso es obtener el mensaje original desde un archivo de texto. La función `leer_archivo` se encarga de leer el archivo "fuente.txt" y almacenar su contenido en la variable `texto_original`.

```python
nombre_archivo_fuente = "fuente.txt"
texto_original = leer_archivo(nombre_archivo_fuente)
print("Mensaje:", texto_original)
```

## **2. Transmisor**

En el transmisor, el mensaje original se convierte en una representación binaria. La función `texto_a_binario` toma el mensaje y lo convierte en una secuencia de ceros y unos, donde cada carácter se representa como una cadena binaria de 8 bits.

```python
texto_binario = texto_a_binario(texto_original)
```

Luego, se construye un árbol Huffman a partir del texto original. Este árbol se crea considerando la frecuencia de cada carácter en el mensaje. Los caracteres más frecuentes se ubican en niveles superiores del árbol, y los menos frecuentes, en niveles inferiores. La función `arbol_huffman` devuelve el nodo raíz del árbol Huffman.

```python
raiz = arbol_huffman(texto_original)
```

El siguiente paso es generar un diccionario que asocie cada carácter con su correspondiente código binario de Huffman. La función `diccionario_huffman` recorre el árbol Huffman y crea este diccionario.

```python
diccionario = diccionario_huffman(raiz)
```

## **3. Canal**

En esta implementación, no se agrega ruido al canal de comunicación, pero es el lugar donde, en un escenario real, podrían ocurrir errores o ruido en la transmisión.

## **4. Receptor**

En el receptor, el mensaje binario codificado se decodifica utilizando el árbol Huffman previamente construido. Comenzando desde la raíz del árbol, se sigue el camino de bits (0 o 1) para identificar los caracteres correspondientes. Cuando se llega a un nodo hoja del árbol, se identifica un carácter y se agrega al mensaje decodificado.

```python
texto_codificado = "".join(diccionario[char] for char in texto_original)
texto_decodificado = decodificar(texto_codificado, raiz)
```

## **5. Destino de Información**

Finalmente, se muestra la cadena binaria original, la cadena binaria comprimida, el mensaje original y el mensaje recibido después de la decodificación. Además, se imprime la lista de símbolos utilizados en el diccionario Huffman, que muestra qué códigos binarios se asignaron a cada carácter en el mensaje original.

```python
print("Cadena binaria original:", texto_binario)
print("Cadena binaria comprimida:", texto_codificado)
print("")
print("Mensaje enviado:", texto_original)
print("Mensaje recibido:", texto_decodificado)

print("Lista de símbolos")
print(diccionario)
```

Con esta implementación de la codificación Huffman, el mensaje se comprime y descomprime eficientemente durante la transmisión y recepción, lo que permite reducir el número de bits necesarios para representar el texto original.

> # <font color="4169E1"> **Códificación Shannon-Fano** </font>

La codificación Shannon-Fano es un algoritmo de compresión de datos sin pérdida desarrollado por Robert Fano, basado en una idea de Claude Shannon. Este método se utiliza para comprimir datos representando los símbolos con códigos binarios variables de longitud. A diferencia de la codificación Huffman, que es óptima, la codificación Shannon-Fano no siempre produce códigos óptimos, pero es más simple y rápida de construir.

La codificación Shannon-Fano se basa en los siguientes pasos:

1. Crear una lista de símbolos y calcular sus frecuencias de aparición en los datos.
2. Ordenar la lista de símbolos por frecuencia, de mayor a menor.
3. Dividir la lista en dos partes, de manera que la suma de las frecuencias de la primera mitad sea lo más cercana posible a la suma de las frecuencias de la segunda mitad.
4. Asignar el bit "0" a los símbolos en la primera mitad y el bit "1" a los símbolos en la segunda mitad.
5. Repetir los pasos 3 y 4 recursivamente para las dos mitades hasta que todos los símbolos tengan un código asignado.

A continuación, se proporciona un fragmento de código que ilustra la implementación de la codificación Shannon-Fano en el esquema de comunicación:

## **1. Fuente de Información**

En este paso, se lee un archivo de texto que contiene el mensaje original:

```python
nombre_archivo_fuente = "fuente.txt"
texto_original = leer_archivo(nombre_archivo_fuente)
```

Luego, se convierte el mensaje de texto en una cadena binaria:

```python
mensaje_binario = texto_a_binario(texto_original)
```

## **2. Transmisor**

En el transmisor, se realizan varios pasos para construir la tabla de codificación Shannon-Fano y codificar el mensaje:

### Paso 2: Dividir la cadena binaria en bytes

```python
bytes_binarios = dividir_binario_en_bytes(mensaje_binario)
```

### Paso 3: Calcular las frecuencias de cada byte

```python
frecuencias = calcular_frecuencias(bytes_binarios)
```

### Paso 4: Construir la tabla de codificación Shannon-Fano

```python
tabla_codificacion_sf = construir_tabla_shannon_fano(frecuencias)
```

### Paso 5: Codificar el mensaje utilizando la tabla de codificación Shannon-Fano

```python
mensaje_codificado = codificar_con_shannon_fano(bytes_binarios, tabla_codificacion_sf)
```

## **3. Canal**

En esta implementación, no se agrega ruido al canal de comunicación, pero este es el lugar donde, en un escenario real, podrían ocurrir errores o ruido en la transmisión.

## **4. Receptor**

En el receptor, se decodifica el mensaje utilizando la tabla de codificación Shannon-Fano:

### Paso 6: Decodificar el texto codificado utilizando la tabla de codificación Shannon-Fano

```python
mensaje_decodificado = decodificar_con_shannon_fano(mensaje_codificado, tabla_codificacion_sf)
```

## **5. Destino de Información**

Finalmente, se muestra el mensaje original, el mensaje codificado y el mensaje decodificado:

```python
print("Mensaje Original:", texto_original)
print("Mensaje Codificado:", mensaje_codificado)
print("Mensaje Decodificado:", mensaje_decodificado)

print("Tabla de Codificación Shannon-Fano:")
for byte, codigo in tabla_codificacion_sf.items():
    print(f"{byte}: {codigo}")
```

La codificación Shannon-Fano permite comprimir datos utilizando códigos de longitud variable de manera eficiente, aunque no siempre óptima. Esta implementación muestra cómo se puede aplicar la codificación Shannon-Fano en un esquema de comunicación para la compresión y posterior descompresión de datos.

> # <font color="4169E1"> **Códificación Lempel Ziv y Welch (Algoritmo LZW)** </font>

El algoritmo Lempel Ziv y Welch, conocido como Algoritmo LZW, es un método de compresión de datos sin pérdida que se basa en la construcción y el mantenimiento de un diccionario de códigos que representan secuencias de caracteres en los datos de entrada. El algoritmo fue desarrollado por Terry Welch en 1984 como una mejora del algoritmo LZ78, y se ha utilizado ampliamente en formatos de compresión como GIF y TIFF.

El proceso del algoritmo LZW se puede dividir en los siguientes pasos:

1. **Fuente de Información:** En este paso, se lee un archivo de texto que contiene el mensaje original que se desea comprimir. Se convierte el texto en una secuencia de caracteres.

2. **Transmisor (Compresión):** Aquí es donde se realiza la compresión del mensaje. El algoritmo LZW mantiene un diccionario que inicialmente contiene caracteres individuales (por ejemplo, caracteres ASCII) y se expande a medida que encuentra secuencias repetitivas en el mensaje original.

3. **Canal:** En este punto, no se agrega ruido al canal de comunicación. Sin embargo, en un entorno real, es donde podría ocurrir ruido o errores en la transmisión.

4. **Receptor (Descompresión):** En esta etapa, se realiza la descompresión de los datos comprimidos. El receptor utiliza el mismo diccionario que se utilizó en el transmisor para reconstruir el mensaje original a partir de los códigos comprimidos.

5. **Destino de Información:** En esta fase, se muestra el mensaje original, el mensaje comprimido (datos comprimidos) y el mensaje descomprimido (resultado de la descompresión). Además, se imprime el diccionario utilizado durante la compresión.

A continuación, se incluyen fragmentos de código que ilustran los pasos 1, 2 y 4 de la implementación del algoritmo LZW en el esquema de comunicación:

## **1. Fuente de Información**

En este paso, se lee un archivo de texto que contiene el mensaje original:

```python
nombre_archivo_fuente = "fuente.txt"
texto_original = leer_archivo(nombre_archivo_fuente)
```

## **2. Transmisor (Compresión)**

La compresión del mensaje se realiza utilizando el algoritmo LZW. Aquí, se mantiene un diccionario que se expande a medida que se encuentra contenido repetitivo en el mensaje:

```python
def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}  # Inicializar el diccionario con caracteres ASCII
    next_code = 256
    result = []
    current_code = ""

    for char in text:
        current_code += char
        if current_code not in dictionary:
            dictionary[current_code] = next_code
            next_code += 1
            result.append(dictionary[current_code[:-1]])
            current_code = char

    result.append(dictionary[current_code])  # Agregar el último código

    return result
```

## **4. Receptor (Descompresión)**

En el receptor, se decodifica el mensaje utilizando el mismo diccionario que se utilizó en el transmisor:

```python
def lzw_decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)}  # Inicializar el diccionario con caracteres ASCII
    next_code = 256
    result = []
    current_code = chr(compressed_data[0])
    result.append(current_code)

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_code + current_code[0]
        else:
            raise ValueError("Data corrupted or invalid.")

        result.append(entry)
        dictionary[next_code] = current_code + entry[0]
        next_code += 1
        current_code = entry

    print("Diccionario:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

    return ''.join(result)
```

En el paso de descompresión, se recupera el mensaje original a partir de los códigos comprimidos utilizando el diccionario. Al final, se imprime el diccionario utilizado durante la compresión para mostrar cómo evolucionó a medida que se encontraron nuevas secuencias en los datos.

## **5. Destino de Información**

En el paso de destino de información, se presentan los resultados de la compresión y descompresión del mensaje, junto con el diccionario utilizado durante la compresión. Es esencial para verificar si el algoritmo LZW logra comprimir y descomprimir los datos de manera efectiva.


```python
# Comprimir el texto
compressed_data = lzw_compress(texto_original)
print("Texto original:", texto_original)
print("Datos comprimidos:", compressed_data)

# Descomprimir los datos comprimidos
decompressed_text = lzw_decompress(compressed_data)
print("Texto descomprimido:", decompressed_text)

print("Diccionario:")
for key, value in dictionary.items():
    print(f"{key}: {value}")
```

En este paso, se muestra el mensaje original, los datos comprimidos (resultado de la compresión) y el mensaje descomprimido (resultado de la descompresión). Además, se imprime el diccionario utilizado durante la compresión, lo que permite una inspección detallada de cómo evolucionó el diccionario a medida que se encontraron nuevas secuencias en los datos durante la compresión y descompresión. Esto es útil para entender el funcionamiento del algoritmo LZW y verificar la fidelidad de la compresión y descompresión.

> # <font color="4169E1"> **Códificación Run-Length Encoding (RLE)** </font>

El algoritmo Run-Length Encoding, abreviado como RLE, es un método de compresión de datos simple y eficaz que se utiliza para codificar secuencias repetitivas en datos. Este algoritmo es especialmente efectivo cuando los datos contienen secuencias repetitivas y puede reducir significativamente el tamaño de los datos.

## **1. Fuente de Información**

El primer paso de RLE implica leer un archivo de texto o una fuente de datos. Esto proporciona el texto original que se comprimirá. Aquí está el código para leer un archivo de texto:

```python
# 1. Fuente de información (leyendo un archivo de texto)
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return ""

nombre_archivo_fuente = "fuente.txt"
texto_original = leer_archivo(nombre_archivo_fuente)
```

## **2. Transmisor**

En el paso del transmisor, el algoritmo RLE codifica el texto original utilizando secuencias repetidas. Aquí tienes el código que realiza la codificación RLE:

```python
# 2. Transmisor (codificamos con el algoritmo RLE)
def run_length_encode(text):
    encoded_text = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            encoded_text.append(text[i - 1] + str(count))
            count = 1

    encoded_text.append(text[-1] + str(count))

    return "".join(encoded_text)
```

## **3. Canal**

En un esquema de comunicación, este es el punto en el que se transmiten los datos codificados. En el caso de RLE, no se agrega ruido porque la codificación y decodificación son deterministas.

## **4. Receptor**

El receptor descomprime los datos codificados utilizando el algoritmo RLE. Aquí tienes el código para decodificar los datos:

```python
# 4. Receptor (decodificamos usando los datos codificados)
def run_length_decode(encoded_text):
    decoded_text = []
    i = 0

    while i < len(encoded_text):
        char = encoded_text[i]
        i += 1
        count_str = ""
        while i < len(encoded_text) and encoded_text[i].isdigit():
            count_str += encoded_text[i]
            i += 1
        count = int(count_str)
        decoded_text.append(char * count)

    return "".join(decoded_text)
```

## **5. Destino de Información**

En este paso, se presentan los resultados de la compresión y descompresión junto con una vista del "diccionario" utilizado por RLE. El algoritmo RLE no utiliza un diccionario en el sentido convencional, pero es útil mostrar las secuencias repetidas que se detectaron. Aquí está el código:

```python
# 5. Destino de Información (Se imprimen las cadenas de texto)
encoded_text = run_length_encode(texto_original)
decoded_text = run_length_decode(encoded_text)

print("Texto original:", texto_original)
print("Texto codificado:", encoded_text)
print("Texto decodificado:", decoded_text)
print()
print_rle_dictionary(texto_original)
```

En este paso, también puedes ver las secuencias repetidas en el texto original. Esto es útil para verificar si RLE funciona de manera efectiva.

Es importante destacar que RLE es especialmente útil para datos que contienen secuencias repetitivas, como imágenes simples o datos binarios con secciones repetidas.