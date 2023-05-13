package com.lynda.weather;

public class Weather {
    private String city;
    private String condition;
    private String temp;
    private String windSpeed;
    private String humidity;
    
    public Weather() {}

	public String getCity() { return city; }
	public void setCity(String city) { this.city = city; }
	
	public String getCondition() { return condition; }
	public void setCondition(String condition) { this.condition = condition; }

	public String getTemp() { return temp; }
	public void setTemp(String temp) {	this.temp = temp; }
        
	public String getWindSpeed() { return windSpeed; }
	public void setWindSpeed(String windSpeed) { this.windSpeed = windSpeed; }

	public String getHumidity() { return humidity; }
	public void setHumidity(String humidity) { this.humidity = humidity; }
}
