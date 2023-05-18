package com.lynda.weather;

import org.apache.log4j.PropertyConfigurator;
import org.dom4j.Document;


public class Main {

	public static void main(String[] args) throws Exception {
		// Configure Log4J
		PropertyConfigurator.configure(Main.class.getClassLoader().getResource("log4j.properties"));

		// Read the City Id from the command prompt
		String cityId = "5268583";  
        try {
		  cityId = args[0];
        } catch( Exception e ) {}

		// Start the program
		new Main(cityId).start();
	}

	private String id;

	public Main(String id) {
		this.id = id;
	}
	
	public void start() throws Exception {
		// Retrieve Data
		Document dataIn = new WeatherRetriever().retrieve( id );
                // Parse Data
		Weather weather = new WeatherParser().parse( dataIn );

		// Format (Print) Data
		System.out.print( new WeatherFormatter().format( weather ) );
	}

}
