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
    
  
  
  
  
    class PaymentMain {
        public static void main(String args[]) {
            WithTax wt = new WithTax(100);
            System.out.println(wt.pay());
            ByCredit bc = new ByCredit(100);
            System.out.println(bc.pay());
        }
    }
  
  /*** ======================================================================================
     
  1. 依據旁邊題目提示，先撰寫 Payment 的子類，WithTax 跟 ByCredit
  
      class WithTax extends Payment {
          ....
          ....
      }
      
  2. 再看到 main() 裡面在建這兩個物件時，有傳入數字當參數，所以要為這兩個 class 寫有參數的
     建構子（Constructor）
     
     class WithTax extends Payment {
          WithTax(int m) {
              ...
          }
          ...
      }
      
  3. 在這兩個 class 實作父類的抽象方法（abstract method） - pay()
     
  ***/