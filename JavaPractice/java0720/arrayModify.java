package java0720;

import java.util.Arrays;
import java.util.Scanner;
public class arrayModify {
    public static void main(String[] args) {
            String[] foods = {"치킨", "보쌈", "삼겹살", "피자"};
            System.out.println(Arrays.toString(foods));

            foods[1] = "짜장면";
            foods[0] = "핫도그";
            System.out.println(Arrays.toString(foods));

            // 배열의 인덱스 번호 탐색.
            Scanner sc = new Scanner(System.in);
            System.out.println("탐색할 음식명을 입력하세요: ");
            String food = sc.next();
            int idx;

            for (idx=0; idx<foods.length; idx++) {
                    if (food.equals(foods[idx])) {
                            System.out.println("탐색완료");
                            System.out.println("인덱스 번호: " + idx);
                            break;
                    }
            }
            if (idx == foods.length) {
                    System.out.println("입력한 음식을 찾을 수 없습니다.");
            }
    }
}
