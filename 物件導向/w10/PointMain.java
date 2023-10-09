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
}

public class PointMain {
    public static void main(String args[]) {
        CPoint cp = new CPoint(3, 4);
        MPoint mp = new MPoint(3, 4);
        System.out.println("Distance to 0 for cp: " + cp.distanceTo0());
        System.out.println("Distance to 0 for mp: " + mp.distanceTo0());
    }
}