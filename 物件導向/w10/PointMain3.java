package 物件導向;
abstract class Point {
    int x, y;
    Point(int a,int b){
        this.x = a;
        this.y = b;
    }
    abstract double distanceTo0();
    boolean closerTo0(Point point){
        return this.distanceTo0() < point.distanceTo0();
    }
    
    

    
}

class CPoint extends Point {
    CPoint(int a, int b) {
        super(a, b);
    }
    public double distanceTo0(){
        return Math.sqrt((x * x + y * y));

    }
    // public boolean closerTo0(CPoint point){
    //     return this.distanceTo0() < point.distanceTo0();
    // }
}

class MPoint extends Point {
    MPoint(int a, int b) {
        super(a, b);
    }
    public double distanceTo0(){
        return (x+y);
    }
    // public boolean closerTo0(MPoint point){
    //     return this.distanceTo0() < point.distanceTo0();
    // }
}

public class PointMain3 {
    public static void main(String args[]) {
        CPoint cp = new CPoint(3, 4);
        CPoint cp2 = new CPoint(12, 5);
        MPoint mp = new MPoint(3, 4);
        MPoint mp2 = new MPoint(1, 5);
        System.out.println("Is cp closer than cp2? " + cp.closerTo0(cp2));
        System.out.println("Is mp closer than mp2? " + mp.closerTo0(mp2));
        System.out.println("Is cp closer than mp? " + cp.closerTo0(mp));
        System.out.println("Is cp2 closer than mp2? " + cp2.closerTo0(mp2));
    }
}