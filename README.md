# Esquema de comunicación

Se realizara un programa en Python que simule un esquema de comunicación con los sigueintes puntos:

- Fuente de información
- Transmisor
- Canal
- Receptor 
- Destino de información

En esta simulacion agregaremos RUIDO artificialmete para ver como cambian los resultados al final.

---

#### **1. Fuente de información**
El primer paso en nuestro esquema de comunicacion es la fuente de infomacion, osea el mensaje.

- En esta etapa, crearemos un archivo de texto llamado "fuente.txt" que contendrá la información que servirá como fuente de datos en nuestro sistema de comunicación.

- Luego, se implementará una función para leer y extraer el contenido de este archivo.

Hay que tener en cuenta que para crear el archivo "fuente.txt" manualmente, podemos utilizar un editor de texto y guardarlo en la misma ubicación donde se encuentra el script de Python. Luego, podemos usar el código en Python para leerlo.

#### **2. Transmisor**
Es el emisor técnico, esto es el que transforma el mensaje emitido en un conjunto de señales o códigos que serán adecuados al canal encargado de transmitirlos.

En este caso, vamos a utilizar el archivo de texto y convertir su contenido a código ASCII y luego a representación binaria para la transmisión.

Ahora explicare mas a detalle esta parte:

1. Leer contenido del archivo de texto:

Inicialmente, hemos leído el contenido del archivo de texto llamado "fuente.txt" en la etapa de la "Fuente de Información". Este contenido se almacena en la variable contenido_fuente que sera el mensaje.

2. Convertir a código ASCII:

En la etapa de la "Fuente de Información", hemos convertido el contenido del archivo de texto en una lista de códigos ASCII utilizando la función texto_a_ascii. Cada carácter del texto se representó como su correspondiente valor ASCII.

3. Convertir a representación binaria (Adicional):

Para llevar a cabo la conversión a una representación binaria, podemos 
agregar una función adicional para realizar esta conversión. Por ejemplo:

```
def ascii_a_binario(ascii_codigos):
    binario = ''.join(format(ord(char), '08b') for char in ascii_codigos)
    return binario

mensaje_transmitido = ascii_a_binario(contenido_fuente)

```
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
#### **4. Receptor**

La actividad del receptor es la inversa de la del transmisor. Su función consiste en decodificar el mensaje transmitido y conducirlo por el canal, para transcribirlo en un lenguaje comprensible por el verdadero receptor que es llamado destinatario. 

1. Recepción del Mensaje Transmitido:

El receptor comienza recibiendo el mensaje transmitido. En el código existente, esto se logra mediante la variable "mensaje_con_ruido", que contiene el mensaje afectado por el ruido.

2. Decodificación:

El receptor decodifica la señal para obtener la información en su forma original. Si en el "Transmisor" convertimos la información a representación binaria, debemos realizar la conversión inversa para obtener los códigos ASCII o el formato original de los datos.

#### **5. Destino de información**D

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
