package com.klyserv.projecteuler;

public class Problem005 {
	
	public static void main(String[] args) {
		long lcm=2;
		for(int i=3;i<20;i++) {
			lcm=Helper.lcm(lcm, i);
		}
		System.out.println(lcm);
	}

}
