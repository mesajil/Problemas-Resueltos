
public class Learn {
    public static void main (String args[]){
        System.out.println("Hello World!");

        // Tipos de datos

        int num1 = 5;
        int num2 = 7; 

        // Clase String

        String resultado = "Salida de la suma: " + (num1 + num2);
        System.out.println(resultado);

        // Estructuras condicionales

        final int EDAD_MIN = 18;
        int edad = 19;
        if (edad >= EDAD_MIN) {
            System.out.println("Es mayor de edad.");
        }
        else {
            System.out.println("No es mayor de edad.");
        }

        // Estructuras condicionales anidadas

        int operacion = 2;
        double num1_ = 5;
        double num2_ = 7;
        double resultado_ = 0;

        if (operacion == 1) {
            resultado_ = num1_ + num2_;
        }
        else if (operacion == 2) {
            resultado_ = num1_ - num2_;
        }
        else if (operacion == 3) {
            resultado_ = num1_ * num2_;
        }
        else if (operacion == 4) {
            resultado_ = num1_ / num2_;
        }
        else {
            System.out.println("Debe ingresar tipo de operacion.");
        }

        System.out.println("Resultado: " + resultado_);


    }
}