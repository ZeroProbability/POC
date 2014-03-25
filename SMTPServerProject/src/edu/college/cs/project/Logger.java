package edu.college.cs.project;

public abstract class Logger {
	
	public static final int INFO=0;
	public static final int WARN=1;
	public static final int ERROR=2;
	
	public void log(String message) {
		log(INFO, message);
	}

	public abstract void log(int errorlevel, String message);
	
	protected String constructMessage(int errorlevel, String message) {
		StringBuffer sb=new StringBuffer();
		switch(errorlevel) {
			case INFO:  sb.append("INFO  "); break;
			case ERROR: sb.append("ERROR "); break;
			case WARN:  sb.append("WARN  "); break;
	        default:    sb.append("INFO  "); break;
		}
		sb.append(message);
		return sb.toString();
	}

}
