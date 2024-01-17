# **Teoría de la información - IT0332**

### ¡Actualización! - Unidad IV. COMPRESIÓN DE DATOS

**Nombre: Marcos Damián Pool Canul.**

**Matricula: 200300591@ucaribe.edu.mx**

**Profesor: Carlos Francisco Paz Cuevas.**

## **Esquema de comunicación**

Se realizara un programa en Python que simule un esquema de comunicación con los sigueintes puntos:

1. **Fuente de información:** Selecciona el mensaje deseado de un conjunto de mensajes posibles.

2. **Transmisor:** Transforma o codifica esta información en una forma apropiada al canal.
3. **Canal:** Medio a través del cual las señales son transmitidas al punto de recepción.
4. **Receptor:** Decodifica la señal transmitida en el mensaje original haciéndolo llegar a su destino.
5. **Destino de información:** Muestra el mensaje decodificado.

# **UNIDAD I. INTRODUCCIÓN A LA TEORÍA DE LA INFORMACIÓN**

#### **1. Fuente de información**
El primer paso en nuestro esquema de comunicacion es la fuente de infomacion, osea el mensaje.

- En esta etapa, crearemos un archivo de texto llamado "fuente.txt" que contendrá la información que servirá como fuente de datos en nuestro sistema de comunicación.

- Luego, se implementará una función para leer y extraer el contenido de este archivo.

Este es el codigo para leer un archivo de texto.
```python
# Funcion para leer un archivo de .txt
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, encoding="utf8") as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return ""
```

#### **2. Transmisor**
Es el emisor técnico, esto es el que transforma el mensaje emitido en un conjunto de señales o códigos que serán adecuados al canal encargado de transmitirlos.

Un ejemplo basico seria el de leer un archivo de texto y convertir su contenido a código ASCII.

Para llevar a cabo la conversión a codigo ASCII, creamos la funcion 'texto_a_ascii' y la implementamos en el esquema de comunicacion:

```python
def texto_a_ascii(texto):
    ascii_codigos = [ord(char) for char in texto]
    return ascii_codigos
```
#### **3. Canal**

Es el medio técnico que debe transportar las señales codificadas por el transmisor. Este medio será, en este caso la simulación de, cables, fibra óptica o por aire.

1. Agregar Ruido al Mensaje Transmitido:

En el código podemos agregar un ruido aleatorio al mensaje transmitido. Para esto podemos crear una funcion llamada agregar_ruido.

2. Probabilidad de Ruido:

Debemos ajustar la variable "probabilidad_ruido" para controlar la cantidad de ruido que deseamos simular en el canal de comunicación. Un valor más alto de "probabilidad_ruido" significa más ruido y una mayor probabilidad de errores.

3. Función para Agregar Ruido:


```python
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
#### **4. Receptor**

La actividad del receptor es la inversa de la del transmisor. Su función consiste en decodificar el mensaje transmitido y conducirlo por el canal, para transcribirlo en un lenguaje comprensible por el verdadero receptor que es llamado destinatario.

1. Recepción del Mensaje Transmitido:

El receptor comienza recibiendo el mensaje transmitido. En el código existente, esto se logra mediante la variable "mensaje_con_ruido", que contiene el mensaje afectado por el ruido.

2. Decodificación:

El receptor decodifica la señal para obtener la información en su forma original. Si en el "Transmisor" convertimos la información a representación binaria, debemos realizar la conversión inversa para obtener los códigos ASCII o el formato original de los datos.

```python
def binario_a_ascii(binario):
    # Divide la cadena binaria en segmentos de 8 bits y conviértelos a valores ASCII
    ascii_codigos = [int(binario[i:i+8], 2) for i in range(0, len(binario), 8)]

    # Convierte los códigos ASCII a caracteres y forma el mensaje de texto
    mensaje_texto = "".join(chr(codigo) for codigo in ascii_codigos)

    return mensaje_texto
```
#### **5. Destino de información**

El "Destino de Información" o "Destinatario," simplemente recibe el mensaje procesado y lo utiliza según su aplicación específica. En este caso el destinatario simplemente imprimirá el mensaje en su forma original.

```python
# 5. Destino de Información (Destinatario)
mensaje_destino = mensaje_recibido  # En este ejemplo, el mensaje en su forma original

# Imprimir el mensaje en el destinatario
mensaje_texto = "".join(chr(int(mensaje_destino[i:i+8], 2)) for i in range(0, len(mensaje_destino), 8))
print("Mensaje en el Destinatario: ", mensaje_texto)

```

El "mensaje_recibido" es el mensaje que ha sido procesado y que ahora se encuentra en su forma recuperada después de haber pasado por el "Receptor."



# **UNIDAD II. ENTROPÍA, PROBABILIDAD E INFERENCIA**

En teoría de la información, una entropía es una medida que indica un contenido medio de información de los mensajes de salida para una determinada fuente de mensajes. La comprensión teórica de la información del término entropía se remonta a Claude Shannon.

### **Entropia de una moneda (ejemplo visto en clase)**
```python
p(X=cara)=0.5
``` 
La entropía viene dada por la siguiente expresión:
```python
H=−∑ip(xi)log2p(xi)=−p(X=cara)log2p(X=cara)−p(X=cruz)log2p(X=cruz)
```
Por tanto, lanzar una moneda asumiendo que la distribución de probabilidades es uniforme resultaría en una entropía de 1 bit.

```python
import math

def calcular_entropia(probabilidad):
    if probabilidad <= 0 or probabilidad >= 1:
        return "La probabilidad debe estar entre 0 y 1"

    entropia = -math.log2(probabilidad)
    return entropia

# Ejemplo: Probabilidad de obtener cara en una moneda justa (0.5)
probabilidad_moneda = 0.5
entropia_moneda = calcular_entropia(probabilidad_moneda)
print(f"La entropía de lanzar una moneda justa es {entropia_moneda}")
```

### **Calculo de la entropia**

En este punto realizamos un ejercicio para calcular la entropia en con un umbarl y sigueindo la formula de la entropia.

```python
def calcular_entropia(probabilidad):
    entropia = 0.0
    for k in range(11):
        if probabilidad > 0:
            entropia -= probabilidad * math.log2(probabilidad)
    return entropia

# Definimos el umbral con los numeros que queramos.
umbral = [15, 16, 17, 18, 19, 20]

#Generamos 10 numeros aleatorios en una rango de 0 a 20.
numeros = [random.randint(0, 20) for _ in range(10)]

contador = 0

# Creamos un ciclo para saber cuantos numeros se repiten en el umbral y sacar la probabilidad.
for numero in numeros:
    if numero in umbral:
        contador = contador + 1

k = len(numeros)
pk = contador / len(numeros)

# Corremos la funcion y despues la imprimimos.
entropia_total = calcular_entropia(pk)

print(f"Numeros generados: {numeros}")
print(f"Entropía con umbral: {umbral}")
print(f"Probabilidad: {pk} \n")
print(f"La entropía es: {entropia_total:.3f} bits")
```



# **UNIDAD III. COMPRESIÓN DE DATOS**

> # **Códificación Huffman**

La codificación Huffman es un método ampliamente utilizado en la compresión de datos. Su objetivo es representar un texto en binario de una manera más eficiente que la codificación estándar ASCII, asignando códigos binarios más cortos a caracteres más comunes y códigos más largos a caracteres menos comunes. Esto resulta en una reducción significativa en la cantidad de bits necesarios para representar el texto.

**A continuación, se explicará cómo se implementó la codificación Huffman en el esquema de comunicación y se proporcionarán fragmentos de código para ilustrar cada paso del proceso.**

### **1. Fuente de Información**

El primer paso es obtener el mensaje original desde un archivo de texto. La función `leer_archivo` se encarga de leer el archivo "fuente.txt" y almacenar su contenido en la variable `texto_original`.

```python
nombre_archivo_fuente = "fuente.txt"
texto_original = leer_archivo(nombre_archivo_fuente)
print("Mensaje:", texto_original)
```

### **2. Transmisor**

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

### **3. Canal**

En esta implementación, no se agrega ruido al canal de comunicación, pero es el lugar donde, en un escenario real, podrían ocurrir errores o ruido en la transmisión.

### **4. Receptor**

En el receptor, el mensaje binario codificado se decodifica utilizando el árbol Huffman previamente construido. Comenzando desde la raíz del árbol, se sigue el camino de bits (0 o 1) para identificar los caracteres correspondientes. Cuando se llega a un nodo hoja del árbol, se identifica un carácter y se agrega al mensaje decodificado.

```python
texto_codificado = "".join(diccionario[char] for char in texto_original)
texto_decodificado = decodificar(texto_codificado, raiz)
```

### **5. Destino de Información**

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

> # **Códificación Shannon Fano**

*La codificación Shannon-Fano es un algoritmo de compresión de datos sin pérdida desarrollado por Robert Fano a partir de una idea de Claude Shannon.*

**Se trata de una codificación de entropía que produce un código de prefijo muy similar a un código de Huffman , aunque no siempre óptimo, a diferencia de este último.**

Un árbol Shannon-Fano se construye de acuerdo a una especificación diseñada para definir una tabla de códigos efectiva. El algoritmo actual es simple:

1. Para una lista de símbolos dada, crear su correspondiente lista de probabilidades o de frecuencias de aparición de manera que se conozca la frecuencia relativa de ocurrencia de cada símbolo.

2. Ordenar las listas de símbolos de acuerdo a la frecuencia, con los símbolos de ocurrencia más frecuente a la izquierda y los menos comunes a la derecha.

3. Dividir la lista en dos partes, haciendo la frecuencia total de la mitad izquierda lo más próxima posible a la de la mitad derecha.

4. Asignar a la mitad izquierda el dígito binario “0”, y a la mitad derecha el dígito “1”. Esto significa que los códigos para los símbolos en la primera mitad empezarán con “0”, y que los códigos de la segunda mitad empezarán por “1”.
5. Aplicar recursivamente los pasos 3 y 4 a cada una de las dos mitades, subdividiéndolas en grupos y añadiendo bits a los códigos hasta que cada símbolo se corresponde con una hoja del árbol.

### **1. Fuente de Información**

En este paso, se lee un archivo de texto que contiene el mensaje original:

```python
# 1. Fuente de información (leyendo un archivo de texto)
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, encoding="utf8") as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return ""

nombre_archivo_fuente = "input.txt"
texto_original = leer_archivo(nombre_archivo_fuente)
```
### **2. Transmisor**
```python
# Se encarga de asignar códigos "0" y "1" a los compresores. 
def codificador(compresores, particion):
    if particion > 0: # Indica que todavía hay compresores que deben recibir códigos.
        parte_1 = compresores[:particion+1]
        for i in parte_1:
            i.codigo += '0' # Esto indica que estos compresores están en la parte izquierda de la partición.
        if len(parte_1) <= 1: # En este caso, retorna y no se realizan más divisiones.
            return
        codificador(parte_1, divisor(probabilidad=[i.probabilidad for i in parte_1], puntero=0))
        parte_2 = compresores[particion+1:]
        for i in parte_2:
            i.codigo += '1' # Esto indica que estos compresores están en la parte derecha de la partición.
        if len(parte_2) <= 1:
            return
        codificador(parte_2, divisor(probabilidad=[i.probabilidad for i in parte_2], puntero=0))
    elif particion == 0: # En caso de que la partición sea igual a cero, significa que todos los compresores se encuentran en la misma partición.
        parte_1 = compresores[:particion+1]
        for i in parte_1:
            i.codigo += '0'
        parte_2 = compresores[particion+1:]
        for i in parte_2:
            i.codigo += '1'
```

### **4. Receptor**

Realizamos el proceso de descompresion y lo guardamos en un archivo de texto.
```python
with open("output.txt", "w", encoding="utf-8") as archivo_salida:
    archivo_salida.write(texto_decomprimido)
print()
print("Mensaje decodificado guardado en 'output'.")
```
### **5. Destino de informacion**

Iteramos para inprimir los caracteres, codigos y las probabilidades.
```python
# 5. Destino de Información (Destinatario)
print("                |------------------------|")
print("                |    Datos codificados   |")
print("                |------------------------|")
print()
datos_comprimidos = comprimir_datos(texto_original)
for i in datos_comprimidos:
    print(f"Caracter: {i.original}, Código: {i.codigo}, Probabilidad: {i.probabilidad}")
```


> # **Códificación Lempel Ziv y Welch (Algoritmo LZW)** 

El algoritmo Lempel Ziv y Welch, conocido como Algoritmo LZW, es un método de compresión de datos sin pérdida que se basa en la construcción y el mantenimiento de un diccionario de códigos que representan secuencias de caracteres en los datos de entrada. El algoritmo fue desarrollado por Terry Welch en 1984 como una mejora del algoritmo LZ78, y se ha utilizado ampliamente en formatos de compresión como GIF y TIFF.

El proceso del algoritmo LZW se puede dividir en los siguientes pasos:

1. **Fuente de Información:** En este paso, se lee un archivo de texto que contiene el mensaje original que se desea comprimir. Se convierte el texto en una secuencia de caracteres.

2. **Transmisor (Compresión):** Aquí es donde se realiza la compresión del mensaje. El algoritmo LZW mantiene un diccionario que inicialmente contiene caracteres individuales (por ejemplo, caracteres ASCII) y se expande a medida que encuentra secuencias repetitivas en el mensaje original.

3. **Canal:** En este punto, no se agrega ruido al canal de comunicación. Sin embargo, en un entorno real, es donde podría ocurrir ruido o errores en la transmisión.

4. **Receptor (Descompresión):** En esta etapa, se realiza la descompresión de los datos comprimidos. El receptor utiliza el mismo diccionario que se utilizó en el transmisor para reconstruir el mensaje original a partir de los códigos comprimidos.

5. **Destino de Información:** En esta fase, se muestra el mensaje original, el mensaje comprimido (datos comprimidos) y el mensaje descomprimido (resultado de la descompresión). Además, se imprime el diccionario utilizado durante la compresión.

A continuación, se incluyen fragmentos de código que ilustran los pasos 1, 2 y 4 de la implementación del algoritmo LZW en el esquema de comunicación:

### **1. Fuente de Información**

En este paso, se lee un archivo de texto que contiene el mensaje original:

```python
nombre_archivo_fuente = "fuente.txt"
texto_original = leer_archivo(nombre_archivo_fuente)
```

### **2. Transmisor (Compresión)**

La compresión del mensaje se realiza utilizando el algoritmo LZW. Aquí, se mantiene un diccionario que se expande a medida que se encuentra contenido repetitivo en el mensaje:

```python
def comprimir(text):
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

### **4. Receptor (Descompresión)**

En el receptor, se decodifica el mensaje utilizando el mismo diccionario que se utilizó en el transmisor:

```python
def descomprimir(datos_descomprimidos):
    dictionary = {i: chr(i) for i in range(256)}  # Inicializar el diccionario con caracteres ASCII
    next_code = 256
    result = []
    current_code = chr(datos_descomprimidos[0])
    result.append(current_code)

    for code in datos_descomprimidos[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = current_code + current_code[0]
        else:
            raise ValueError("Invalido")

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

### **5. Destino de Información**

En el paso de destino de información, se presentan los resultados de la compresión y descompresión del mensaje, junto con el diccionario utilizado durante la compresión. Es esencial para verificar si el algoritmo LZW logra comprimir y descomprimir los datos de manera efectiva.

```python
# Comprimir el texto
datos_comprimidos = comprimir(texto_original)
print("Texto original:", texto_original)
print("Datos comprimidos:", datos_comprimidos)

# Descomprimir los datos comprimidos
datos_descomprimidos = descomprimir(datos_comprimidos)
print("Texto descomprimido:", datos_descomprimidos)

print("Diccionario:")
for key, value in dictionary.items():
    print(f"{key}: {value}")
```

En este paso, se muestra el mensaje original, los datos comprimidos (resultado de la compresión) y el mensaje descomprimido (resultado de la descompresión). Además, se imprime el diccionario utilizado durante la compresión, lo que permite una inspección detallada de cómo evolucionó el diccionario a medida que se encontraron nuevas secuencias en los datos durante la compresión y descompresión. Esto es útil para entender el funcionamiento del algoritmo LZW y verificar la fidelidad de la compresión y descompresión.

> # **Códificación Run-Length Encoding (RLE)**

El algoritmo Run-Length Encoding, abreviado como RLE, es un método de compresión de datos simple y eficaz que se utiliza para codificar secuencias repetitivas en datos. Este algoritmo es especialmente efectivo cuando los datos contienen secuencias repetitivas y puede reducir significativamente el tamaño de los datos.

### **1. Fuente de Información**

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

### **2. Transmisor**

En el paso del transmisor, el algoritmo RLE codifica el texto original utilizando secuencias repetidas. Aquí tienes el código que realiza la codificación RLE:

```python
# 2. Transmisor (codificamos con el algoritmo RLE)
def codificacion(text):
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

### **3. Canal**

En un esquema de comunicación, este es el punto en el que se transmiten los datos codificados. En el caso de RLE, no se agrega ruido porque la codificación y decodificación son deterministas.

### **4. Receptor**

El receptor descomprime los datos codificados utilizando el algoritmo RLE. Aquí tienes el código para decodificar los datos:

```python
# 4. Receptor (decodificamos usando los datos codificados)
def decodificacion(encoded_text):
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

### **5. Destino de Información**

En este paso, se presentan los resultados de la compresión y descompresión junto con una vista del "diccionario" utilizado por RLE. El algoritmo RLE no utiliza un diccionario en el sentido convencional, pero es útil mostrar las secuencias repetidas que se detectaron. Aquí está el código:

```python
# 5. Destino de Información (Se imprimen las cadenas de texto)
encoded_text = codificacion(texto_original)
decoded_text = decodificacion(encoded_text)

print("Texto original:", texto_original)
print("Texto codificado:", encoded_text)
print("Texto decodificado:", decoded_text)
print()
print_rle_dictionary(texto_original)
```

En este paso, también puedes ver las secuencias repetidas en el texto original. Esto es útil para verificar si RLE funciona de manera efectiva.

Es importante destacar que RLE es especialmente útil para datos que contienen secuencias repetitivas, como imágenes simples o datos binarios con secciones repetidas.

# **UNIDAD IV. TÓPICOS SELECTOS DE TEORÍA DE LA INFORMACIÓN**

Aplicar las propiedades de los códigos Hash y binarios para la resolución de problemas de ingeniería de datos.

- 1) Códigos Hash
- 2) Códigos binarios
 
## Esquema de comunicación con Codificación Hash

### Descripción:

Este código implementa un esquema de comunicación que utiliza la codificación hash para asegurar la integridad de los mensajes transmitidos. Aquí se proporciona una descripción de las principales funciones y pasos del programa:

### Importamos las librerías
- `hashlib`: Utilizada para generar el hash SHA-256.
- `random`: Utilizada para la generación de valores aleatorios.
- `bitstring`: Utilizada para manipular cadenas binarias.
- `collections.Counter`: Utilizada para contar las frecuencias de elementos en una lista.

### 1. Fuente de información

#### `leer_archivo(nombre_archivo)`
- Descripción: Lee el contenido de un archivo y devuelve su contenido.
- Parámetros: `nombre_archivo` - El nombre del archivo a leer.
- Retorno: El contenido del archivo o una cadena vacía si el archivo no es encontrado.

```python
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no fue encontrado.")
        return ""
```

### 2. Transmisor

#### `Convertir_a_Lista(mensaje)`
- Descripción: Convierte un mensaje en una lista de caracteres.
- Parámetros: `mensaje` - El mensaje a convertir.
- Retorno: Lista de caracteres.

```python
def Convertir_a_Lista(mensaje):
  lista = []
  for i in mensaje:
    lista.append(i)
  return lista
```

#### `Convertir_a_String(lista)`
- Descripción: Convierte una lista de caracteres en una cadena.
- Parámetros: `lista` - Lista de caracteres.
- Retorno: Cadena de caracteres.

```python
def Convertir_a_String(lista):
    return ''.join(lista)
```

#### `Binario_a_Texto(binario)`
- Descripción: Convierte una cadena binaria en texto.
- Parámetros: `binario` - Cadena binaria.
- Retorno: Texto correspondiente a la cadena binaria.

```python
def Binario_a_Texto(binario):
    bloques = [binario[i:i+8] for i in range(0, len(binario), 8)]
    caracteres = [chr(int(bloque, 2)) for bloque in bloques]
    texto = ''.join(caracteres)
    return texto
```

#### Codificación Hash

##### `FrecuenciasRelativas(lista_patrones)`
- Descripción: Calcula las frecuencias relativas de los patrones en una lista.
- Parámetros: `lista_patrones` - Lista de patrones.
- Retorno: Listas ordenadas de palabras y sus frecuencias relativas.

##### `Transmisor(BinariList)`
- Descripción: Realiza la transmisión de datos aplicando RLE y generando un diccionario de patrones y sus correspondientes codificaciones.
- Parámetros: `BinariList` - Lista de datos binarios.
- Retorno: Diccionario de patrones y sus codificaciones.

##### `CodificarLista(BinariList, handshake)`
- Descripción: Codifica una lista de datos binarios según el diccionario de patrones proporcionado.
- Parámetros: `BinariList` - Lista de datos binarios. `handshake` - Diccionario de patrones y sus codificaciones.
- Retorno: Lista de datos codificados.

##### `BorrarAleatorio(lista1, lista2)`
- Descripción: Elimina de manera aleatoria un elemento de dos listas y lo devuelve.
- Parámetros: `lista1` y `lista2` - Listas de elementos.
- Retorno: Listas actualizadas y el elemento eliminado.

### 3. Canal

#### `Canal(paquete, indices, canales)`
- Descripción: Simula la transmisión del paquete a través de un canal y puede introducir ruido.
- Parámetros: `paquete` - Lista de paquetes, `indices` - Lista de índices de paquetes, `canales` - Lista que simula canales de comunicación.
- Retorno: Lista actualizada de canales, indicador de ruido, canal usado y el índice eliminado.

### Busqueda Binaria

#### `BusquedaBinaria(lista_valores, buscar)`
- Descripción: Realiza una búsqueda binaria en una lista ordenada.
- Parámetros: `lista_valores` - Lista ordenada, `buscar` - Valor a buscar.
- Retorno: Índice del valor encontrado o -1 si no se encuentra.

#### `Ordenar(diccionario)`
- Descripción: Ordena un diccionario por sus valores y devuelve las claves y valores ordenados.

### 4. Generar Hash

#### `GenerarHash(dato)`
- Descripción: Genera un hash SHA-256 de un dato.
- Parámetros: `dato` - Dato a ser hasheado.
- Retorno: Hash SHA-256.

```python
def GenerarHash(dato):
  bdatos = bytes(dato,'utf-8')
  h = hashlib.new("sha256",bdatos)
  digest=h.hexdigest()
  return digest
```

### 5. Comparar Hash

#### `CompararHash(cadenaList, claves, valores)`

```python
def CompararHash(cadenaList,claves,valores):
  indice = BusquedaBinaria(valores, cadenaList)

  if(indice != -1):
    return claves[indice]
  else:
    return "x"
```
