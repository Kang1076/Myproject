package java0720;

public class g_MethodQuiz {
        static int sum(int n) {
                int total = 0;
                System.out.print(n + "의 약수:");
                for (int i=1; i<=n; i++) {
                    if (n % i == 0) {
                            System.out.print(i + " ");
                            total += i;
                    }
                }
                System.out.println();
                return total;
        }
        public static void main(String[] args) {
                System.out.println("10의 약수의 총합: " + sum(10));
                System.out.println("=======================");
                System.out.println("30의 약수의 총합: " + sum(30));
    }
}
