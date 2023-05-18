package com.lynda;

import com.lynda.createfile.CreateFile;
import com.lynda.madlib.MadLib;
import java.io.FileNotFoundException;

public class App {

        public static void main(String[] args) throws FileNotFoundException {
               
              
           CreateFile.getWords();
           //make sure you update the absolute file location with your project information
           MadLib.createMadLib("C:\\Users\\Producer\\Documents\\NetBeansProjects\\sample-multi-app\\app\\words.txt");
          
        }

}