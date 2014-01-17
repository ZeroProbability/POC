package com.klyserv.game.tictactoe;

public class TictactoeBoard {
	
	public static final Boolean X=true;
	public static final Boolean O=false;
	public static final Boolean NONE=null;

	private Boolean nextTurn=NONE;
	
	private final Boolean[][] board={ { NONE, NONE, NONE} , { NONE, NONE, NONE} ,{ NONE, NONE, NONE} };
	
	private final int BOARD_SIZE=board.length;
	
	public int getBoardSize() {
		return BOARD_SIZE;
	}
	
	public Boolean whoWon() {
		mainloop:for(int i=0;i<BOARD_SIZE;i++) {
			if(board[i][0]==NONE) continue;
			for(int j=1;j<BOARD_SIZE-1;j++) {
				if(board[i][0]==board[i][j]) continue;
				continue mainloop;
			}
			if(board[i][0]==board[i][BOARD_SIZE-1]) return board[i][0];
		}
		mainloop:for(int j=0;j<BOARD_SIZE;j++) {
			if(board[0][j]==NONE) continue;
			for(int i=1;i<BOARD_SIZE-1;i++) {
				if(board[0][j]==board[i][j]) continue;
				continue mainloop;
			}
			if(board[0][j]==board[BOARD_SIZE-1][j]) return board[0][j];
		}
		if(board[0][0]!=NONE && board[0][0]==board[1][1] && board[1][1]==board[2][2]) return board[0][0];
		if(board[0][2]!=NONE && board[0][2]==board[1][1] && board[1][1]==board[2][0]) return board[0][2];
		return NONE;
	}
	
	private void put(int x, int y, Boolean symbol) throws InvalidPlacementException, OutOfTurnException {
		if(nextTurn!=symbol&&nextTurn!=NONE) throw new OutOfTurnException();
		if(x<0||x>BOARD_SIZE-1) throw new InvalidPlacementException("X position "+x+" is invalid. It has to be between 0 and "+(BOARD_SIZE-1));
		if(y<0||y>BOARD_SIZE-1) throw new InvalidPlacementException("Y position "+y+" is invalid. It has to be between 0 and "+(BOARD_SIZE-1));
		if(board[x][y]!=NONE) throw new InvalidPlacementException("There is already something on cell "+x+","+y);
		board[x][y]=symbol;
		nextTurn=!symbol;
	}
	
	public void putX(int x, int y) throws InvalidPlacementException, OutOfTurnException {
		put(x,y,X);
	}
	
	public void putO(int x, int y) throws InvalidPlacementException, OutOfTurnException {
		put(x,y,O);
	}
	
}
