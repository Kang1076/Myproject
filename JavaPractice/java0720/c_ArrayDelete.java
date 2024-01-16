package java0720;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;
public class c_ArrayDelete {
    public static void main(String[] args) {
        String[] pokemon = {"피카츄", "라이츄", "파이리", "꼬부기", "버터풀"};

        Scanner sc = new Scanner(System.in);
        System.out.println("삭제전 정보: " + Arrays.toString(pokemon));

        System.out.println("삭제하고자 이름을 적어주세요");
        System.out.print(">");
        String delname = sc.next();

        int n;
        for (n=0; n<pokemon.length; n++) {
                if (delname.equals(pokemon[n])) {
                        System.out.println(pokemon[n] + "를 삭제합니다.");

                        for(int i=n; i<pokemon.length-1; i++) {
                            pokemon[i] = pokemon[i+1];
                        }
                        break;
                }
        }
        if (n !=pokemon.length) {
                String[] temp = new String[pokemon.length-1];
                for (int k=0; k<temp.length; k++) {
                        temp[k] = pokemon[k];
                }
                pokemon = temp;
                temp = null;
            System.out.println("*삭제 후 정보: " + Arrays.toString(pokemon));
        } else {
                System.out.println("해당 별명은 존재하지 않습니다.");
        }
    }
}
