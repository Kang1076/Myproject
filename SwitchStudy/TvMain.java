package SwitchStudy;

public class TvMain {
    public static void main(String[] args) {
        TvInfo samsung = new TvInfo();

        samsung.setON(true);
        samsung.getTV();
        samsung.setChannel();
        samsung.setVolume();
        samsung.getTV();
    }
}
