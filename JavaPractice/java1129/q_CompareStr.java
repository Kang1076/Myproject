package java1129;
import java.util.Scanner;
public class q_CompareStr {
        public static void main(String[] args) {
                String name = "홍길동";
                String name2 = "홍길동";
                System.out.println(name == name2);

                p_User kim = new p_User("abc1234");

                Scanner sc = new Scanner(System.in);
                System.out.println("비밀번호를 입력하세요: ");
                String password = sc.next();

                System.out.println("내가 방금 입력한 비번: " + password);
                System.out.println("가입 당시 설정한 비번: " + kim.pw);

                System.out.println("kim.pw == password : " + (kim.pw == password));
                System.out.println("----------------------");
                System.out.println("kim.equals(password):" + (kim.pw.equals(password)));

                System.out.println(kim);
                System.out.println(password.hashCode());
    }
}
