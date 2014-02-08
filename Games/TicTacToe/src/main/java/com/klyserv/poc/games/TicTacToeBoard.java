package com.klyserv.poc.games;

public class TicTacToeBoard {
	
	public static final int EMPTY_CELL=0;
	public static final int X_CELL=1;
	public static final int O_CELL=2;
	
	public static final int BOARD_SIZE=3;
	
	private int[][] board=new int[3][3];
	
	private int nextPutType=X_CELL;
	
	public static class InvalidMoveException extends Exception {
		private static final long serialVersionUID = 1L;
	}
	
	public static class InvalidLocationException extends Exception {
		private static final long serialVersionUID = 1L;
	}
	
	public TicTacToeBoard() {
		for(int i=0;i<3;i++) {
			for(int j=0;j<3;j++) {
				board[i][j]=EMPTY_CELL;
			}
		}
	}
	
	private TicTacToeBoard(TicTacToeBoard other) {
		for(int i=0;i<3;i++) {
			for(int j=0;j<3;j++) {
				board[i][j]=other.board[i][j];
			}
		}
	}
	
	public TicTacToeBoard put(int i, int j, int value) throws InvalidMoveException{
		TicTacToeBoard t=new TicTacToeBoard(this);
		if(i<0||i>=BOARD_SIZE) throw new InvalidMoveException();
		if(j<0||j>=BOARD_SIZE) throw new InvalidMoveException();

		if(value==X_CELL||value==O_CELL||value==EMPTY_CELL)
			t.board[i][j]=value;

		if(value==X_CELL) t.nextPutType=O_CELL;
		if(value==O_CELL) t.nextPutType=X_CELL;
		return t;
	}
	
	public int getAt(int i, int j) throws InvalidLocationException {
		if(i<0||i>=BOARD_SIZE) throw new InvalidLocationException();
		if(j<0||j>=BOARD_SIZE) throw new InvalidLocationException();
		
		return board[i][j];
	}
	
	public int getNextPutType() {
		return nextPutType;
	}
	
	public boolean winPositionReached() {
		for(int i=0;i<BOARD_SIZE;i++) {
			for(int j=0;j<BOARD_SIZE;j++) {
				if(board[i][j]==TicTacToeBoard.EMPTY_CELL) continue;
				if((i+2)<BOARD_SIZE && board[i][j]==board[i+1][j] && board[i][j]==board[i+2][j]) return true;
				if((j+2)<BOARD_SIZE && board[i][j]==board[i][j+1] && board[i][j]==board[i][j+2]) return true;
				if((j+2)<BOARD_SIZE && (i+2)<BOARD_SIZE && board[i][j]==board[i+1][j+1] && board[i][j]==board[i+2][j+2]) return true;
				if((i+2)<BOARD_SIZE && (j-2)>=0 && board[i][j]==board[i+1][j-1] && board[i][j]==board[i+2][j-2]) return true;
			}
		}
		return false;
	}
	
	public int emptyCellCount() {
		int count=0;
		for(int i=0;i<3;i++) {
			for(int j=0;j<3;j++) {
				if(board[i][j]==EMPTY_CELL) count++;
			}
		}
		return count;
	}

	@Override
	public String toString() {
		StringBuilder sb=new StringBuilder();
		for(int i=0;i<BOARD_SIZE;i++) {
			for(int j=0;j<BOARD_SIZE;j++) {
				switch (board[i][j]) {
				case X_CELL:
					sb.append("X"); break;
				case O_CELL:
					sb.append("o"); break;
				default:
					sb.append(" ");break;
				}
			}
			sb.append("\n");
		}
		sb.deleteCharAt(sb.length()-1);
		return sb.toString();
	}
}
