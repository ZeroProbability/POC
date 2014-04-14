package com.klyserv.codejam2014;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class Minesweeper {
	
	private static final boolean OUTPUT_TO_CONSOLE=true;
	
	private static Scanner reader;
	private static BufferedWriter writer;
	
	public static void main(String[] args) throws Exception {
		Minesweeper ms=new Minesweeper();
		ms.openFile("large1.txt");
		int probCount=ms.readproblemCount();

		for(int probNumber=1;probNumber<=probCount;probNumber++) {
			Problem p=Problem.read();
			String outputString="Case #"+probNumber+": "+p.solve();
			if(OUTPUT_TO_CONSOLE)
				ms.writeConsole(outputString);
			else 
				ms.write(outputString);
		}
		
		ms.closeFile();
	}

	private void writeConsole(String string) {
		System.out.print(string);
	}

	private void write(String string) throws Exception {
		writer.write(string);
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
	
	/* solve here */
	
	private static class Problem {
		private int row;
		private int column;
		private int minesCount;
		private Matrix matrix;
		
		private String solve() {
			int m=minesCount+1,tm=minesCount;
			int emptyRows=matrix.emptyRowCount();
			int emptyColumns=matrix.emptyColumnCount();
			int minSize=emptyRows<emptyColumns?emptyRows:emptyColumns;
			
			while(tm<m && tm>=minSize) {
				m=tm;
				tm=matrix.fillOneRowOrColumn(m);
				emptyRows=matrix.emptyRowCount();
				emptyColumns=matrix.emptyColumnCount();
				minSize=emptyRows<emptyColumns?emptyRows:emptyColumns;
			}
			m=tm;
			
			for(int c=emptyColumns;c>2 && m>0 && emptyRows>2; m--,c--) { // leave first two columns & rows empty
				matrix.map[emptyRows][c]=Matrix.MINE;
			}
			
			matrix.map[1][1]=Matrix.CHOOSE;
			if(m>1) throw new RuntimeException("Error");// it should be 1 or less; 
			
			if(m==1 && emptyRows-1>2 && emptyColumns>2) { matrix.map[emptyRows-1][emptyColumns]=Matrix.MINE; m--; }
			
			if(m==1) return "\nImpossible\n";
			if(matrix.map[2][2]==Matrix.MINE && matrix.map[1][2]==Matrix.MINE && matrix.map[2][1]==Matrix.MINE) return matrix.toString();
			if(matrix.column>1 && matrix.map[1][2]==Matrix.MINE && matrix.row>1)  return "\nImpossible\n";
			if(matrix.row>1 && matrix.map[1][2]==Matrix.MINE && matrix.column>1)  return "\nImpossible\n";
			if(matrix.column>1 && matrix.row>1 && matrix.map[2][2]==Matrix.MINE) return "\nImpossible\n";
			return matrix.toString();
		}
		
		private static Problem read() {
			Problem p=new Problem();
			p.row=reader.nextInt();
			p.column=reader.nextInt();
			p.minesCount=reader.nextInt();
			p.matrix=new Matrix(p.row, p.column);
			return p;
		}
		
	}
	
	private static class Matrix {
		private int row;
		private int column;
		private int[][] map;
		
		private static final int MINE=-1;
		private static final int EMPTY=0;
		private static final int CHOOSE=-2;
		
		public Matrix(int row, int column) {
			this.row=row; this.column=column;
			map=new int[row+2][column+2];
			for(int r=0;r<row+1;r++) {
				for(int c=0;c<column+1;c++) {
					map[r][c]=EMPTY;
				}
			}
		}
		
		public int emptyRowCount() {
			int rowCount=0;
			for(int r=1;r<=row;r++) {
				if(map[r][1]==EMPTY) rowCount++;
			}
			return rowCount;
		}
		
		public int emptyColumnCount() {
			int columnCount=0;
			for(int c=1;c<=column;c++) {
				if(map[1][c]==EMPTY) columnCount++;
			}
			return columnCount;
		}
		
		public int fillOneRowOrColumn(int mineCount) {
			int rowCount=emptyRowCount();
			int columnCount=emptyColumnCount();
			int colSize=rowCount;
			int rowSize=columnCount;
			if(colSize<rowSize) { 
				// fill columns
				for(int r=1;r<=rowCount;r++) {
					map[r][columnCount]=MINE;
				}
				mineCount=mineCount-rowCount;
			} else { 
				// fill rows
				for(int c=1;c<=columnCount;c++) {
					map[rowCount][c]=MINE;
				}
				mineCount=mineCount-columnCount;
			}
			return mineCount;
		}

		public String toString() {
			StringBuffer sb=new StringBuffer("\n");
			for(int r=1;r<=row;r++) {
				for(int c=1;c<=column;c++) {
					if(map[r][c]==MINE) {
						sb.append("*");
					} else if(map[r][c]==CHOOSE){
						sb.append("c");
					} else {
						sb.append(".");
					}
				}
				sb.append("\n");
			}
			return sb.toString();
		}
		
	}
	
}
