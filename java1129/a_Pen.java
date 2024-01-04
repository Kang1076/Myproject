package java1129;
// 설계용 클래스(라이브러리 클래스)에서는 메인메서드를 작성하지 않습니다.
public class a_Pen {
    // 객체의 속성을 필드(클래스 맴버변수)라고 부릅니다.
    String color;
    int price;

    // 객체의 기능들을 메서드라고 부릅니다.
    void write() {
            System.out.println(color + "색 글을 씁니다.");
    }
    void priceInfo() {
            System.out.println(color + "펜의 가격은" + price + "원 입니다.");
    }
}
