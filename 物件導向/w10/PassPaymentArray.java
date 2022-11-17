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



class PassPaymentArray {
    public static void main(String args[]) {
        Payment pa[] = newPaymentAry();
        int sum = calSum(pa);
        System.out.print("The average pay of " + pa.length);
        System.out.println(" payment is " + sum / pa.length);
    }
    static Payment[] newPaymentAry () {
        Payment pa[] = {new WithTax(100), new ByCredit(100), new WithTax(80), new ByCredit(80)};
        return pa;
    }
    static int calSum(Payment pa[]) {
        int sum = 0;
        for (int counter = 0; counter < pa.length; ++counter) {
            sum += pa[counter].pay();
        }
        return sum;
    }
}


    


    
