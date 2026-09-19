public class InheritanceExample{
	
	public static void main(String arg[]){
		Superclass a = new Superclass();
		System.out.println("Object: " + a);
		Subclass b = new Subclass();
		System.out.println("Object: " +b);
		a=b;
		System.out.println("Object: " +a);
	}
	
}

class Superclass{
	
	Superclass(){	
	}
	
}

class Subclass extends Superclass{

	Subclass(){	
	}
	
}