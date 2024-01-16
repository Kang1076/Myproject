package java0720;

import java.util.Scanner;
public class forquiz {
    public static void main(String[] args) {

        int dan = (int) ((Math.random() * 8) + 2);

        System.out.println("구구단" + dan + "단");
        System.out.println("--------------------------");

        for (int hang=1; hang<=9; hang++) {
                System.out.printf("%d x %d = $d/n", dan, hang, dan * hang);
        }
    }
}
