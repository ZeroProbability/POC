package com.klyserv.projecteuler;

import java.util.HashMap;
import java.util.Map;

public class Problem026 {
	
	public static String findRecurring(int i) {
		String ret="0.";
		Map<Integer,Integer> m=new HashMap<Integer, Integer>(); //contains previous reminder and position
		int pos=1;
		int r=1;
		while(true) {
			m.put(r*10, pos);
			int r1=(r*10)%i;
			int q=(r*10)/i;
			ret+=q;
			r=r1;
			if(m.containsKey(r*10)) {
				int firstPos=m.get(r*10);
				String s=ret.substring(0,firstPos+1);
				s+="(";
				s+=ret.substring(firstPos+1)+")";
				ret=s;
				return ret;
			}
			if(r==0) break;
			pos++;
		}
		return ret;
	}
	
	private static int recurringLength(String str){
		int strat=str.indexOf('(');
		if(strat==-1) return 0;
		int end=str.indexOf(')');
		return end-strat-1;
	}
	
	public static void main(String[] args) {
		int maxRecLenth=0;
		for(int i=2;i<1000;i++){
			int recLen=recurringLength(findRecurring(i));
			if(recLen>maxRecLenth) {
				System.out.println(i+" => "+recLen);
				maxRecLenth=recLen;
			}
		}
		
	}

}
