package java1208;

// 스레드 생성, 전사 캐릭터에 대한 구현부
public class GameThread1 extends Thread {
    private Character warrior;
    private Character wizard;

    public GameThread1(Character warrior, Character wizard) {
        this.warrior = warrior;
        this.wizard = wizard;
    }

    @Override
    public void run() {
        int normal;
        int special;
        boolean endGame = false;
        while(true) {
            try {
                sleep(3000);
                normal = (int)(Math.random() * 2);
                special = (int)(Math.random() * 20);
                if (normal == 1) {
                    System.out.println("물리 공격 : " + wizard.name + "에게 " + warrior.pAttack() + " 데미지를 입혔습니다.");
                    endGame = wizard.setDamage(warrior.pAttack());
                } else {
                    System.out.println("마법 공격 : " + wizard.name + "에게 " + warrior.mAttack() + " 데미지를 입혔습니다.");
                    endGame = wizard.setDamage(warrior.mAttack());
                }
                if (special == 10) {
                    System.out.println(warrior.name + " 궁극기 발동 !!!!!, " + wizard.name + "에게 " + warrior.ultimate()
                    + " 데미지를 입혔습니다.");
                    endGame = wizard.setDamage(warrior.ultimate());
                }
                if (endGame) {
                    System.exit(0);
                }

            } catch (InterruptedException e) {}
        }
    }
}
