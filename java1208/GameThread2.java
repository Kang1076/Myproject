package java1208;

public class GameThread2 extends Thread {
    private Character warrior;
    private Character wizard;

    public GameThread2(Character warrior, Character wizard) {
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
                sleep(3300);
                normal = (int)(Math.random() * 2);
                special = (int)(Math.random() * 18);
                if (normal == 1) {
                    System.out.println("마법 공격 : " + warrior.name + "에게 " + wizard.mAttack() + " 데미지를 입혔습니다.");
                    endGame = warrior.setDamage(wizard.mAttack());
                } else {
                    System.out.println("물리 공격 : " + warrior.name + "에게 " + wizard.pAttack() + " 데미지를 입혔습니다.");
                    endGame = warrior.setDamage(wizard.pAttack());
                }
                if (special == 10) {
                    System.out.println(wizard.name + " 궁극기 발동 !!!!!, " + warrior.name + "에게 " + wizard.ultimate()
                            + " 데미지를 입혔습니다.");
                    endGame = warrior.setDamage(wizard.ultimate());
                }
                if (endGame) {
                    System.exit(0);
                }

            } catch (InterruptedException e) {}
        }
    }
}
