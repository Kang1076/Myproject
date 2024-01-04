package SwitchStudy;

public class WhileEx1 {
    public static void main(String[] args) {
        int treeHit = 0;

        while(true) {
            treeHit++;
            System.out.println("나무를 " + treeHit + "번 찍었습니다.");
            if (treeHit == 10) {
                System.out.println("나무가 쓰러집니다.");
                break;
            }
        }
    }
}
