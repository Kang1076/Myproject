package java1207;
import java.util.Calendar;
import java.util.Scanner;

public class AirCon {
    // 1. 기능 설계에 필요한 인스턴스 필드 선언
    private boolean isPower; // 전원
    private int setTemp; // 온도 설정
    private int currTemp; // 현재 온도
    private boolean isCooler; // 냉방기 전원
    private boolean isHeater; // 난방기 전원
    private int windStep; // 1단, 2단, 3단
    private String onOffStr;

    // 2. 기본 생성자 생성 - 초기값 세팅
    public AirCon() {
        final int[] monthTemp = {-5, 3, 8, 14, 22, 27, 31, 30, 22, 18, 7, 2};
        Calendar now = Calendar.getInstance();
        int month = now.get(Calendar.MONTH); // 현재 달을 가져옴
        currTemp = monthTemp[month];
        isPower = false;
        setTemp = 20;
        isCooler = false;
        isHeater = false;
        windStep = 1;
    }
    // 3. 메소드 생성
    // 에어컨의 온도가 변경 될 때 화면 출력
    public void airConInfo() {
        String OnOffStr = (isPower) ? "ON" : "OFF";
        String coolerStr = (isCooler) ? "ON" : "OFF";
        String heaterStr = (isHeater) ? "ON" : "OFF";
        final String[] windStr = {"", "1단계", "2단계", "3단계"};
        System.out.println("====== 에어컨 정보 ======");
        System.out.println("전원 : " + onOffStr);
        System.out.println("현재 온도 : " + currTemp);
        System.out.println("설정 온도 : " + setTemp);
        System.out.println("히터 : " + heaterStr);
        System.out.println("쿨러 : " + coolerStr);
        System.out.println("바람 세기 : " + windStr[windStep]);
    }
    // 에어컨에 대해 온도와 바람세기 설정 및 조건에 따라 히터 또는 쿨러 가동
    public void setAirConState() {
        Scanner sc = new Scanner(System.in);
        System.out.println("현재 온도는 " + currTemp + " 입니다.");
        System.out.println("온도를 설정 하세요. : ");
        setTemp = sc.nextInt();
        System.out.println("설정 온도는 " + setTemp + " 입니다.");
        System.out.println("바람 세기를 설정 하세요.[1단]/[2단]/[3단] : ");
        windStep = sc.nextInt();
        if (currTemp > setTemp) { // 현재 더운 상태
            System.out.println("쿨러가 동작 합니다.");
            isCooler = true;
            isHeater = false;
        } else if (currTemp < setTemp) { // 현재 추운 상태
            System.out.println("히터가 동작 합니다.");
            isHeater = true;
            isCooler = false;
        } else {
            isCooler = false;
            isHeater = false;
        }
    }
    public void setPower(boolean power) {
        isPower = power;
    }
    public int getWindStep() {
        return windStep;
    }
    public boolean isHeater() {
        return isHeater;
    }
    public boolean isCooler() {
        return isCooler;
    }
    public void setCurrTemp(int n) {
        currTemp += n;
    }
    public int getCurrTemp() {
        return currTemp;
    }
    public int getSetTemp() {
        return setTemp;
    }
}
