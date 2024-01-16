package java0720;

public class e_MethodExample2 {
        static int calcRangeTotal(int x, int y) {
                int total = 0;
                for (int i=x; i<=y; i++) {
                        total += i;
                }
                return total;
        }
        static String selectRandomFood() {
                double rn = Math.random();
                if(rn > 0.66) {
                        return "치킨";
                } else if(rn > 0.33) {
                        return "족발";
                } else {
                        return "삼겹살";
                }
        }
        static int calcNumberTotal(int[] nums) {
                int total = 0;
                for (int n : nums) {
                        total += n;
                }
                return total;
        }

        public static void main(String[] args) {
                int result = calcRangeTotal(4, 7);
                System.out.println(result);

                System.out.println("오늘 점심 뭐먹지? -> " + selectRandomFood());

                int[] arr = {10,20,30,40,50};

                int sum = calcNumberTotal(arr);
                System.out.println("sum의 값: " + sum);

                sum = calcNumberTotal(new int[] {1,3,5,7});
                System.out.println("sum의 값: " + sum);
    }
}
