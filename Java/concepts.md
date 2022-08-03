

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
## Crear y ejecutar una clase en java

1. Define la clase **learn** y el método **main**.
    ``` java
    public class learn {
        public static void main (String args[]){
            System.out.println("Hello World!");
        }
    }
    ```

2. Guardar el archivo con el nombre de la clase **learn.java**.
3. Crea el archivo bytecode
    ```
    javac learn.java
    ```
4. Ejecuta el archivo bytecode
    ```
    java learn
    ```


