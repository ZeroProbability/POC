package com.klyserv.projecteuler;

public class Problem030 {
	
	public static int pow(int n, int m) {
		int ret=1;
		for(int i=0;i<m;i++){
			ret=ret*n;
		}
		return ret;
	}
	
	public static void main(String[] args) {
		int sum=0;
		for(int i=2;i<9999999;i++){
			int n=i;
			int last1=n%10;n=n/10;
			int last2=n%10;n=n/10;
			int last3=n%10;n=n/10;
			int last4=n%10;n=n/10;
			int last5=n%10;n=n/10;
			int last6=n%10;n=n/10;
			int last7=n;
			
			if(pow(last1,5)+pow(last2,5)+pow(last3,5)+pow(last4,5)+pow(last5,5)+pow(last6,6)+pow(last7,7)==i) {
				System.out.println(i);
				sum+=i;
			}
			
		}
		System.out.println("sum="+sum);
	}

}
