package com.klyserv.projecteuler;

public class Problem039 {
	
	public static void main(String[] args) {

		int maxSolutionCount=0;
		for (int p = 3; p < 1000; p++) {
			int solutionCount=0;
			for (int a = 1; a < 1000; a++) {
				for (int b = a; b < 1000; b++) {
					int c=p-a-b;
					
					if(c<b) break; // no more solution
					
					if(a+b<=c || a+c<=b || b+c<=a) continue; // cant form triangle
					
					if(c*c==(a*a+b*b)) {
						//System.out.println(a+" "+b+" "+c);
						solutionCount++;
					}
					
				}
			}
			if(solutionCount>maxSolutionCount) {
				System.out.println("p="+p+" has "+solutionCount+" solution(s).");
				maxSolutionCount=solutionCount;
			}
		}
	}

}
