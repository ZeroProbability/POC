package com.klyserv.projecteuler;

public class Problem040 {
	
	public static void main(String[] args) {
		int product=1;
		
		int counter=0;
		int position=1;
		boolean forever=true;
		int intrestedPos=1;
		
		while(forever) {
			counter++;
			int positionOfNextNumber=position+Helper.numDigits(counter);
			
			if(intrestedPos>=position && intrestedPos<positionOfNextNumber) {
				char c=Integer.toString(counter).charAt(intrestedPos-position);
				intrestedPos*=10;
				product*=(c-'0');
				//System.out.println(c);
				if(intrestedPos>1000000) break;
			}

			position=positionOfNextNumber;
		}
		System.out.println(product);
	}

}
