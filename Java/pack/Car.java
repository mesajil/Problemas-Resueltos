package pack;

public class Car {
    public static int wheels = 4;
    public String color;

    public Car() {
        color = "red";
    }

    public Car(String newColor) {
        color = newColor;
    }

    public void setColor(String newColor) {
        color = newColor;
    }
    
    public String getColor () {
        return color;
    }
    public void printColor() {
        System.out.println("Printing color from the class: " + color);
    }
}