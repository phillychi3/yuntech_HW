package 物件導向;

import java.util.*;

class Count {
    static Scanner input = new Scanner(System.in);
	public static void main(String args[]) {
        System.out.println("Input:");
        int num = input.nextInt();
        int all=0;
        for(int i = 1; i <= num; i++) {
            if(i%3 ==0 || i%2 == 0 && i%7 != 0) {
                all=all+i;
            }
        }
	}
}

/*** ===========================================================================================
   
1. 「找出哪些是 3 的倍數或是 5 的倍數，而不是 7 的倍數，並計算其和」，當該值為 7 的倍數時，應該
    略過此次迴圈，直接進入下一個次迴圈，判斷下一個數字


***/