package java0720;

import java.util.Scanner;

public class Breakexample2 {
    public static void main(String[] args) {
        /*
         # 무한루프
         - 무한 루프는 반복문의 반복 횟수를 개발자가 정확히 사전에 인지하지 못하는 상황에서 주로 사용됩니다.
         - 특정 조건 하에서 반복문을 강제 종료하는 형태로 구성됩니다.
         - 무한루프는 일반적으로 while문을 사용하며,
         while의 조건식 자리에 논리상수 true를 쓰면 무한루프가 구성됩니다.
         */
        int i = 0;
        while(true) {
                if (i == 150) break;
                System.out.println(i);
                i++;
        }
        Scanner sc = new Scanner(System.in);
        while(true) {
                System.out.println("숫자를 입력하세요.");
                System.out.println("그만 입력하시려면 0을 입력해주세요.");
                System.out.println(">");
                int num = sc.nextInt();

                if(num == 0);

                System.out.println("입력하신 숫자는: " + num);
                System.out.println("무한루프 종료!");
        }
    }
}
