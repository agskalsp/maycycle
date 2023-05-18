package com.lynda;


public class App {
	public static void main(String[] args){
		
		System.out.println(sum(10,5));
		System.out.println(subtraction(10,5));
		System.out.println(division(10,5));
		System.out.println(multiplication(10,5));

	}
	public static int sum(int a, int b)
	{
		return a + b;
	}
	public static int subtraction(int a, int b)
	{
		return a - b;
	}
	public static int division(int a, int b)
	{
		return a / b;
	}
	public static int multiplication(int a, int b)
	{
		return a * b;
	}
	
}
