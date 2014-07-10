package com.klyserv.codejam2014;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class DeceitfulWar {
	
	private static Scanner reader;
	
	private static BufferedWriter writer;
	
	private static class Problem {
		private int blockCount;
		
		private List<Double> blocksNaomi;
		private List<Double> blocksKen;
		
		private String solve() {
			int kenChoice=0;
			int naomiSkipCount=0;
			outer1:for(int naomiChoice=0;naomiChoice<blockCount;naomiChoice++, kenChoice++) {
				while(blocksNaomi.get(naomiChoice)<blocksKen.get(kenChoice)) {
					naomiSkipCount++;
					naomiChoice++;
					if(naomiChoice>=blockCount) break outer1;
				}
			}
			int deceitfulWin=blockCount-naomiSkipCount;
			
			kenChoice=0;
			int kenSkipCount=0;
			outer:for(int naomiChoice=0;naomiChoice<blockCount && kenChoice<blockCount;naomiChoice++,kenChoice++) {
				while(blocksNaomi.get(naomiChoice)>blocksKen.get(kenChoice)) {
					kenSkipCount++;
					kenChoice++;
					if(kenChoice>=blockCount) break outer;
				}
			}
			int realWin=kenSkipCount;
			
			return (deceitfulWin+" "+realWin);

		}
		
		private static Problem read() {
			Problem p=new Problem();
			p.blockCount=reader.nextInt();
			p.blocksKen=new ArrayList<Double>();
			p.blocksNaomi=new ArrayList<Double>();
			for(int i=0;i<p.blockCount;i++) {
				p.blocksNaomi.add(reader.nextDouble());
			}
			Collections.sort(p.blocksNaomi);
			// System.out.println("Naomi=>"+p.blocksNaomi);
			for(int i=0;i<p.blockCount;i++) {
				p.blocksKen.add(reader.nextDouble());
			}
			Collections.sort(p.blocksKen);
			// System.out.println("Ken=>"+p.blocksKen);
			return p;
		}
		
	}
	
	public static void main(String[] args) throws Exception {
		DeceitfulWar ms=new DeceitfulWar();
		ms.openFile("large1.txt");
		int probCount=ms.readproblemCount();

		for(int probNumber=1;probNumber<=probCount;probNumber++) {
			Problem p=Problem.read();
			ms.writeConsole("Case #"+probNumber+": "+p.solve());
		}
		
		ms.closeFile();
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
