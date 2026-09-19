package Equals;

public class Car {
    private final int year;

    public Car(int year) {
        this.year = year;
    }

    @Override
    public boolean equals(Object other) {
        if (this == other) return true;
        if (other == null || getClass() != other.getClass()) return false;
        return year == ((Car) other).year;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode(year);
    }
}

class BigCar extends Car {
    private final int weight;

    public BigCar(int weight, int year) {
        super(year);
        this.weight = weight;
    }

    @Override
    public boolean equals(Object other) {
        return super.equals(other) && weight == ((BigCar) other).weight;
    }

    @Override
    public int hashCode() {
        return 31 * super.hashCode() + Integer.hashCode(weight);
    }
}
