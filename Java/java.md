# Conceptos de Java

## ¿Que se necesita para programar en Java?

Principalmente el JDK.

## Cómo descargar el JDK

1. Ingresar a la página oficial de Oracle a la sección de Java SE Development Kit downloads - Windows
2. Revisar tipo de Sistema Operativo y Descargar el Installer (.exe)
3. Configurar variables del sistema
    1. Ir a la ruta C/Archivos de Programa/Java/Jdk/bin
    2. Copiar ruta
    3. Ir a Sistema/Configuración avanzada de sistema/Variables de entorno
    4. Editar Variables de sistema/Path
    5. Pegar ruta copiada y aceptar.
4. Ver correcta instalación de java
    ```
    java --version
    ```

## Guardar codigo java en Git/Github

Para evitar guardar archivos innecesarios como los **.class**, es recomendable crear el archivo **.gitignore** y añadir las líneas de código que ignoran dichos archivos.
* En el buscardor de internet buscar:
    ```
    gitignore java
    ```

## Crear y ejecutar una clase en java

1. Define la clase **Learn** y el método **main**.
    ``` java
    public class Learn {
        public static void main (String args[]){
            System.out.println("Hello World!");
        }
    }
    ```

2. Guardar el archivo con el nombre de la clase **Learn.java**.
3. Crea el archivo bytecode
    ```
    javac Learn.java
    ```
    Para especificar una direccion para guardar las clases
    ```
    javac -d . Learn.java
    ```
4. Ejecuta el archivo bytecode
    ```
    java Learn
    ```
    o bien si la clase esta empaquetada:
    ```
    java pack.Learn
    ```

## Estandares de Java

1. El estilo de escritura es el CamelCase.
2. No se puede definir una variable anteriormente definida.
3. Todo archivo con su clase deberia estar empaquetado.

## Tipos de variables

1. Constantes:
    ``` java
    final int CONSTANT = 55;
    ```

## Clases en Java

1. Los nombres de las clases empiezan con mayusculas.
2. El **documento.java** que la contiene tendra el mismo nombre que la clase y debe estar escrita exactamente igual.
3. Los atributos constantes utilizando **final** deben ser asignados con un valor inicial en su misma definicion o utilizando el o los constructores.

## Import Java Package

1. Establecer la clase como publica
2. Establecer el paquete de la clase:

    ``` java
    package pack;
    public class Car {
        ...
    }
    ```
    **No olvidar guardar la clase en la carpeta con el nombre del paquete**

3. Importar la clase:

    ``` java
    import pack.Car;
    ```


## OPP

### Ventajas

1. Programación modular utilizando clases.
2. Más comprensibles, modificables y depurables.
3. Reutilizable utilizando herencia.
4. Control de errores con excepciones. 
5. Encapsulamiento.

### Vocabulario de la OPP

1. Clases y objetos
0. Instancia de clase
0. Modularización
0. Encapsulamiento
0. Herencia
0. Polimorfismo



