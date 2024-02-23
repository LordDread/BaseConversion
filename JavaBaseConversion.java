// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Dictionary;
import java.util.Enumeration;
import java.util.Hashtable;

class Main {
    static void base_conversion(int base10Num, int targetBase) {
        Dictionary<Integer, String> hex_conversion = new Hashtable<>();
	hex_conversion.put (0,"0");
	hex_conversion.put (1,"1");
	hex_conversion.put (2,"2");
	hex_conversion.put (3,"3");
	hex_conversion.put (4,"4");
	hex_conversion.put (5,"5");
	hex_conversion.put (6,"6");
	hex_conversion.put (7,"7");
	hex_conversion.put (8,"8");
	hex_conversion.put (9,"9");
	hex_conversion.put (10,"A");
	hex_conversion.put (11,"B");
	hex_conversion.put (12,"c");
	hex_conversion.put (13,"D");
	hex_conversion.put (14,"E");
	hex_conversion.put (15,"F");
	int workingNumber = base10Num;
    String result = "";
	String hex_conversion_result = "";
	
        while (workingNumber != 0) {
            hex_conversion_result = hex_conversion.get(workingNumber % targetBase);
	    result = hex_conversion_result + result;
            workingNumber = workingNumber / targetBase;
        }
            System.out.println("Base 10 input: " + base10Num + "\nBase " + targetBase + " result:" + result);
        
        
    
  }
    public static void main(String[] args) {
        base_conversion(4600,13);
        
    }
}
