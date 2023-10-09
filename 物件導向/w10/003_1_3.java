public class 003_1_3 {
    public static void main(String args[]) {
        Animal dog = new Dog("John");
        Animal bird = new Bird("Mary");
        System.out.println("小狗 " + dog.getName() + " 的移動方式是:" + dog.move());
        System.out.println("小鳥 " + bird.getName() + " 的移動方式是:" + bird.move());
    }
}
abstract class Animal {
    String name;
    Animal(String name) {
        this.name = name;
    }
    abstract String move();
    String getName(){
        return this.name;
    }
}

class Dog extends Animal{
    Dog(String name) {
        super(name);
    }

    public String move(){
        return "跑";
    }
        
}

class Bird extends Animal{
    Bird(String name) {
        super(name);
    }
    

    public String move(){
        return "飛";
    }
        
}

/*** ======================================================================================
   
1. move() 是一個抽象方法，Dog 跟 Bird 這兩個子類別都要實作此方法，實作
   方式不一樣，Dog 移動的方式是用跑的，Bird 移動的方式是用飛的
   
2. 第 3 行跟第 4 行在建立實例時有傳入名字進去，所以在設計這兩個 class 時，要記得建一個
   有傳入參數的建構子（Constructor）

***/