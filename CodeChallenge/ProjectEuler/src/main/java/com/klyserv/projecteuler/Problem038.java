package com.klyserv.projecteuler;

public class Problem038 {
	
	private static boolean isValid(String s) {
		int l=s.length();

		for(int i=0;i<l;i++) 
			if(s.charAt(i)=='0') return false;
		
		for(int i=0;i<l;i++) {
			for(int j=i+1;j<l;j++) {
				if(s.charAt(i)==s.charAt(j)) return false;
			}
		}
		return true;
	}
	
	public static void main(String[] args) {
		String maxValue="0";
		for(int i=1;i<10000000;i++) {
			String concatString="";
			int p1=i*1;
			int p2=i*2;
			concatString+=p1;concatString+=p2;
			
			int n=3;
			while(concatString.length()<9) {
				int pn=i*n;
				concatString+=pn;
				n++;
			}
			if(concatString.length()>9) continue; 
			
			if(isValid(concatString)) {
				if(maxValue.compareTo(concatString)<0) {
					System.out.println(concatString);
					maxValue=concatString;
				}
			}
		}
		
	}

}
