package com.klyserv.projecteuler;

public class Problem044 {
	static final int max=100000;
	
	public static void main(String[] args) {
		for(int j=1;j<max;j++) {
			for(int k=j+1;k<max;k++){
				long pj=Helper.pentagonal(j);
				long pk=Helper.pentagonal(k);
				
				long sum=pj+pk;
				long diff=pk-pj;
				
				if(Helper.isPentagonal(sum)>0 && Helper.isPentagonal(diff)>0) {
					System.out.println(pj+" "+pk);
					System.out.println("sum="+sum);
					System.out.println("diff="+diff);
					System.exit(0);
				}
				
			}
		}
	}

}
