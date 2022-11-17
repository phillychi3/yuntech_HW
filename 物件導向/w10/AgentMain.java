
interface Agent {
    abstract int moveRight();
    abstract int moveLeft();
}


class Boy implements Agent {
    int x;
    Boy(int x){
        this.x = x;
    }
    public int moveRight(){
        return x+=2;
    }
    public int moveLeft(){
        return x-=2;
    }
}

class Girl implements Agent{
    int x;
    Girl(int x){
        this.x = x;
    }
    public int moveRight(){
        return x+=1;
    }
    public int moveLeft(){
        return x-=1;
    }
}


class AgentMain {
    public static void main(String args[]){
    Boy b1 = new Boy(100);
    //b1往右移，並印出position
    System.out.println(b1.moveRight());
    //b1往左移，並印出position
    System.out.println(b1.moveLeft());
    Girl g1 = new Girl(200);
    //g1往左移，並印出position
    System.out.println(g1.moveLeft());
    //g1往右移，並印出position
    System.out.println(g1.moveRight());
    }
}
