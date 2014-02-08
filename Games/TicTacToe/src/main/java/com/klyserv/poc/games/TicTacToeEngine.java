package com.klyserv.poc.games;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import com.klyserv.poc.games.TicTacToeBoard.InvalidLocationException;
import com.klyserv.poc.games.TicTacToeBoard.InvalidMoveException;

public class TicTacToeEngine {
	
	public static class TicTacToeMove {
		private int i;
		public int getI() {
			return i;
		}

		public int getJ() {
			return j;
		}

		public int getType() {
			return type;
		}

		private int j;
		private int type;

		public TicTacToeMove(int i, int j, int type) {
			this.i=i;
			this.j=j;
			this.type=type;
		}

		@Override
		public String toString() {
			return "TicTacToeMove [i=" + i + ", j=" + j + ", type=" + type
					+ "]";
		}
		
	}
	
	private List<TicTacToeMove> nextSequentialMoves(TicTacToeBoard board) {
		List<TicTacToeMove> retList=new ArrayList<>();
		if(board.winPositionReached()) return null;
		for(int i=0;i<TicTacToeBoard.BOARD_SIZE;i++) {
			for(int j=0;j<TicTacToeBoard.BOARD_SIZE;j++) {
				try {
					if(board.getAt(i, j)==TicTacToeBoard.EMPTY_CELL) 
						retList.add(new TicTacToeMove(i, j, board.getNextPutType()));
				} catch (InvalidLocationException e) {
					throw new RuntimeException(e);
				}
			}
		}
		return retList;
	}
	
	public TicTacToeMove nextRandomMove(TicTacToeBoard board) {
		if(board.winPositionReached()) throw new RuntimeException("win position already reached!!");
		List<TicTacToeMove> possible=nextSequentialMoves(board);
		return possible.get((new Random()).nextInt(possible.size()));
	}

	public TicTacToeMove nextOneLevelMove(TicTacToeBoard board) {
		if(board.winPositionReached()) throw new RuntimeException("win position already reached!!");
		List<TicTacToeMove> possibleMoves=nextSequentialMoves(board);
		
		for(TicTacToeMove myMove:possibleMoves) {
			TicTacToeBoard boardAfterMyMove=null;
			try {
				boardAfterMyMove=board.put(myMove.i, myMove.j, myMove.type);
			} catch (InvalidMoveException e) {
				throw new RuntimeException("Internal error -", e);
			}
			if(boardAfterMyMove.winPositionReached()) return myMove;
		}
		
		return nextRandomMove(board);
	}
	
	public void nextSmartMove(TicTacToeBoard board) {
		// TODO: make this work!!
		System.out.println("---");
		System.out.println(board);
		if(board.winPositionReached()) throw new RuntimeException("win position already reached!!");
		List<TicTacToeMove> possibleMoves=nextSequentialMoves(board);
		
		for(TicTacToeMove thisMove:possibleMoves) {
			TicTacToeBoard boardAfterThisMove=null;
			try {
				boardAfterThisMove=board.put(thisMove.i, thisMove.j, thisMove.type);
			} catch (InvalidMoveException e) {
				throw new RuntimeException("Internal error -", e);
			}
			if(boardAfterThisMove.winPositionReached()) { 
				System.out.println("      < Win");
				return; 
			}; // Sure win
		}

		for(TicTacToeMove thisMove:possibleMoves) {
			TicTacToeBoard boardAfterThisMove=null;
			try {
				boardAfterThisMove=board.put(thisMove.i, thisMove.j, thisMove.type);
			} catch (InvalidMoveException e) {
				throw new RuntimeException("Internal error -", e);
			}
			nextSmartMove(boardAfterThisMove);
		}
		
	}
	
	public static void main(String[] args) throws InvalidMoveException {
		TicTacToeBoard board=new TicTacToeBoard();
		TicTacToeEngine engine=new TicTacToeEngine();
		engine.nextSmartMove(board);
	}
}
