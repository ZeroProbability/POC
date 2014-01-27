package com.klyserv.projecteuler;

public class Problem001 {
	public static void main(String[] args) {
		int max=1000;
		boolean[] numList=new boolean[max+1];
		for (int i = 0; i < numList.length; i++) {
			numList[i]=false;
		}
		for(int i=3;i<max+1;i+=3) {
			numList[i]=true;
		}
		for(int i=5;i<max;i+=5) {
			numList[i]=true;
		}
		int sum=0;
		for (int i = 0; i < numList.length; i++) {
			if(numList[i]) sum+=i;
		}
		System.out.println("sum ="+sum);
	}

}
