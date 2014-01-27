package com.klyserv.projecteuler;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Problem022 {
	
	private static long nameValue(String name) {
		long value=0;
		for(char c:name.toCharArray()) {
			value=value+(c-'A'+1);
		}
		return value;
	}
	
	public static void main(String[] args) throws Exception {
		File f=new File("Problem022-names.txt");
		BufferedReader br=new BufferedReader(new FileReader(f));
		String allNames=br.readLine();
		br.close();
		
		int pos=1;
		long sum=0;
		List<String> namesList=Arrays.asList(allNames.split(","));
		Collections.sort(namesList);
		for(String name:namesList) {
			name=name.replaceAll("\"", "");
			sum+=(pos*nameValue(name));
			pos++;
		}
		System.out.println(sum);
		
	}

}
