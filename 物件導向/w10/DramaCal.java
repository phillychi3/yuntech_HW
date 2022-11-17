package 物件導向;

abstract class Drama {
    //宣告三個整數script, acting, direction;
    int script, acting, direction;
    
    //定義Drama的建構子，並傳入整數參數s, a, d
    Drama(int s, int a, int d){
        this.script = s;
        this.acting = a;
        this.direction = d;
    }
    //定義一個abstract method: score()
    abstract double score();
    
    //定義一個子類別們共有的方法 finalScore()，傳回 score() + 10
    double finalScore(){
        return score() + 10;
    }
}

class EngDrama extends Drama {
    //定義EngDrama的建構子，並傳入整數參數s, a, d
    EngDrama(int s, int a, int d) {
        super(s, a, d);
    }
    double score() {
        return script * 0.3 + acting * 0.3 + direction * 0.4;
    }
}

class ChiDrama extends Drama {
    //定義ChiDrama的建構子，並傳入整數參數s, a, d
    ChiDrama(int s, int a, int d) {
        super(s, a, d);
    }
    double score() {
        return script * 0.4 + acting * 0.4 + direction * 0.2;
    }
}

public class DramaCal {
    public static void main(String args[]) {
        EngDrama ed = new EngDrama(85, 85, 90);
        ChiDrama cd = new ChiDrama(90, 80, 90);
        System.out.println("EngDrama's orignal score: " + ed.score());
        System.out.println("EngDrama's final score: " + ed.finalScore());
        System.out.println("ChiDrama's orignal score: " + cd.score());
        System.out.println("ChiDrama's final score: " + cd.finalScore());
    }
}

