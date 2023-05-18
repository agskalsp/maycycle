/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.lynda.print;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 *
 * @author Producer
 */
public class PrintMadLib {
    public static void printmadlib(String filename) throws FileNotFoundException
    {
        File finished = new File(filename);
        Scanner in = new Scanner(finished);
        while(in.hasNext())
        {
            System.out.print(in.next()+" ");
        }
        
    }
    
}
