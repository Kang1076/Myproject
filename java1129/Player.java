package java1129;

public class Player {
        String name;
        int level;
        int atk;
        int hp;
        // 공통되는 부분만 넣도록 한다.

        void characterInfo() {
                System.out.println("*** 캐릭터 정보 ***");
                System.out.println("#아이디: " + name);
                System.out.println("#레벨: " + level);
                System.out.println("#공격력: " + atk);
                System.out.println("#체력: " + hp);
        }
}
