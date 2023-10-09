package 物件導向;


interface Payment{
    abstract int pay(int money);
}

class WithTax implements Payment{
    public int pay(int money){
        return (int)(money*1.05);
    }

}

class ByCredit implements Payment {
    public int pay(int money){
        return (int)(money*1.02);
    }
}
class PaymentInterMain {
    public static void main(String args[]) {
        Payment wt = new WithTax();
        System.out.println(((WithTax)wt).pay(100));
        Payment bc = new ByCredit();
        System.out.println(((ByCredit)bc).pay(100));
    }
}