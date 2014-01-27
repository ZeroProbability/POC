package com.klyserv.projecteuler;

public class Problem036 {
	
	public static void main(String[] args) {
		int sum=0;
		for(int i=1;i<1000*1000;i++) {
			if(Helper.isPalindrome(Integer.toString(i))&&Helper.isPalindrome(Integer.toBinaryString(i))) {
				sum+=i;
			}
		}
		System.out.println(sum);
	}

}
