package java1207;

public class PolyBuyer {
    public static void main(String[] args) {
        Buyer buyer = new Buyer();
        TV tv = new TV();
        Audio audio = new Audio();
        Computer computer = new Computer();
        buyer.buy(tv);
        buyer.buy(audio);
        buyer.buy(computer);
        buyer.viewInfo();
    }
}
