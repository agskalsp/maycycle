package com.lynda;

import com.lynda.createfile.CreateFile;
import com.lynda.print.PrintMadLib;
import com.lynda.madlib.MadLib;
import java.io.FileNotFoundException;

public class App {

        public static void main(String[] args) throws FileNotFoundException {
               
              
           CreateFile.getWords();
           MadLib.createMadLib("C:\\Users\\Producer\\Documents\\NetBeansProjects\\sample-multi-app\\app\\words.txt");
           PrintMadLib.printmadlib("C:\\Users\\Producer\\Documents\\NetBeansProjects\\sample-multi-app\\app\\finished.txt");   
        }

}