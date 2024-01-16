package java0720;

public class RandomExample {
    public static void main(String[] args) {
        // 난수(랜덤값)를 발생시키는 메서드 Math.random()
        // 0.01이상 1.0미만의 랜덤 실수값을 가져옵니다.(double타입)

        // double rn = Math.random(); <== 기본형
        // 1~10까지의 정수 난수를 발생시키고 싶어요.
        int rn = (int) ((Math.random() * 10) + 1);

        // 로또의 범위 (1~45까지의 정수 난수)
        int rw = (int) ((Math.random() * 45) + 1);
        int rn1 = (int) (Math.random()); // 캐스팅 단축키 컨트롤+1

        System.out.println(rn1);
        System.out.println(rw);
    }
}
