package Fibonacci;

import static org.junit.jupiter.api.Assertions.*;


import org.junit.jupiter.api.Test;



class FibonacciTest {

	@Test
	void testFib1() {
		int n = 1;
		assertEquals(1, Fibonacci.fib(n));
	}
	void testFib2() {
		int n = 2;
		assertEquals(2, Fibonacci.fib(n));
	}
	void testFib3() {
		int n = 3;
		assertEquals(20, Fibonacci.fib(n));
	}
}
