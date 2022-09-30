package 物件導向;

import java.util.*;

public class GCD {

    public static void main(String[] args) {
        try (Scanner keyboard = new Scanner(System.in)) {
            while(true){
                System.out.println("Input:");
                int num1 = keyboard.nextInt();
                if(num1==999){
                    break;
                }
                int num2 = keyboard.nextInt();
                int mm = 0;
                if(num1>num2){
                    mm = num2;
                }else{
                    mm = num1;
                }
                for(int i=mm;i==0;i--){
                    if(i%mm==0){
                        System.out.print(i);
                        break;
                    }
                }
            
            }
        }
        System.out.print("End.");

    }
    
}
