package com.klyserv.projecteuler;

import java.util.HashMap;
import java.util.Map;

public class Problem014 {
	
	private static Map<Long, Long> chainLengthLookup=new HashMap<Long, Long>();
	
	public static long chainLength(long i) {
		if(chainLengthLookup.containsKey(i)) return chainLengthLookup.get(i);

		long length=1;
		long originalValue=i;
		while(i>1) {
			if(chainLengthLookup.containsKey(i)) {
				length+=chainLengthLookup.get(i);
				break;
			}
			length++;
			if(i%2==0) {
				i=i/2;
			}
			else {
				i=3*i+1;
			}
		}
		chainLengthLookup.put(originalValue, length);
		return length;
	}
	
	public static void main(String[] args) {
		for(long i=1;i<1000*1000;i++){
			chainLength(i);
		}
		long maxLength=0;
		for(long i:chainLengthLookup.keySet()) {
			if(chainLengthLookup.get(i)>maxLength) {
				System.out.println(i+" => "+chainLengthLookup.get(i));
				maxLength=chainLengthLookup.get(i);
			}
		}
	}

}
