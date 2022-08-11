package learn;
import pack.Car;

public class LearnOOP {
    public static void main (String[] args) {
        
        // Public attributes and methods

        Car myCar = new Car();
        System.out.println("color: " + myCar.color);

        System.out.println("Changing the color ...");
        myCar.color = "blue";

        System.out.println("color: " + myCar.color);

        System.out.println("static wheels: " + myCar.wheels);
    
        System.out.println("Setting the color ...");
        myCar.setColor("green");

        myCar.printColor();

        // Constructors            

        System.out.println("new Car( ... ) ...");
        Car myCar2 = new Car("black");

        myCar2.printColor();
    }
}