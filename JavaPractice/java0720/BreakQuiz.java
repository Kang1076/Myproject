package java0720;

import java.util.Scanner;
public class BreakQuiz {
        public static void main(String[] args) {

                Scanner sc = new Scanner(System.in);

                System.out.println("덧셈 연산 문제입니다.");
                System.out.println("그만 하시려면 0을 입력해 주세요.");
                int cCount = 0;
                int aCount = 0;

                while (true) {
                        int rn1 = (int) ((Math.random()*100) + 1);
                        int rn2 = (int) ((Math.random()*100) + 1);

                        int num = (int) (Math.random()*2);
                        int correct;  // 문제에 따라 정답을 저장할 변수를 if 밖에 선언.
                                        if (num == 0) {
                                                System.out.printf("%d + %d = ???/n"
                                                                , rn1, rn2);
                                                System.out.print(">");
                                        } else {
                                                System.out.printf("%d + %d = ???/n"
                                                                , rn1, rn2);
                                                System.out.print(">");
                                                correct = rn1 + rn2;
                                        }
                                        int answer = sc.nextInt();

                        System.out.printf("%d + %d = ???/n", rn1, rn2);
                        System.out.print(">");
                        answer = sc.nextInt();
                        correct = rn1 + rn2;

                        if(answer == 0) {
                                System.out.println("입력종료");
                                break;
                        } else if (answer == correct) {
                                System.out.println("정답입니다!");
                                cCount++;
                        } else {
                                System.out.println("오답입니다!");
                                aCount++;
                        }
                }

                        System.out.println("================");
                        System.out.println("정답횟수: " + cCount + "회");
                        System.out.println("오답횟수: " + aCount + "회");
                        sc.close();
        }
}
