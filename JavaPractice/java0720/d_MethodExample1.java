package java0720;

public class d_MethodExample1 {

        static int calcTotal(int x) {
                System.out.println("계산 기능을 수행합니다.");
                int total = 0;
                for (int i=1; i<x; i++) {
                        total += i;
                }
                return total;
        }
        public static void main(String[] args) {
                int result = calcTotal(10);
                System.out.println(result);

                System.out.println(calcTotal(50));
                System.out.println(calcTotal(100));
                System.out.println(calcTotal(20));
                System.out.println(calcTotal(30));
    }
}
