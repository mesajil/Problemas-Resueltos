package pack;

public class Car {
    public String color;
    public static int wheels = 4;

    public Car() {
        color = "red";
    }

    public Car(String color_) {
        color = color_;
    }

    public void print() {
        System.out.println("Color: " + color);
    }
}