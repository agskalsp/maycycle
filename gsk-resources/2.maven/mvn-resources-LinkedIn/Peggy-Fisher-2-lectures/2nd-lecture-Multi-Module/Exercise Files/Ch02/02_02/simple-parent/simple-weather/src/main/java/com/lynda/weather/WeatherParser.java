package com.lynda.weather;

import java.util.List;
import org.apache.log4j.Logger;
import org.dom4j.Document;
import org.dom4j.Node;


public class WeatherParser {

	private static Logger log = Logger.getLogger(WeatherParser.class);

	public Weather parse(Document doc) throws Exception {
		Weather weather = new Weather();
                try{

		log.info( "Creating XML Reader" );
    		log.info( "Parsing XML Response" );
              
                List<Node> nodes = doc.selectNodes("/weatherdata/location" );
                Node node = nodes.get(0);
                weather.setCity(node.selectSingleNode("name").getText());
                List<Node> forecastNodes = doc.selectNodes("/weatherdata/forecast/time");
                weather.setCondition(forecastNodes.get(0).selectSingleNode("symbol").valueOf("@name").toString());
                weather.setTemp(forecastNodes.get(0).selectSingleNode("temperature").valueOf("@value"));
                weather.setWindSpeed(forecastNodes.get(0).selectSingleNode("windSpeed").valueOf("@mps").toString());
                weather.setHumidity(forecastNodes.get(0).selectSingleNode("humidity").valueOf("@value").toString());

                } 
                catch(Exception e)
                {
                    e.printStackTrace();
                }
                return weather; 
	}

 
}
