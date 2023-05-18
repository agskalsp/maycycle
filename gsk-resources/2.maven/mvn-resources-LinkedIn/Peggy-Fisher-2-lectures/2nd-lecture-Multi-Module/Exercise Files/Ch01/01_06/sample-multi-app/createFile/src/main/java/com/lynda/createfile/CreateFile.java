/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lynda.createfile;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 *
 * @author Producer
 */
public class CreateFile {

    /**
     * @param args the command line arguments
     */
    public static PrintWriter getWords( ) throws FileNotFoundException{
      
        String[] wordTypes = {"relative", "place", "food", "food", "number", "plural food", 
            "food", "verb ending in 'ing'", "person", "proper name", 
            "adjective", "noun", "plural food", "place", "animal", "place", "plural food"};
        
        File words = new File("words.txt");
        PrintWriter out = new PrintWriter(words);
        Scanner in = new Scanner(System.in);
        String word;
        for (int i = 0; i<wordTypes.length; i++)
        {
            System.out.println("Please enter a "+wordTypes[i]);
            word = in.nextLine();
            out.println(word);
          
        }
            
        in.close();
        out.close();
        return out;
    }
    
}
