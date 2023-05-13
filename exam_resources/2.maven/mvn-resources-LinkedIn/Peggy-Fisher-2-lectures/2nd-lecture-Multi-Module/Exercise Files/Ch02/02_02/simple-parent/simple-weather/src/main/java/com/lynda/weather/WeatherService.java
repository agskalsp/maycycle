package com.lynda.weather;

import org.dom4j.Document;

public class WeatherService {

    public WeatherService() {}

    public String retrieveForecast( String cityId ) throws Exception {
	// Retrieve Data
	Document dataIn = new WeatherRetriever().retrieve( cityId );
        
	// Parse Data
	Weather weather = new WeatherParser().parse( dataIn );
	
	// Format (Print) Data
	return new WeatherFormatter().format( weather );
    }	
}
