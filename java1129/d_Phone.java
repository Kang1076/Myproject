package java1129;

public class d_Phone {
        String model;
        String color;
        int price;

        // 생성자 선언
        d_Phone() {
                System.out.println("1번 생성자 호출!");
                model = "애니콜";
                color = "회색";
                price = 20000;
        }

        d_Phone(String pModel, String pColor) {
                System.out.println("3번 생성자 호출!!!");
                model = pModel;
                color = pColor;
        }

        d_Phone(String pModel) {
                System.out.println();
                System.out.println("2번 생성자 호출!");
                model = pModel;
                color = "블루";
                price = 1000000;
        }

        d_Phone(String pModel, String pColor, int pPrice) {
                System.out.println("4번 생성자 호출!");
                model = pModel;
                color = pColor;
                price = pPrice;
        }

        void showSpec() {
                System.out.println("*** 핸드폰의 정보 ***");
                System.out.println("# 모델명: " + model);
                System.out.println("# 색상: " + color);
                System.out.println("# 가격: " + price);
        }
}
