package java1208;

import java.util.List;
import java.util.Vector;

public class Main1 {
    public static void main(String[] args) {
        List<NameCard> n1 = new Vector<>();
        n1.add(new NameCard("양콩미","010-1234-1234","aaa@naver.com","Junior",
                "서울시 강남구"));
        n1.add(new NameCard("홍길동","010-0987-1234","bbb@kakao.com","Junior",
                "수원시 영통구"));
        n1.add(new NameCard("도래미","010-3422-1234","ccc@naver.com","Senior",
                "서울시 송파구"));

        for (NameCard e : n1) {
            System.out.println("이름 : " + e.name);
            System.out.println("전화번호 : " + e.phone);
            System.out.println("메일 : " + e.mail);
            System.out.println("직급 : " + e.position);
            System.out.println("주소 : " + e.address);
            System.out.println();
        }
    }
}
class NameCard {
    String name;
    String phone;
    String mail;
    String position;
    String address;
    public NameCard(String name, String phone, String mail, String position, String address) {
        this.name = name;
        this.phone = phone;
        this.mail = mail;
        this.position = position;
        this.address = address;
    }
}
