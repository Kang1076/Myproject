package java1207;

public class InheritanceTV {
    public static void main(String[] args) {
        ProductTV lgTV = new ProductTV("우리집 TV");
        lgTV.setPower(true);
        lgTV.setVolume(35);
        lgTV.setChannel(1000, true);
        lgTV.viewTV();
    }
}
