public class MutableValue {

	private Integer b;
	private MutableValue a;
	
	public MutableValue(int a) {
		this.b = a;
	}
	
	public void setB(int _b){
		b=_b;
	}
	
	public int getB(){
		return b;
	}
	
	static MutableValue changeValue(MutableValue kl){
	  kl.b = 3;
	  return kl;
	}
	
	static MutableValue replaceValue(MutableValue kl){
	  kl=new MutableValue(5);
	  return kl;
	}
	
	static int changeNumber(int kl){
	  kl= 44;
	  return kl;
	}
}