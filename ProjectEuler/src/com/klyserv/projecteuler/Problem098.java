package com.klyserv.projecteuler;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Problem098 {
	
	private static String sortCharsInWord(String inStr) {
		char[] sortedArray=inStr.toCharArray();
		Arrays.sort(sortedArray);
		return new String(sortedArray);
	}
	
	private static List<String> readFileInput() throws Exception {
		Reader r=new FileReader(new File("Problem098-words.txt"));
		BufferedReader br=new BufferedReader(r);
		String fullString=br.readLine();
		br.close();
		return Arrays.asList(fullString.replaceAll("\"","").split(","));
	}
	
	private static boolean isASquare(String str) {
		long n=Long.parseLong(str);
		long sqrt=(long)Math.sqrt(n);
		return n==(sqrt*sqrt);
	}
	
	private static String isThisASolution(long squareNumber, String word1, String word2) {
		String strSquareNumber=Long.toString(squareNumber);
		if(strSquareNumber.length()!=word1.length()) return null;
		
		Map<Character,Character> mci=new HashMap<Character, Character>();
		
		for(int i=0;i<word1.length();i++) {
			if(mci.containsKey(word1.charAt(i)) && word1.charAt(i)!=strSquareNumber.charAt(i)) return null;
			mci.put(word1.charAt(i), strSquareNumber.charAt(i));
		}
		
		for(char i:mci.keySet()) {
			for(char j:mci.keySet()){
				if(i==j) continue;
				if(mci.get(i)==mci.get(j)) return null;
			}
		}
		
		String newSquare="";
		for(int i=0;i<word2.length();i++) {
			newSquare+=mci.get(word2.charAt(i));
		}
		
		if(newSquare.charAt(0)=='0') return null;
		
		if(isASquare(newSquare)) return newSquare;
		
		return null;
	}
	
	public static void main(String[] args) throws Exception {
		Map<String,List<String>> anagramLookup=new HashMap<String, List<String>>();
		List<String> inputStrList=readFileInput();
		for(String str:inputStrList) {
			String lookup=sortCharsInWord(str);
			List<String> possibleAnagrams=null;
			if(anagramLookup.containsKey(lookup)) {
				possibleAnagrams=anagramLookup.get(lookup);
			} else {
				possibleAnagrams=new ArrayList<String>();
			}
			possibleAnagrams.add(str);
			anagramLookup.put(lookup, possibleAnagrams);
		}
		
		Map<String,List<String>> filteredAnagramLookup=new HashMap<String, List<String>>();
		for(String lookup:anagramLookup.keySet()) 
			if(anagramLookup.get(lookup).size()>1) filteredAnagramLookup.put(lookup, anagramLookup.get(lookup));
		
		for(String lookup:filteredAnagramLookup.keySet()) {
			for(int i=1;i<10000000;i++) {
				long sqr=i*i;
				int numSize=Long.toString(sqr).length();
				List<String> anagramWords=filteredAnagramLookup.get(lookup);
				if(numSize>anagramWords.get(0).length()) break;
				if(numSize<anagramWords.get(0).length()) continue;
				
				String solution=isThisASolution(sqr, anagramWords.get(0), anagramWords.get(1));
				if(solution!=null) {
					System.out.println(sqr+","+solution+"=>"+anagramWords);
				};
			}
		}
		
	}

}
