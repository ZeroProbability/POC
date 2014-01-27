package com.klyserv.projecteuler;

import java.math.BigInteger;
import java.util.Set;
import java.util.TreeSet;

public class Problem029 {
	
	public static void main(String[] args) {
		int max=100;
		Set<BigInteger> result=new TreeSet<BigInteger>();
		for(int a=2;a<=max;a++) {
			for(int b=2;b<=max;b++) {
				result.add(BigInteger.valueOf(a).pow(b));
				result.add(BigInteger.valueOf(b).pow(a));
			}
		}
//		for(BigInteger i:result){
//			System.out.println(i);
//		}
		System.out.println(result.size());
	}

}
