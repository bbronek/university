package Exceptions;

public class CastingExample {

    public static void main(String[] args) {

        ExampleException a = new ExampleException();
        SecondExampleException b = new SecondExampleException();
        Throwable e = (ExampleException)a;

        if (a instanceof ExampleException)
            System.out.println("a is instanceof ExampleException");
        if (b instanceof SecondExampleException)
            System.out.println("b is instanceof SecondExampleException");
        if (a instanceof SecondExampleException)
            System.out.println("a is instanceof SecondExampleException");
        if (b instanceof ExampleException)
            System.out.println("b is instanceof ExampleException");
        //       if (a instanceof Exception) System.out.println("a is instanceof Exception");
        //       if (b instanceof Exception) System.out.println("b is instanceof Exception");

        if (ExampleException.class.isInstance(a))
            System.out.println("a is isInstance ExampleException");
        if (SecondExampleException.class.isInstance(b))
            System.out.println("b is isInstance SecondExampleException");
        if (ExampleException.class.isInstance(b))
            System.out.println("b is isInstance SecondExampleException");
        if (SecondExampleException.class.isInstance(a))
            System.out.println("a is isInstance ExampleException");
        if (Exception.class.isInstance(a))
            System.out.println("a is isInstance Exception");
        if (Exception.class.isInstance(b))
            System.out.println("b is isInstance Exception");

        if (ExampleException.class.equals(a.getClass()))
            System.out.println("a.Class is == ExampleException.class");
        if (SecondExampleException.class.equals(b.getClass()))
            System.out.println("b.Class is == SecondExampleException.class");
        if (ExampleException.class.equals(b.getClass()))
            System.out.println("b.Class is == ExampleException.class");
        if (SecondExampleException.class.equals(a.getClass()))
            System.out.println("a.Class is == SecondExampleException.class");
        if (Throwable.class.equals(a.getClass()))
            System.out.println("a.Class is == Exception.class");
        if (Exception.class.equals(b.getClass()))
            System.out.println("b.Class is == Exception.class");
    }
}
