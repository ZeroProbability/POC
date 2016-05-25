package com.klyserv.poc.games;

import java.awt.Graphics;

import javax.swing.JFrame;

public class DrawBox extends JFrame {

	private static final long serialVersionUID = 1L;
	private TicTacToePanel ticTacToeBoard;
	
	public DrawBox() {
		super("Tic-Tac-Toe...");
		setVisible(true);
		setSize(600, 400);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		ticTacToeBoard=new TicTacToePanel();
		add(ticTacToeBoard);
	}

	public static void main(String[] args) {
		new DrawBox();
	}

	@Override
	public void paint(Graphics g) {
		super.paint(g);
	}

}
