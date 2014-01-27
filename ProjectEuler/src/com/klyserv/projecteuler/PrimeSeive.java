package com.klyserv.projecteuler;

public class PrimeSeive {

	private boolean[] isPrime = null;
	
	private int currentPrime=2;
	
	private boolean endOfSearch=false;

	public PrimeSeive(int max) {
		isPrime = new boolean[max+1];
		isPrime[0]=isPrime[1]=false;
		for(int i=2;i<max+1;i++) {
			isPrime[i]=true;
		}
	}
	
	private void seive(int factor) {
		isPrime[factor]=true;
		for(int i=factor+factor;i<isPrime.length;i+=factor) {
			isPrime[i]=false;
		}
	}
	
	public int getNextPrime() {
		if(isEndOfSearch()) return currentPrime;
		if(currentPrime==isPrime.length) {
			setEndOfSearch(true);
			return currentPrime;
		}
		seive(currentPrime);
		int ret=currentPrime;
		for(int i=currentPrime+1;i<isPrime.length;i++){
			if(isPrime[i]) {
				currentPrime=i;
				return ret;
			}
		}
		setEndOfSearch(true);
		return currentPrime;
	}
	
	public static void main(String[] args) {
		PrimeSeive ps=new PrimeSeive(100);
		while(!ps.isEndOfSearch()){
			System.out.println(ps.getNextPrime());
		}
		System.out.println(ps.isPrime(3));
	}

	public boolean isEndOfSearch() {
		return endOfSearch;
	}

	private void setEndOfSearch(boolean endOfSearch) {
		this.endOfSearch = endOfSearch;
	}
	
	private void computeAll() {
		while(!isEndOfSearch()){
			getNextPrime();
		}
	}
	
	public boolean isPrime(int i) {
		if(i<2) return false;
		computeAll();
		return(isPrime[i]); 
	}

}
