interface Figure {
    double circumference();
    double area();
    static final double PI = 3.1415;
}

class Circle implements Figure{
    double radius;

    Circle(double radius){
        this.radius = radius;
    }

    public double circumference() {
        return 2*PI*radius;
    }

    public double area() {
        return PI*radius*radius;
    }
}
class Triangle implements Figure{

    double a;
    double b;
    double c;

    public Triangle(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double circumference()
    {
        return a + b + c ;
    }

    public double area()
    {
        double polOb = this.circumference()/2.0;
        return Math.sqrt(polOb*(polOb-a)*(polOb-b)*(polOb-c));
    }
}

public class Zad2 {
    public static void main(String[] args) {
        Circle c = new Circle(3);
        System.out.println(c.circumference());
        Triangle t = new Triangle(3,4,5);
        System.out.println(t.area());
    }
}
