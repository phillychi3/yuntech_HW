package 物件導向;

abstract class Volume {
    double height;
    Volume(double h) {
        height = h;
    }
    public abstract double area();
    public double volume() {
        return area() * height;
    }
}

class Rectangle extends Volume {
    private double width, length;
    Rectangle (double w, double l, double h) {
        super(h);
        width = w;
        length = l;
    }
    public double area() {
        return width * length;
    }
}

class Circle extends Volume {
    private double radius;
    Circle (double r, double h) {
        super(h);
        radius = r;
    }
    public double area() {
        return radius * radius * 3.14;
    }
}

public class VolumeMain {
    public static void main (String args[]) {
        Rectangle r = new Rectangle(3.0, 4.0, 5.0);
        System.out.println("Area: " + r.area());
        System.out.println("Volume: " + r.volume());
        Circle c = new Circle(3.0, 5.0);
        System.out.println("Area: " + c.area());
        System.out.println("Volume: " + c.volume());
    }
}

/*** ======================================================================================
   
1. 此題的 Volume 是一個抽象類別（abstract），它有 volume() 方法計算體積，而 Rectangle 跟
   Circle 都要繼承 Volume，這樣可以統一使用父類的計算體積方法，而不用多寫重複的 code

***/
