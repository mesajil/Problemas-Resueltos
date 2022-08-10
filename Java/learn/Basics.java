package learn;
import java.util.Scanner;

public class Basics {
    public static void main (String[] args){
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
        
        // Scanner: Read input

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese su nombre: ");
        // String nombre__ = sc.nextLine();

        System.out.print("Ingrese su edad: ");
        // int edad__ = sc.nextInt();

        // System.out.println("Hola " + nombre__ + ", su edad es " + edad__);

        // switch case

        int operacion_ = 5;
        double num1__ = 50;
        double num2__ = 7;
        double resultado__ = 0;

        switch (operacion_) { // Se puede usar int, enum, String

            case 1:
                resultado__ = num1__ + num2__;
                break;
            case 2:
                resultado__ = num1__ - num2__;
                break;
            case 3:
                resultado__ = num1__ * num2__;
                break;
            case 4:
                resultado__ = num1__ / num2__;
                break;
            default:
                System.out.println("Debe ingresar tipo de operacion.");    
        }

        System.out.println("Resultado: " + resultado__);

        // Ciclos y bucles

        for (int i = 0; i < 3; i ++){
            System.out.println("Hello World " + (i + 1) + "!");
        }

        int i_ = 0;
        while (i_ < 5){
            System.out.print((i_ + 1) + ", ");
            i_ ++;
        }
        System.out.println();

        int j_ = 1;
        do {
            System.out.print(j_ + ", ");
            j_ += 2;
        } while (j_ < 10);
        System.out.println();

        j_ = 0;
        while (true) {
            System.out.print(j_ + ", ");
            j_ += 2;
            if (j_ > 8) break;
        }
        System.out.println();

        // Imprimir: 1, 99, 2, 98, 3, 97, 4, 96, 5, 95,
        int inicial1 = 1;
        int inicial2 = 99;
        for (int i = 0; i < 5; i ++) {
            System.out.print((inicial1 + i) + ", " + (inicial2 - i) + ", ");
        }
        System.out.println();

        // Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
        int n1 = 0, n2 = 1, aux = 0;
        for (int i = 0; i < 10; i ++) {
            System.out.print(n1 + ", ");
            aux = n1;
            n1 = n2;
            n2 = n2 + aux;
        }
        System.out.println();

        // Strings

        // Equals

        String name = "Luis";

        System.out.println(name == "Luis");
        System.out.println(name.equals("Luis"));
        System.out.println(name.equalsIgnoreCase("luis"));

        // Length

        System.out.println("String's length: " + name.length());

        // Substring

        System.out.println("Subtring with one argument: " + name.substring(1));
        System.out.println("Subtring with two arguments: " + name.substring(1, 3));

        // Arrays
        
        int[] numbers = new int[5]; // Se inicializan en 0
        
        int length = numbers.length;
        
        for (int i = 0; i < length; i ++) {
            numbers[i] = (i + 1) * (i + 1);
        }
        
        System.out.println("Array: " + numbers + " Length: " + length);
        System.out.println("Data: ");
        for (int i = 0; i < length; i ++) {
            System.out.print(numbers[i] + ", ");
        }
        System.out.println();
        
        System.out.print("Printing the array with for each: ");
        int array[] = {1,2,3,4,5};
        
        for (int e: array) {
            System.out.print(e + ", ");
        }
        System.out.println();

        // Matrix

        int[][] matrix = new int[5][5];
        
        for (int i = 0; i < matrix.length; i ++) {
            for (int j = 0; j < matrix[0].length; j ++) {
                matrix[i][j] = i * j;
            }
        }
        
        System.out.print("Printing the matrix with for: ");

        for (int i = 0; i < matrix.length; i ++) {
            for (int j = 0; j < matrix[0].length; j ++) {
                
                System.out.print(matrix[i][j] + ", ");
            }
            System.out.println();
        }

        // Matrix and for :

        System.out.print("Print matrix with for each:");

        for (int[] row: matrix) {
            for (int e: row) {
                System.out.print(e + ", ");
            }
            System.out.println();
        }

        // Irregular matrix

        int[][] A = new int[3][];
        
        for (int i = 0; i < A.length; i ++) {
            A[i] = new int[i + 1];
        }
        
        System.out.println("Printing irregular matrix with length");
        
        for (int i = 0; i < A.length; i ++) {
            for (int j = 0; j < A[i].length; j ++) {
                
                System.out.print(A[i][j] + ", ");
            }
            System.out.println();
        }
        
        System.out.println("Printing irregular matrix with for each");
        
        for (int[] row: A) {
            for (int e: row) {
                System.out.print(e + ", ");
            }
            System.out.println();
        }
    }
}