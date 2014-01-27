package com.klyserv.projecteuler;

public class Problem009 {
	
	public static void main(String[] args) {
		for(int i=3;i<1000;i++) {
			for(int j=4;j<1000;j++) {
				int k=1000-i-j;
				if(i*i+j*j==k*k) {
					System.out.println(i+" "+j+" "+k);
					System.out.println(i*j*k);
					return;
				}
			}
		}
	}

}
