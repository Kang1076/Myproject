package java0720;

public class Breakexample1 {
    public static void main(String[] args) {
        for (int i = 1; i<=10; i++) {
            if (i == 6) break;

            // break 대신 컨티뉴를 하면 한번만 건너뜀
            System.out.print(i + " ");
        }
        System.out.println("반복문 종료!");
        System.out.println("---------------------");

        for (int i = 0; i<3; i++) {
                for (int j=0; j<2; j++) {
                        if(i == j) break;
                        System.out.println(i + "-" + j);
                }
                if (i == 1) break;
        }
        outer: for (char upper='A'; upper<='Z'; upper++) {
                for (char lower='a'; lower<='z'; lower++) {
                        System.out.println(upper + "-" + lower);
                        if(lower == 'f') break outer;
                }
        }
    }
}
