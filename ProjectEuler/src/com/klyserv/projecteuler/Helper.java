package com.klyserv.projecteuler;

import java.math.BigInteger;
import java.util.Collection;

public class Helper {
	
	private static final BigInteger _0=BigInteger.ZERO;
	private static final BigInteger _1=BigInteger.ONE;
	private static final BigInteger _10=BigInteger.TEN;

	public static long max(long first, long second, long... n) {
		long ret=first>second?first:second;
		
		for(int i=0;i<n.length;i++) {
			if(n[i]>ret) ret=n[i];
		}
		
		return ret;
	}
	
	public static long min(long first, long second, long... n) {
		long ret=first>second?second:first;
		
		for(int i=0;i<n.length;i++) {
			if(n[i]<ret) ret=n[i];
		}
		
		return ret;
	}
	
	public static long gcd(long first, long second) {
		long ret=min(first,second);
		long other=max(first,second);
		while(other%ret!=0) {
			long temp=ret;
			ret=other%ret;
			other=temp;
		}
		return ret;
	}
	
	public static long lcm(long first, long second) {
		return first*second/gcd(first,second);
	}
	
	public static long npr(int n, int r) {
		long npr=1;
		for(int i=n;i>=n-r+1;i--) {
			npr*=i;
		}
		return npr;
	}
	
	public static BigInteger factorial(int r) {
		BigInteger prod=BigInteger.ONE;
		for(int i=1;i<=r;i++){
			prod=prod.multiply(BigInteger.valueOf(i));
		}
		return prod;
	}
	
	public static long ncr(int n, int r) {
		long prod=1;
		for(int i=1;i<=r;i++){
			prod*=(n-i+1);
			prod=prod/i;
		}
		return prod;
	}
	
	public static BigInteger sumDigits(BigInteger n) {
		BigInteger sum=BigInteger.ZERO;
		while(n.compareTo(BigInteger.ZERO)>0){
			sum=sum.add(n.remainder(BigInteger.TEN));
			n=n.divide(BigInteger.TEN);
		}
		return sum;
	}
	
	private static String toWordsUpTo20(int i) {
		switch(i) {
		case 0: return ""; // zero is special case should be handled elsewhere
		case 1: return "one";
		case 2: return "two";
		case 3: return "three";
		case 4: return "four";
		case 5: return "five";
		case 6: return "six";
		case 7: return "seven";
		case 8: return "eight";
		case 9: return "nine";
		case 10: return "ten";
		case 11: return "eleven";
		case 12: return "twelve";
		case 13: return "thirteen";
		case 14: return "fourteen";
		case 15: return "fifteen";
		case 16: return "sixteen";
		case 17: return "seventeen";
		case 18: return "eighteen";
		case 19: return "nineteen";
		case 20: return "twenty";
		default: throw new RuntimeException("this method can not handle more than 20");
		}
	}
	
	private static String toWordsUpTo99(int i) {
		if(i>99) throw new RuntimeException("this method can not handle more than 99");
		if(i<21) return toWordsUpTo20(i);
		if(i/10==2) return "twenty "+toWordsUpTo20(i%10);
		if(i/10==3) return "thirty "+toWordsUpTo20(i%10);
		if(i/10==4) return "forty "+toWordsUpTo20(i%10);
		if(i/10==5) return "fifty "+toWordsUpTo20(i%10);
		if(i/10==6) return "sixty "+toWordsUpTo20(i%10);
		if(i/10==7) return "seventy "+toWordsUpTo20(i%10);
		if(i/10==8) return "eighty "+toWordsUpTo20(i%10);
		if(i/10==9) return "ninety "+toWordsUpTo20(i%10);
		throw new RuntimeException("should never reach here!! i="+i);
	}
	
	private static String toWordsUpTo999(int i) {
		if(i>999) throw new RuntimeException("this method can not handle more than 999");
		if(i<100) return toWordsUpTo99(i);
		String suffix=((i%100)>0)?(" and "+toWordsUpTo99(i%100)):"";
		return(toWordsUpTo20(i/100)+" hundred"+suffix);
	}

	public static String toWordsUpTo999999(int i) {
		if(i>999999) throw new RuntimeException("this method can not handle more than 999999");
		if(i<1000) return toWordsUpTo999(i);
		return(toWordsUpTo999(i/1000)+" thousand "+toWordsUpTo999(i%1000));
	}
	
	public static BigInteger sumCollection(Collection<Long> collection){
		BigInteger sum=BigInteger.ZERO;
		for(Long i:collection){
			sum=sum.add(BigInteger.valueOf(i));
		}
		return sum;
	}
	
	private static BigInteger calcualteN(BigInteger n, BigInteger leftNum, int rightMostDigit, String nextTwoDigits) {
		BigInteger n1=leftNum.multiply(BigInteger.valueOf(rightMostDigit));
		n=n.subtract(n1).multiply(BigInteger.valueOf(100));
		BigInteger nextTwoDigitsN=BigInteger.valueOf(Integer.parseInt(nextTwoDigits));
		return n.add(nextTwoDigitsN);
	}
	
	public static String sqrt(String inNumAsStr){
		int nToAnalyze=0;
		int positionAtString=0;
		if(inNumAsStr.length()%2==1) {
			nToAnalyze=Integer.parseInt(inNumAsStr.substring(0,1));
			positionAtString++;
		}
		BigInteger n=BigInteger.valueOf(nToAnalyze);
		int sqrt=(int)Math.sqrt(nToAnalyze);
		
		BigInteger leftNum=BigInteger.valueOf(sqrt);
		BigInteger topNum=BigInteger.valueOf(sqrt);

		do{
			int rightMostDigit=topNum.remainder(_10).intValue();
			n=calcualteN(n, leftNum, rightMostDigit, inNumAsStr.substring(positionAtString,positionAtString+2));
			
			leftNum=leftNum.add(BigInteger.valueOf(rightMostDigit));
			
			int possibleNextNumber=0;
			for(BigInteger i=_0;i.compareTo(_10)<0;i=i.add(_1)) {
				if(leftNum.multiply(_10).add(i).multiply(i).compareTo(n)>0) break;
				possibleNextNumber=i.intValue();
			}
			
			leftNum=leftNum.multiply(_10).add(BigInteger.valueOf(possibleNextNumber));
			topNum=topNum.multiply(_10).add(BigInteger.valueOf(possibleNextNumber));
			positionAtString+=2;
			
		} while(positionAtString<inNumAsStr.length());
		
		int rightMostDigit=topNum.remainder(_10).intValue();
		n=calcualteN(n, leftNum, rightMostDigit, "00");
		
		// TODO: what if there is a reminder?
		
		return topNum.toString();
	}
	
	public static boolean isSquare(BigInteger i) {
		int lastDigit=i.remainder(_10).intValue();
		if(lastDigit==2||lastDigit==3||lastDigit==7||lastDigit==8) return false;
		BigInteger sqrt=new BigInteger(sqrt(i.toString()));
		return(i.subtract(sqrt.multiply(sqrt)).compareTo(_0)==0);
	}
	
	public static int numDigits(long i) {
		int c=1;
		while((i=i/10)>0) c++;
		return c;
	}
	
	public static int rotateNumber(int i){
		return rotateNumber(i, numDigits(i));
	}
	
	public static int rotateNumber(int i, int size){
		if(size<numDigits(i)) throw new RuntimeException("Size "+size+" is less than number of digits "+numDigits(i));
		if(i<10) return i;
		int lastDigit=i%10;
		i=i/10;
		for(int x=0;x<size-1;x++) lastDigit*=10;
		return i+lastDigit;
	}
	
	public static boolean isPalindrome(String inputString) {
		StringBuffer sb=new StringBuffer(inputString);
		sb.reverse();
		return(inputString.equals(sb.toString()));
	}
	
	public static long chopLeft(long in) {
		long n = 1;
		int nD=numDigits(in);
		nD=nD-1;
		for (int i = 0; i < nD; i++)
			n *= 10;
		return in%n;
	}
}
