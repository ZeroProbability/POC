package com.klyserv.poc.games;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JOptionPane;
import javax.swing.JPanel;

import com.klyserv.poc.games.TicTacToeBoard.InvalidLocationException;
import com.klyserv.poc.games.TicTacToeBoard.InvalidMoveException;
import com.klyserv.poc.games.TicTacToeEngine.TicTacToeMove;

public class TicTacToePanel extends JPanel implements MouseListener {
	
	private static final long serialVersionUID = 1L;
	
	private int padding=10;
	
	private TicTacToeBoard board;

	private boolean listening=true;
	
	private int unitBoxWidth(){
		return (getWidth() - (2 * padding)) / TicTacToeBoard.BOARD_SIZE;
	}
	
	private int unitBoxHeight() {
		return (getHeight() - (2 * padding))/ TicTacToeBoard.BOARD_SIZE;
	}
	
	private int boxStartX(int i) {
		return padding+i*unitBoxWidth();
	}
	
	private int boxStartY(int j) {
		return padding+j*unitBoxHeight();
	}

	public TicTacToePanel() {
		addMouseListener(this);
		board=new TicTacToeBoard();
	}
	
	@Override
	public void paint(Graphics g) {
		super.paint(g);

		g.setColor(Color.red);
		
		for(int i=0;i<TicTacToeBoard.BOARD_SIZE;i++) {
			for(int j=0;j<TicTacToeBoard.BOARD_SIZE;j++) {
				g.drawRect(boxStartX(i), boxStartY(j), unitBoxWidth(), unitBoxHeight());
				try {
					put(i, j, board.getAt(i, j));
				} catch (InvalidLocationException e) {
					// should not happen
				}
			}
		}
		
	}
	
	private void put(int i, int j, int type) {
		Graphics g=getGraphics();
		
		int boxX=boxStartX(i);
		int boxY=boxStartY(j);
		int boxX1=boxX+unitBoxWidth();
		int boxY1=boxY+unitBoxHeight();
		
		if(type==TicTacToeBoard.X_CELL) {
			g.drawLine(boxX+padding, boxY+padding, boxX1-padding*2, boxY1-padding);
			g.drawLine(boxX+padding, boxY1-padding, boxX1-padding*2, boxY+padding);
		} else if(type==TicTacToeBoard.O_CELL) {
			g.drawOval(boxX+padding,boxY+padding,boxX1-boxX-padding*2,boxY1-boxY-padding*2);
		}
	}
	
	private void stopListening() {
		listening=false;
	}
	
	private void startListening() {
		listening=true;
	}
	
	@Override
	public void mouseClicked(MouseEvent e) {
		if(!listening) return;
		int i=(e.getX()-padding)/unitBoxWidth();
		int j=(e.getY()-padding)/unitBoxHeight();
		if(i>=0 && i<TicTacToeBoard.BOARD_SIZE && j>=0 && j<TicTacToeBoard.BOARD_SIZE)
			try {
				try {
					if(board.getAt(i, j)!=TicTacToeBoard.EMPTY_CELL) return;
				} catch (InvalidLocationException e1) {
					// shouldn't happen
				}
				
				board=board.put(i, j, board.getNextPutType());
				put(i, j,board.getNextPutType());
				if(board.winPositionReached()) {
					JOptionPane.showMessageDialog(null, "You won!");
					stopListening();
					return;
				}
				stopListening();
				if(board.emptyCellCount()==0) {
					JOptionPane.showMessageDialog(null, "Its a draw. Try again.");
					return;
				}

				// Let engine do the move now 
				TicTacToeMove engineMove=new TicTacToeEngine().nextOneLevelMove(board);
				board=board.put(engineMove.getI(), engineMove.getJ(), board.getNextPutType());
				put(engineMove.getI(), engineMove.getJ(),board.getNextPutType());

				if(board.winPositionReached()) {
					JOptionPane.showMessageDialog(null, "I won! hahaha");
					stopListening();
					return;
				}
			} catch (InvalidMoveException e1) {
				JOptionPane.showMessageDialog(null, "Wrong move!");
			}
		startListening();
	}

	@Override
	public void mousePressed(MouseEvent e) {}

	@Override
	public void mouseReleased(MouseEvent e) {}

	@Override
	public void mouseEntered(MouseEvent e) {}

	@Override
	public void mouseExited(MouseEvent e) {	}

}
