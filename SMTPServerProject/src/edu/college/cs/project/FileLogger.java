package edu.college.cs.project;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class FileLogger extends Logger {
	
	public static PrintWriter pfw=null; 
	private final static StdoutLogger console=new StdoutLogger();
	
	public FileLogger(String fileName) {
		try {
			pfw=new PrintWriter(new BufferedWriter(new FileWriter(fileName, true)));
		} catch (IOException e) {
			console.log(Logger.ERROR, "Error creating message log file. Exception:"+e.getMessage());
			pfw=null;
		}
	}

	@Override
	public void log(int errorlevel, String message) {
		if(pfw==null) return;
		pfw.println(super.constructMessage(errorlevel, message));
		pfw.flush();
	}

}
