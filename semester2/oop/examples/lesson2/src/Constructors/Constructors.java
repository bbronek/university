package Constructors;

class Insect {
	 int i = 9;
	 int j;

	Insect() {
		System.out.println("Running the Insect constructor");
		System.out.println("i =" + i + " ,j=" + j);
	}

	private static int x1 = print("Insect static field initialized");

	public  String name() {
		return "Insecta";
	}

	static int print(String s) {
		System.out.println(s);
		return 47;
	}
}

class Bee extends Insect {
	private int k = print("Bee field initialized");
	
	public Bee() {
		super();
		System.out.println("Running the Bee constructor");
		System.out.println("k = " + k);
		System.out.println("j = " + j);
		k = 23;
		System.out.println("k = " + k);
	}

	public String name() {
		return "Apis";
	}

	private static int x2 = print("Bee static field initialized");
}

public class Constructors {

	public static void main(String[] args) {
		System.out.println("Creating a Bee object");
		Bee b1 = new Bee();
		System.out.println(b1.name());
	}

}
