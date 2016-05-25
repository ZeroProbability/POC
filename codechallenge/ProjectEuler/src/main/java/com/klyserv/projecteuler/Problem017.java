package com.klyserv.projecteuler;


public class Problem017 {
	public class LetterCount {
	    
	    /** Creates a new instance of LetterCount */
	    public LetterCount() {
	        int onetonine = "onetwothreefourfivesixseveneightnine".length();
	        int tentonineteen = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen".length();
	        int and = "and".length();
	        int twentytoninety = "twentythirtyfortyfiftysixtyseventyeightyninety".length();
	        int hundred = "hundred".length();
	        int thousand = "thousand".length();
	        count = "one".length() + thousand + 
	          900*hundred + 100*onetonine + 
	          100*twentytoninety + 891*and + 
	          80*onetonine + 10*(onetonine + tentonineteen);
	    }
	 
	    int count;
	    
	    int getCount(){return count;}
	    
	}
	
	private static int length(String s) {
		int length=0;
		for(char c:s.toCharArray()){
			if(c!=' ') length++; 
		}
		return length;
	}
	
	public static void main(String[] args) {
		int sum=0;
		for(int i=1;i<=100000;i++) {
			sum+=length(Helper.toWordsUpTo999999(i));
		}
		System.out.println(sum);
	}

}
