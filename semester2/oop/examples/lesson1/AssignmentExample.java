public class AssignmentExample {

	public static void main(String[] args) {
		MutableValue a = new MutableValue(0);
		MutableValue b = new MutableValue(1);
		System.out.println(a.getB());
		System.out.println(b.getB());
		a = b;
		System.out.println(a.getB());
		System.out.println(b.getB());
	    MutableValue.changeValue(b);
		System.out.println(a.getB());
		System.out.println(b.getB());
	}
}