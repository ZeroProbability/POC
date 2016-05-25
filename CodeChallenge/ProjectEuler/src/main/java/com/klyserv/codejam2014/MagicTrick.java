package com.klyserv.codejam2014;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class MagicTrick {
	
	private static Scanner reader;
	
	private static BufferedWriter writer;

	private static class Problem {
		private int firstAnswer;
		private Integer[][] firstArrangement;
		private int secondAnswer;
		private Integer[][] secondArrangement;
		
		private String solve() {
			Set<Integer> firstSet=new HashSet<Integer>(Arrays.asList(firstArrangement[firstAnswer-1]));
			Set<Integer> secondSet=new HashSet<Integer>(Arrays.asList(secondArrangement[secondAnswer-1]));
			
			firstSet.retainAll(secondSet);
			
			if(firstSet.size()==1) return Integer.toString(firstSet.iterator().next());
			if(firstSet.size()==0) return "Volunteer cheated!";
			return "Bad magician!";
		}
		
		private static Problem read() {
			Problem problem=new Problem();
			problem.firstAnswer=reader.nextInt();
			problem.firstArrangement=new Integer[4][];
			for(int i=0;i<4;i++){
				problem.firstArrangement[i]=new Integer[4];
				for(int j=0;j<4;j++){
					problem.firstArrangement[i][j]=reader.nextInt();
				}
			}

			problem.secondAnswer=reader.nextInt();
			problem.secondArrangement=new Integer[4][];
			for(int i=0;i<4;i++){
				problem.secondArrangement[i]=new Integer[4];
				for(int j=0;j<4;j++){
					problem.secondArrangement[i][j]=reader.nextInt();
				}
			}
			return problem;
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		MagicTrick mt=new MagicTrick();
		mt.openFile("small1.txt");
		int probCount=mt.readproblemCount();

		for(int probNumber=1;probNumber<=probCount;probNumber++) {
			Problem p=Problem.read();
			mt.write("Case #"+probNumber+": "+p.solve());
		}
		
		mt.closeFile();
	}

	@SuppressWarnings("unused")
	private void writeConsole(String string) {
		System.out.println(string);
	}

	private void write(String string) throws Exception {
		writer.write(string+"\n");
	}

	private int readproblemCount() {
		return reader.nextInt();
	}

	private void closeFile() throws Exception {
		reader.close();
		writer.close();
	}

	private void openFile(String fileName) throws Exception {
		File inputFile=new File(fileName);
		reader = new Scanner(inputFile);
		
		File outputFile=new File("output.txt");
		if (!outputFile.exists()) {
			outputFile.createNewFile();
		}
		FileWriter fw = new FileWriter(outputFile);
		writer=new BufferedWriter(fw);
	}

}
