package Wyjatki;

class Watek{
	public void dwa(boolean czyWyjatek){
		System.out.println("Metoda dwa wypisywanie 1");
		System.out.println("Metoda dwa wypisywanie 2");
	}
	
	public void jeden(boolean czyWyjatek){
		System.out.println("Metoda jeden wypisywanie 1");
		dwa(czyWyjatek);
		System.out.println("Metoda jeden wypisywanie 2");
	}
}

public class Wyjatki {
	
	public static void main(String[] args) {
		System.out.println("Zaczynamy działanie programu");
		Watek w = new Watek();
		w.jeden(false);
		System.out.println("Kończymy działanie programu");
	}

}
