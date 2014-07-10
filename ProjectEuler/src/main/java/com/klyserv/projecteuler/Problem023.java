package com.klyserv.projecteuler;

import java.math.BigInteger;
import java.util.LinkedHashSet;
import java.util.Set;

public class Problem023 {
	
	private static Set<Integer> abundantList=new LinkedHashSet<Integer>();
	
	private static boolean isAbundant(int i) {
		BigInteger sum=Helper.sumCollection(Factors.findFactors(i)).subtract(BigInteger.valueOf(i));
		return BigInteger.valueOf(i).compareTo(sum)<0;
	}
	
	private static boolean canBeExpressedAsSum(int i) {
		for(int firstNum:abundantList) {
			int possibleSecondNum=i-firstNum;
			if(possibleSecondNum< firstNum) return false;
			if(abundantList.contains(possibleSecondNum)) return true;
		}
		return false;
	}
	
	public static void main(String[] args) {
		for(int i=1;i<28124;i++){
			if(isAbundant(i)) abundantList.add(i);
		}
		long sum=0;
		for(int i=1;i<28124;i++){
			if(!canBeExpressedAsSum(i))
				sum+=i;
		}
		System.out.println(sum);
	}

}
