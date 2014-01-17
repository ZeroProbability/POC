package com.klyserv.game.tictactoe;

import org.testng.Assert;
import org.testng.annotations.Test;

public class TictactoeBoardTest {
	
	@Test(expectedExceptions=InvalidPlacementException.class)
	public void testInvalidPlacement() throws InvalidPlacementException, OutOfTurnException {
		TictactoeBoard tboard=new TictactoeBoard();
		tboard.putX(1, 0);
		tboard.putO(1, 0);
	}

	@Test(expectedExceptions=OutOfTurnException.class)
	public void testOutOfTurn() throws InvalidPlacementException, OutOfTurnException {
		TictactoeBoard tboard=new TictactoeBoard();
		tboard.putX(1, 0);
		tboard.putX(2, 0);
	}

	@Test
	public void winTestX() throws InvalidPlacementException, OutOfTurnException {
		TictactoeBoard tboard=new TictactoeBoard();

		tboard.putX(1, 0);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.NONE);
		tboard.putO(2, 0);tboard.putX(1, 1);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.NONE);
		tboard.putO(0, 0);tboard.putX(1, 2);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.X);
	}

	@Test
	public void winTestY() throws InvalidPlacementException, OutOfTurnException {
		TictactoeBoard tboard=new TictactoeBoard();;

		tboard.putX(0, 0);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.NONE);
		tboard.putO(0, 1);tboard.putX(1, 0);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.NONE);
		tboard.putO(0, 2);tboard.putX(2, 0);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.X);
	}
	
	@Test
	public void winDiagnolly() throws InvalidPlacementException, OutOfTurnException {
		TictactoeBoard tboard=new TictactoeBoard();
		tboard.putO(0, 0); tboard.putX(1, 0); tboard.putO(1, 1); tboard.putX(2, 0); tboard.putO(2, 2);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.O);
		tboard=new TictactoeBoard();
		tboard.putO(2, 0); tboard.putX(1, 0); tboard.putO(1, 1); tboard.putX(2, 1); tboard.putO(0, 2);
		Assert.assertEquals(tboard.whoWon(), (Boolean)TictactoeBoard.O);
	}

}
