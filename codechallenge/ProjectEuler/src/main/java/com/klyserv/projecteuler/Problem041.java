package com.klyserv.projecteuler;

public class Problem041 {
	
	private static boolean isPandigital(String s) {
		int n=s.length();
		for (int i = 0; i < n; i++) {
			if(s.charAt(i)=='0'||(s.charAt(i)-'0')>n) return false;
			for(int j=i+1;j<n;j++){
				if(s.charAt(i)==s.charAt(j)) return false;
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		PrimeSeive ps=new PrimeSeive(1000*1000*1000);
		
		while(!ps.isEndOfSearch()) {
			int nextP=ps.getNextPrime();
			
			if(isPandigital(Integer.toString(nextP))) {
				System.out.println(nextP);
			}
		}
		
	}

}
