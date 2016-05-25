package com.klyserv.projecteuler;

public class Problem033 {
	public static void main(String[] args) {
		long superNum=1; long superden=1;
		for(int num=11;num<100;num++) {
			if(num%10==0) continue;
			int nd1=num/10;int nd2=num%10;
			for(int den=num+1;den<100;den++){
				if(num==den) continue;
				int dd1=den/10;int dd2=den%10;
				boolean isSolution=false;
				if(nd1==dd1) {
					isSolution=(num*dd2==den*nd2);
				} else if(nd1==dd2) {
					isSolution=(num*dd1==den*nd2);
				} else if(nd2==dd1) {
					isSolution=(num*dd2==den*nd1);
				} else if(nd2==dd2) {
					isSolution=(num*dd1==den*nd1);
				}
				
				if(isSolution) {
					System.out.println(num+"/"+den);
					superNum*=num;
					superden*=den;
					long divider=Helper.gcd(superNum, superden);
					superNum=superNum/divider;
					superden=superden/divider;
				}
				
			}
		}
		
		System.out.println(superNum+"/"+superden);
	}
}
