package SwitchStudy;

import java.util.Scanner;

public class SwitchEx1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("계절을 입력 하세요.");
        String season = sc.next();

        switch(season) {
            case "봄" :
            case "spring" :
            case "SPRING" :
                System.out.println("따뜻한 봄이 왔어요.");
                break;
            case "여름" :
            case "summer" :
            case "SUMMER" :
                System.out.println("무더운 여름이 왔어요.");
                break;
            case "가을" :
            case "fall" :
            case "FALL" :
                System.out.println("쓸쓸한 가을이 왔어요.");
                break;
            case "겨울" :
            case "winter" :
            case "WINTER" :
                System.out.println("추운 겨울이 왔어요.");
                break;
            default: System.out.println("계절을 잘못 입력하셨습니다.");
        }
    }
}
