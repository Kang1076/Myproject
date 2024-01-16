package java1129;

public class e_PhoneFactory {
        public static void main(String[] args) {

            d_Phone basic = new d_Phone();
            basic.showSpec();

            d_Phone galaxys10 = new d_Phone("갤럭시s10");
            galaxys10.showSpec();

            d_Phone iPhoneXs = new d_Phone("아이폰Xs", "스페이스그레이");
            iPhoneXs.showSpec();

            d_Phone xiaomi = new d_Phone("흥미노트","에메랄드", 400000);
            xiaomi.showSpec();

    }
}
