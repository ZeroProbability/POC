package com.klyserv.projecteuler;

public class Problem002 {
	
	static class Fibonacci {
		private long firstNum=1;
		private long secondNum=2;
		
		public long getNext() {
			long next=firstNum+secondNum;
			firstNum=secondNum;
			secondNum=next;
			return secondNum;
		}
		
	}
	
	public static void main(String[] args) {
		Fibonacci f=new Fibonacci();
		long sum=2;
		
		long n=0;
		while((n=f.getNext())<4000000l){
			if(n%2==0) sum+=n;
		}
		
		System.out.println(sum);
		
	}

}
