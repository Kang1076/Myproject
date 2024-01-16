package java0720;

import java.util.Arrays;
import java.util.Scanner;

public class a_test {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String[] pokemon = {"피카츄", "라이츄", "파이리", "꼬부기", "버터풀"};
        System.out.println("* 변경 전 정보: " + Arrays.toString(pokemon));
        System.out.println("수정할 맴버의 이름을 입력하세요");
        System.out.println(">");
        String name = sc.next();

        int idx;
        for (idx=0; idx<pokemon.length; idx++) {
                if (name.equals(pokemon[idx])) {
                        System.out.println(pokemon[idx] + "의 별명을");
                        System.out.print(">");

                        pokemon[idx] = sc.next();

                        System.out.println("변경 완료!");
                        System.out.println("* 변경 후 정보: " + Arrays.toString(pokemon));
                }
                if (idx == pokemon.length) {
                        System.out.println("해당 이름은 존재하지 않습니다.");
                }
        }
        sc.close();
    }
}
