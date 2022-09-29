package 物件導向;
import java.util.Scanner;


public class Fac {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Please enter one value:");
        int num = keyboard.nextInt();
        int m=1;
        int f = 1;
        while(m<=num){
            f=f*m;
            m++;
        }
        System.out.println(num+"!:"+f);
    }
}
