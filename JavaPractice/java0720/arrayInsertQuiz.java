package java0720;

import java.util.Scanner;
public class arrayInsertQuiz {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String[] foods = new String[100];

        System.out.println("# 먹고 싶은 음식을 입력하세요.");
        System.out.println("# 입력을 중지하려면 <그만>이라고 입력하세요.");

        for (int i=0; i<foods.length; i++) {

            System.out.print(">");
            String food = sc.nextLine();

            if (food.equals("그만")) {
                    System.out.println("입력을 종료합니다.");
                    break;
            }

            foods[i] = food;
        }
            System.out.print("내가 먹고 싶은 음식들: [");

            for(String n : foods) {
                    if(n == null) break;
                    System.out.print(n + " ");
            }

                    System.out.println("]");
                    sc.close();
    }

}

