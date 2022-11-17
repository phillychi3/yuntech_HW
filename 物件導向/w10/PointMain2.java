package 物件導向;

class Point {}

class CPoint extends Point {
    private int x, y;
    CPoint(int a,int b){
        this.x = a;
        this.y = b;
    }
    public double distanceTo0(){
        return Math.sqrt((x * x + y * y));
    }
    public boolean closerTo0(CPoint point){
        return this.distanceTo0() < point.distanceTo0();
    }
}

class MPoint extends Point {
    private int x, y;
    MPoint(int a,int b){
        this.x = a;
        this.y = b;
    }
    public double distanceTo0(){
        return (x+y);
    }
    public boolean closerTo0(MPoint point){
        return this.distanceTo0() < point.distanceTo0();
    }
}

public class PointMain2 {
    public static void main(String args[]) {
        CPoint cp = new CPoint(3, 4);
        CPoint cp2 = new CPoint(12, 5);
        MPoint mp = new MPoint(3, 4);
        MPoint mp2 = new MPoint(1, 5);
        System.out.println("Is cp closer? " + cp.closerTo0(cp2));
        System.out.println("Is mp closer? " + mp.closerTo0(mp2));
    }
}