interface Figure {
    double circumference();
    double area();
    static final double PI = Math.PI;
}

class Circle implements Figure {
    double radius;

    Circle(double radius) { this.radius = radius; }

    public double circumference() { return 2 * PI * radius; }

    public double area() { return PI * radius * radius; }
}
class Triangle implements Figure {

    double a;
    double b;
    double c;

    public Triangle(double a, double b, double c) {
        if (!(a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a))
            throw new IllegalArgumentException("Invalid triangle sides");
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double circumference() { return a + b + c; }

    public double area() {
        double semiperimeter = this.circumference() / 2.0;
        return Math.sqrt(semiperimeter * (semiperimeter - a) * (semiperimeter - b) *
                         (semiperimeter - c));
    }
}

public class Figures {
    public static void main(String[] args) {
        Circle c = new Circle(3);
        System.out.println(c.circumference());
        Triangle t = new Triangle(3, 4, 5);
        System.out.println(t.area());
    }
}
