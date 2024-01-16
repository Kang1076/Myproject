package java0720;

import java.util.Arrays;
import java.util.Scanner;

public class arrayInsery {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String[] names = new String[10];

        for (int i=0; i<names.length; i++) {

            System.out.println("이름을 입력하세요: ");
            System.out.println("그만 입력하고 싶으면 '그만'이라고 쓰세요.");
            String name = sc.next();

            /*
             - 자바에서는 문자열 동등 비교시에 == 연산자를 사용하시면 안됩니다.
             - 비교문자열 1.equals(비교문자열2)를 사용하셔야 합니다.
             */

            if(names.equals("그만")) {
                    System.out.println("입력을 종료합니다.");
                    break;
            }

            names[i] = name;

            System.out.print("# 현재까지 입력된 이름:");
            System.out.println(Arrays.toString(names));

            for (String n : names) {
                    if(n == null) break; //null은 문자열 아님
                    System.out.print(n + " ");
            }
            System.out.println();
        }

    }
}
