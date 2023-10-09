package 物件導向;


abstract class Payment {
    int money;
    Payment(int m){
    money=m;
    }
    abstract int pay(); 
}

class WithTax extends Payment {
    WithTax(int m) {
        super(m);
    }
    int pay() {
        return (int)(money*1.05);
    }
}

class ByCredit extends Payment {
    ByCredit(int m) {
        super(m);
    }
    int pay() {
        return (int)(money*1.02);
    }
}

class PaymentArray {
    public static void main(String args[]) {
        Payment pa[] = {new WithTax(100), new ByCredit(100), new WithTax(80), new ByCredit(80)};
        int sum = 0;
        for (int counter = 0; counter < pa.length; ++counter) {
            sum += pa[counter].pay();
        }

        System.out.print("The average pay of " + pa.length);
        System.out.println(" payment is " + sum / pa.length);
    }
}


/*** ======================================================================================
   
1. 參照第九題 PaymentMain，宣告一個 Payment 型態的陣列，可以儲存各種 WithTax 跟 ByCredit 物件

2. 使用 for() 迴圈呼叫 pa[] 陣列裡面所有的物件的 pay() 方法

    for (int counter = 0; counter < pa.length; ++counter) {
        ...
    }


***/