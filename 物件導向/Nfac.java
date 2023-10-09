package 物件導向;
import java.util.Scanner;
public class Nfac {
    static Scanner keyboard = new Scanner(System.in);
    public static void main(String[] args) {
        test();
        test();
        test();
    }
    
    public static void test() {
        System.out.println("Please enter one value:");
        int num = keyboard.nextInt();
        if(num >10 || num <= 0){
            System.out.println("Error, the value is out of range.");
            return;
        }
        int m=1;
        int f = 1;
        while(m<=num){
            f=f*m;
            m++;
        }
        System.out.println(num+"!:"+f);
    }
}