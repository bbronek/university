package Exceptions;

class CallSequence{
	public void second(boolean throwException){
		System.out.println("Second method, output 1");
		System.out.println("Second method, output 2");
	}
	
	public void first(boolean throwException){
		System.out.println("First method, output 1");
		second(throwException);
		System.out.println("First method, output 2");
	}
}

public class Exceptions {
	
	public static void main(String[] args) {
		System.out.println("Starting the program");
		CallSequence w = new CallSequence();
		w.first(false);
		System.out.println("Program finished");
	}

}
