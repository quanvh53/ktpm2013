
public class PTb1 {
	
	/**
	 * @param args
	 */
	
	public float gpt(int a,int b){
		if(a==0)return 0f;
		return -1f*b/a;
	}
	
	public float gpt(float a,float b){
		if(a==0) return 0f;
		return -1f*b/a;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float a =  2.0000001f;
		float b = -1.9999999f;
		PTb1 obj = new PTb1();
		System.out.println("Ket qua: x = " + obj.gpt(a, b));
	}

}
