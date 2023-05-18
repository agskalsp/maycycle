package com.lynda.weather;

import java.net.URL;
import java.net.URLConnection;

import org.apache.log4j.Logger;
import org.dom4j.Document;
import org.dom4j.io.SAXReader;

public class WeatherRetriever {

	private static Logger log = Logger.getLogger(WeatherRetriever.class);

	public Document retrieve(String id) throws Exception {
           // public InputStream retrieve(String id) throws Exception {
		log.info( "Retrieving Weather Data" );
		String url = "http://api.openweathermap.org/data/2.5/forecast/city?id=5268583&mode=xml&units=Imperial&APPID=25b917908e8d5b115fae98ac4d6924e2";

		URLConnection conn = new URL(url).openConnection();
                SAXReader reader = new SAXReader();
                Document document = reader.read(url);
                return document;
    }
   

}
