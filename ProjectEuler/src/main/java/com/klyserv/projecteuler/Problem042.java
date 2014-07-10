package com.klyserv.projecteuler;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashSet;
import java.util.Set;

public class Problem042 {
	
	public static void main(String[] args) throws Exception {
		File f=new File("Problem042-words.txt");
		FileReader fr=new FileReader(f);
		BufferedReader br=new BufferedReader(fr);
		String words=br.readLine();
		br.close();
		
		Set<Integer> triangleNums=new HashSet<Integer>(); 
		
		for(int i=1;i<1000;i++) {
			triangleNums.add(i*(i+1)/2);
		}
		
		
		words=words.replaceAll("\"", "");
		int counter=0;
		for(String w:words.split(",")){
			int sum=0;
			for(char c:w.toCharArray()) {
				sum+=(c-'A'+1);
			}
			if(triangleNums.contains(sum)) 
				counter++;
		}
		
		System.out.println("count="+counter);
	}

}
