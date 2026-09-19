public class ReferencesExample {
	
	
	public static void main(String[] args) {
		MutableValue object1 = new MutableValue(0);
		MutableValue object2 = new MutableValue(1);
		
		System.out.println("1) object1.b="+object1.getB());
		System.out.println("1) object2.b="+object2.getB());

		MutableValue.changeValue(object1);
		object2 = MutableValue.changeValue(object2);
		System.out.println("2) object1.b="+object1.getB());
		System.out.println("2) object2.b="+object2.getB());
		
		MutableValue.replaceValue(object1);
		object2 = MutableValue.replaceValue(object2);
		System.out.println("3) object1.b="+object1.getB());
		System.out.println("3) object2.b="+object2.getB());

		int i=3;
		MutableValue.changeNumber(i);
		System.out.println("i="+i);
	}

} 
