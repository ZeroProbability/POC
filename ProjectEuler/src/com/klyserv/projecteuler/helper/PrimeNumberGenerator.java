package com.klyserv.projecteuler.helper;

import java.util.ArrayList;
import java.util.List;

public class PrimeNumberGenerator {
	
	private boolean[] isPrime = null;
	
	private long currentPrime=2;
	
	private boolean endOfSearch=false;
	
	private long bufferStartPosition=0;
	
	private List<Long> primeNumbers=new ArrayList<Long>();

	public PrimeNumberGenerator(int buffersize) {
		primeNumbers.add(currentPrime);
		isPrime = new boolean[buffersize+1];
		isPrime[0]=isPrime[1]=false;
		for(int i=2;i<buffersize+1;i++) {
			isPrime[i]=true;
		}
	}
	
	private void seive(long factor) {
		isPrime[(int)(factor-bufferStartPosition)]=true; // TODO: handle long here
		for(long i=factor+factor;i<isPrime.length;i+=factor) {
			isPrime[(int)i]=false; // TODO: handle long here 
		}
	}

	public long getNextPrime() {
		seive(currentPrime);
		long ret=currentPrime;
		for(long i=currentPrime+1;i<isPrime.length;i++){
			if(isPrime[(int)i]) { // TODO: handle long here
				currentPrime=i;
				return ret;
			}
		}
		setEndOfSearch(true);
		return currentPrime;
	}

	public boolean isEndOfSearch() {
		return endOfSearch;
	}

	private void setEndOfSearch(boolean endOfSearch) {
		this.endOfSearch = endOfSearch;
	}
	

}
