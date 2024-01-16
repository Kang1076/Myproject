package java1206;

public class MethodOverloading {
    public static void main(String[] args) {
        System.out.println(sum(3,4));
        System.out.println(sum(100,85,350));
        System.out.println(sum(3,4,1,2));
        System.out.println(sum("인천","서울","부산"));
        System.out.println(sum(3,"강남",10));
    }

    static int sum(int x, int y) {
        return x + y;
    }

    static int sum(int x, int y, int z) {
        return x + y + z;
    }

    // 매개변수의 개수가 달라서 오버로딩 가능..
    static double sum(int x, int y, int z, int a) {
        return(double)x + y + z + a;
    }

    // 매개변수의 타입이 달라서 오버로딩 가능..
    static String sum(String x, String y, String z) {
        return x + y + z;
    }

    // 매개변수의 타입 또는 순서가 달라 가능
    static String sum(int x, String y, int z) {
        return x + y + z;
    }
}
