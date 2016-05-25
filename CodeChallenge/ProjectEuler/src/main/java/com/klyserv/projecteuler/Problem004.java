package com.klyserv.projecteuler;

public class Problem004 {
	
	private static boolean isPalindrome(String s) {
		StringBuilder sb=new StringBuilder(s);
		sb.reverse();
		return sb.toString().equals(s);
	}
	
	public static void main(String[] args) {
		int max=0;
		for (int i = 100; i <= 999; i++) {
			for(int j=100; j<=999;j++) {
				int mult=i*j;
				if(isPalindrome(Integer.toString(mult))) {
					if(max<mult) max=mult;
				}
			}
		}
		System.out.println(max);
	}

}
