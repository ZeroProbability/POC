package com.klyserv.codejam2014;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Scanner;

public class CookieProblem {
	
	private static Scanner reader;
	
	private static BufferedWriter writer;

	private static class Problem {
		Double costOfFarm;
		Double farmProductionRate;
		Double targetCookies;
		
		private String solve() {
			int farmCount=0;
			double s=0.0;
			for(farmCount=0;farmCount<Integer.MAX_VALUE;farmCount++){
				double timeForNewFarm=costOfFarm/(2+farmProductionRate*farmCount);
				double timeForTarget=targetCookies/(2+farmProductionRate*farmCount);
				double timeForTargetInNext=targetCookies/(2+farmProductionRate*(farmCount+1));
				
				double rsum=s+timeForTarget;
				double rsum1=s+timeForNewFarm+timeForTargetInNext;
				if(rsum<rsum1) break;
				s=s+timeForNewFarm;
			}
			double answer=s+targetCookies/(2+farmProductionRate*farmCount);
			BigDecimal bd = new BigDecimal(answer);
			bd = bd.setScale(7, RoundingMode.HALF_UP);
			
			return Double.toString(bd.doubleValue());
		}
		
		private static Problem read() {
			Problem p=new Problem();
			p.costOfFarm=reader.nextDouble();
			p.farmProductionRate=reader.nextDouble();
			p.targetCookies=reader.nextDouble();
			return p;
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		CookieProblem cp=new CookieProblem();
		cp.openFile("large1.txt");
		int probCount=cp.readproblemCount();

		for(int probNumber=1;probNumber<=probCount;probNumber++) {
			Problem p=Problem.read();
			cp.writeConsole("Case #"+probNumber+": "+p.solve());
		}
		
		cp.closeFile();
	}

	private void writeConsole(String string) {
		System.out.println(string);
	}

	@SuppressWarnings("unused")
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
