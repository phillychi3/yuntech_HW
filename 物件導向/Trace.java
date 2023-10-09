package 物件導向;

import java.util.Scanner;


public class Trace {
    public static void main(String[] args) {
        try (Scanner keyboard = new Scanner(System.in)) {
            System.out.println("Please enter one value:");
            int num = keyboard.nextInt();
            int m=1;
            int f = 1;

            while(m<=num){
                System.out.printf("n = %d m = %d f = %d\n", num, m, f); 
                f=f*m;
                m++;
               
            }
            System.out.printf("n = %d m = %d f = %d\n", num, m, f); 
            System.out.println(num+"!:"+f);
        }
    }
}
