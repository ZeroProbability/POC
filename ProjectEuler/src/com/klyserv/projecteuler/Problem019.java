package com.klyserv.projecteuler;

public class Problem019 {
	
	private enum Month {
		JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC
		
	}
	
	private static int daysInMonth(int year, Month month) {
		if(month==Month.JAN || month==Month.MAR ||month==Month.MAY ||month==Month.JUL ||month==Month.AUG || month==Month.OCT || month==Month.DEC) 
			return 31;
		if(month==Month.APR || month==Month.JUN ||month==Month.SEP ||month==Month.NOV) 
			return 30;
		if(year%400==0) return 29;
		if(year%100==0) return 28;
		if(year%4==0) return 29;
		return 28;
	}
	
	public static void main(String[] args) {
		// zero - sunday .. six - saturday
		int nextMonth1stDay=1; // Monday
		int count=0;
		for(int year=1900;year<2001;year++) {
			for(Month m: Month.values()) {
				nextMonth1stDay=(nextMonth1stDay+daysInMonth(year, m))%7;
				if(nextMonth1stDay==0) {
					int evalYear=year;
					System.out.println("year="+year+" month="+m); // following month actually 
					if(m==Month.DEC) evalYear++;
					if(evalYear>1900 && evalYear<2001) count++;
				}
			}
		}
		System.out.println("count="+ count);
	}

}
