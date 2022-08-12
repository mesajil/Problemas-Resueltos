package learn;
import pack.Car;

public class LearnOOP {
    public static void main (String[] args) {
        
        // Evaluate constructors, attributes and methods 

        Car myCar = new Car();
        System.out.println("myCar.color: " + myCar.color);

        myCar.color = "blue";

        System.out.println("myCar.color: " + myCar.color);

        myCar.setColor("green");

        myCar.printColor();

        myCar = new Car("black");

        myCar.printColor();

        
    }
}