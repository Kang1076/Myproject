package SwitchStudy;
import java.util.Scanner;

public class SwitchEx2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("영문 대문자를 입력하세요. : ");
        char capitalLetter = sc.next().charAt(0);

        switch(capitalLetter) {
            case 'A' :
                System.out.println("훌륭합니다.");
                break;
            case 'B' :
                System.out.println("좋습니다.");
                break;
            case 'C' :
                System.out.println("보통입니다.");
                break;
            case 'D' :
                System.out.println("노력하세요.");
                break;
            default: System.out.println("잘못 입력하셨습니다.");
        }
    }
}
