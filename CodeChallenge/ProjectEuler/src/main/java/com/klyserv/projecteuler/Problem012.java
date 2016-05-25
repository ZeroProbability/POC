package com.klyserv.projecteuler;

public class Problem012 {
	
	public static void main(String[] args) {
		int triangleNum=6;
		for(int i=4;i<1000000;i++) {
			triangleNum+=i;
			if(Factors.findFactors(triangleNum).size()>500) {
				System.out.println(triangleNum);
				return;
			}
		}
	}

}
