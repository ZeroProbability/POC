package com.klyserv.projecteuler;

public class Problem086 {
	
	public static boolean isIntSquare(long square) {
		long l=(long) Math.sqrt(square);
		return(l*l==square);
	}
	
	public static boolean isValidSet(int i, int j, int k) {
		long cand1=i*i+(j+k)*(j+k);
		long cand2=j*j+(i+k)*(i+k);
		long cand3=k*k+(j+i)*(j+i);
		
		long shortest=Helper.min(cand2, cand1, cand3);
		
		boolean valid=isIntSquare(shortest);
		//if(valid) System.out.println(i+" "+j+" "+k);
		return valid;
	}
	
	public static void main(String[] args) {
		long sum=0;
		int n=1;
		while(n<10000) { // some huge value
			for(int i=1;i<=n;i++){
				for(int j=i;j<=n;j++){
					if(isValidSet(i, j, n)) sum++;
				}
			}
			
			if(sum>1000*1000) {
				break;
			}
			n++;
			
		}
		System.out.println(n+" > "+ sum);
	}

}
