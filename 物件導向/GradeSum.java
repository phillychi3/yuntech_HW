package 物件導向;
import java.util.*;

public class GradeSum {
    static Scanner input = new Scanner(System.in);
    public static void main(String args[]) {
        int num=0;
        int all=0;
        int ct = 0;
        while(num!=-1){
            System.out.println("Please enter score or enter -1 to stop:");
            num = input.nextInt();
            if(num!=-1){
                all=all+num;
                ct++;
            }
        }
        System.out.println("Total:"+all);
        //The average of 5 score is:82.40
        System.out.printf("The average of %d score is:%.2f",ct,(float)all/ct);
    }
    
}
