package com.klyserv.poc.fibonacci;

public class FibonacciTest {
	
	public static void main(String[] args) {
		Fibonacci f=new Fibonacci();
		
		for(int i=0;i<10;i++){
			System.out.println(f.nextNumber());
		}
	}

}
