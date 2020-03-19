package Fibonacci;

public class Fibonacci {
	public static long fib(int n) {
		long []term = new long [1000]; 	   
	    if (n <= 1) 
	        return n; 	  
	    if (term[n] != 0) 
	        return term[n];
	    else 
	    { 
	        term[n] = fib(n - 1) + fib(n - 2); 
	  
	        return term[n]; 
	    } 
	}
	public static void main(String[] args) { 
		System.out.print(fib(1));
	} 
}
