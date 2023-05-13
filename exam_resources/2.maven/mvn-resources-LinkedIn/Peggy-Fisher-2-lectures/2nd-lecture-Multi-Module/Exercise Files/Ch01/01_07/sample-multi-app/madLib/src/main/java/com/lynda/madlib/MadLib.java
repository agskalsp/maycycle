/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lynda.madlib;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author Producer
 */
public class MadLib {

    /**
     * @param args the command line arguments
     */
    public static void createMadLib(String fileName) throws FileNotFoundException{
        /*  This program reads a file containing a series of random words
        representing adjectives, verbs, names, nouns, etc. 
        In the madlib file, there is a numeric placeholder for each 
        word.  The program reads both files and creates a third file
        which contains the finished 'madlib' 
        If you want to update the word list, it should inlcude the following
        word types (total of 17 words): 
        relative, adj, adj, adj, name, adj, adj, verb (ed), body part, verb (ing)
        plural noun, noun, adverb, verb, verb, relative, name */
        
        File input = new File(fileName);
        File madlib = new File("C:\\Users\\Producer\\Documents\\NetBeansProjects\\sample-multi-app\\madLib\\src\\main\\java\\com\\lynda\\madlib\\madlib.txt");
        Scanner in = new Scanner(input);
        ArrayList<String> words = new ArrayList<String>();
        while(in.hasNext())
        {
            words.add(in.next());
        }
        File output = new File("finished.txt");
        PrintWriter out = new PrintWriter(output);
        in.close();
        in = new Scanner(madlib);
       
        while(in.hasNext())
        {
            if(in.hasNextInt())
            {
                int pos = in.nextInt();
                pos--;
                out.print(" "+words.get(pos)+" ");
            }
            else
                out.print(in.next() + " ");
        }
        out.close();
    }
    
}
