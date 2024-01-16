package java1129;

public class MainClass {
        public static void main(String[] args) {
                Warrior w1 = new Warrior();
                w1.name = "전사1";
                w1.level = 1;
                w1.atk = 3;
                w1.hp = 50;
                w1.rage = 60;
                w1.characterInfo();

                Mage m1 = new Mage();
                m1.name = "마법사1";
                m1.level = 15;
                m1.atk = 4;
                m1.hp = 45;
                m1.skill = "fuck!";
                m1.characterInfo();

                Hunter h1 = new Hunter();
                h1.name = "헌터1";
                h1.level = 441;
                h1.atk = 23144;
                h1.hp = 5335;
                h1.characterInfo();
    }
}
