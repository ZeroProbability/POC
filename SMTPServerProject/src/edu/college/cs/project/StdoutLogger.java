package edu.college.cs.project;

import java.util.Date;

public class StdoutLogger extends Logger {
	
	@Override
	public void log(int errorlevel, String message) {
		String timestamp=new Date().toString();
		System.out.println(constructMessage(errorlevel, timestamp+"> "+message));
	}
}
