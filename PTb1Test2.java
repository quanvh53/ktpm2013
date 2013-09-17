import static org.junit.Assert.*;

import org.junit.Test;


public class PTb1Test2 {

	@Test
	public void testGptFloat() {
		PTb1 obj = new PTb1();
		assertEquals(1f, obj.gpt(2.0000001f, -1.9999999f),0.0000001f);
		assertEquals(0f, obj.gpt(0f, -0.00000013f),0.0000002f);
	}

}
