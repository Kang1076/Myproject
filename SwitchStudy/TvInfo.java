package SwitchStudy;

import java.util.Scanner;

public class TvInfo {
    private boolean isON;
    private int channel;
    private int volume;

    TvInfo() {
        isON = false;
        channel = 7;
        volume = 15;
    }
    TvInfo(boolean isON, int channel, int volume) {
        this.isON = isON;
        this.channel = channel;
        this.volume = volume;
    }

    // 외부에서 전원 on/off를 할 수 있는 기능 제공
    public void setON(boolean isON) {
        this.isON = isON;
        String onOffStr = (isON) ? "ON" : "OFF";
        System.out.println("TV가 " + onOffStr + " 되었습니다.");
    }
    // 외부에서 채널을 변경할 수 있는 기능 제공
    public void setChannel() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print("채널을 입력하세요. : ");
            channel = sc.nextInt();
            if (channel >= 0 && channel <= 999) break;
            else System.out.println("채널의 범위를 벗어났습니다.(0 ~ 999)");
        } System.out.println("채널이 " + channel + "(으)로 변경되었습니다.");
    }
    // 외부에서 볼륨을 변경할 수 있는 기능 제공
    public void setVolume() {
        Scanner sc = new Scanner(System.in);
        while(true) {
            System.out.print("볼륨을 조정해주세요. : ");
            volume = sc.nextInt();
            if (volume >= 0 && volume <= 100) break;
            else System.out.println("볼륨의 범위를 벗어났습니다.");
        }
        System.out.println("볼륨이 " + volume + "(으)로 변경되었습니다.");
    }
    // tv정보 출력 메소드
    public void getTV() {
        String onOffStr = (isON) ? "ON" : "OFF";
        System.out.println("===== TV 정보 =====");
        System.out.println("전원 : " + onOffStr);
        System.out.println("채널 : " + channel);
        System.out.println("볼륨 : " + volume);
        System.out.println("===================");
    }
}
