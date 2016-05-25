package com.klyserv.projecteuler;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class PrimeFactors {
	
	public static class Factor {
		private int factor=0;
		
		private int times=0;
		
		public Factor(int factor) {
			this(factor,1);
		}

		public Factor(int factor, int times) {
			setFactor(factor);
			setTimes(times);
		}

		public int getFactor() {
			return factor;
		}

		private void setFactor(int factor) {
			this.factor = factor;
		}

		public int getTimes() {
			return times;
		}

		private void setTimes(int times) {
			this.times = times;
		}
		
		private void incTimes() {
			this.times++;
		}
		
		@Override
		public String toString() {
			return "Factor("+this.factor+"^"+this.times+")";
		}
		
	}
	
	private List<Factor> factorList;
	
	private PrimeFactors() {
	}
	
	public PrimeFactors(long number) {
		int maxPossibleFactor=(int)Math.sqrt(number);
		
		PrimeSeive ps=new PrimeSeive(maxPossibleFactor);
		
		factorList=new ArrayList<Factor>();
		
		while(!ps.isEndOfSearch()) {
			int nextPrime=ps.getNextPrime();
			if(number%nextPrime==0) {
				Factor f=new Factor(nextPrime);
				number=number/nextPrime;
				while(number%nextPrime==0) {
					f.incTimes();
					number=number/nextPrime;
				}
				factorList.add(f);
			}
		}
		if(number>1) factorList.add(new Factor((int) number));
		factorList=Collections.unmodifiableList(factorList);
	}
	
	public List<Factor> getFactorList() {
		return factorList; 
	}
	
	public static void main(String[] args) {
		PrimeFactors pf1=new PrimeFactors(15);
		PrimeFactors pf2=new PrimeFactors(100);
		PrimeFactors pf3=pf1.add(pf2);
		System.out.println(pf3);
		System.out.println(new PrimeFactors(70600674));
	}
	
	public PrimeFactors add(PrimeFactors other) {
		PrimeFactors ret=new PrimeFactors();
		ret.factorList=new ArrayList<Factor>();
		
		Map<Integer,Integer> sumMap=new HashMap<Integer, Integer>();
		
		for(Factor f:this.factorList) {
			sumMap.put(f.getFactor(), f.getTimes());
		}
		
		for(Factor f:other.factorList) {
			if(sumMap.containsKey(f.getFactor())) {
				if (sumMap.get(f.getFactor())<f.getTimes())
					sumMap.put(f.getFactor(), f.getTimes());
			} else {
				sumMap.put(f.getFactor(), f.getTimes());
			}
		}
		
		for(int i:sumMap.keySet()) {
			ret.factorList.add(new Factor(i, sumMap.get(i)));
		}
		ret.factorList=Collections.unmodifiableList(ret.factorList);
		
		return ret;
	}
	
	@Override
	public String toString() {
		return factorList.toString();
	}

}
