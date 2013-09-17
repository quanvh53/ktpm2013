import static org.junit.Assert.*;

import org.junit.Test;


public class PTb1Test{

	@Test
	public void testGptInt() {
		PTb1 a = new PTb1();
		assertEquals("Test aX + b = 0",0.74999f,a.gpt(4, -3),0.0001f);
		assertEquals("sai so la: 0.0001",-3.33334f,a.gpt(3, 10),0.0001f);
		assertEquals("Kiem tra voi he so a =0",-0.0001f,a.gpt(0, 3),0.0001f);
	}	
}
