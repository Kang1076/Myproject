package java1129;

public class c_MemberLocalVariable {
        int a;  // 멤버변수
        void printNumber(int c) {
                int b = 1; // 지역변수
                System.out.println("멤버변수: " + a);
                System.out.println("지역변수: " + b);
                System.out.println("매개변수: " + c);
        }

        public static void main(String[] args) {
                c_MemberLocalVariable m = new c_MemberLocalVariable();
                m.printNumber(4);
                // 출력 시 멤버변수:0, 지역변수:1, 매개변수:4가 나온다.
    }
}
