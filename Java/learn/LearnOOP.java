package learn;
import pack.Car;

public class LearnOOP {
    public static void main (String[] args) {
        
        Car myCar = new Car();
        System.out.println("public color: " + myCar.color);

        System.out.println("Changing the color ...");
        myCar.color = "blue";

        System.out.println("public color: " + myCar.color);

        System.out.println("public static wheels: " + myCar.wheels);
    

    }
}