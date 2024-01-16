package java0720;

public class f_MethodExample3 {
        static int add(int n1, int n2) {
                return n1 + n2;
        }
        static int[] operateTotal(int n1, int n2) {
                return new int[] {n1+n2, n1-n2, n1*n2, n1/n2};
        }
        static double[] calcArrayTotal(int[] nums) {
                int sum = 0;
                for (int n : nums) {
                        sum += n;
                }
                double avg = (double)sum / nums.length;
                return new double[] {sum, avg};
        }
        static void multi(int n1, int n2) {
                int result = n1 * n2;
                System.out.printf("%d x %d = %d\n", n1, n2, result);
        }
        static void divide(int n1, int n2) {
                if (n2 == 0) {
                        System.out.println("0으로 나누면 안돼요~!");
                        return;
                }
                int result = n1 / n2;
                System.out.printf("%d / %d = %d\n", n1, n2, result);
        }
        public static void main(String[] args) {
                        int r1 = add(3,8);
                        System.out.println(r1);

                        int r2 = add(add(4,6), add(8,7));

        int[] totalResult = operateTotal(20,5);
        System.out.println("20 + 5 = " + totalResult[0]);
        System.out.println("20 - 5 = " + totalResult[1]);
        System.out.println("20 * 5 = " + totalResult[2]);
        System.out.println("20 / 5 = " + totalResult[3]);

        System.out.println("----------------------------------");
        int[] numbers = {57, 89, 78, 91, 93, 47};
        double[] result = calcArrayTotal(numbers);
        System.out.printf("합계 %d점, 평균: %.2f점\n", (int)result[0], result[1]);
        multi(10,7);
        multi(add(3,1), add(6,3));
        divide(10,0);
    }
}
