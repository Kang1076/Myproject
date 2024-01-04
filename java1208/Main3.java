package java1208;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

// [1] 메뉴보기 [2] 메뉴조회 [3] 메뉴추가 [4]메뉴삭제 [5]메뉴수정 [6]종료
public class Main3 {
    Map<String, MenuInfo1> map = new TreeMap<>();
    public static void main(String[] args) {
        Main3 coffee = new Main3();
        coffee.makeMenu();
        coffee.selectMenu();
    }

    void makeMenu() {
        map.put("아메리카노", new MenuInfo1("아메리카노", 3500, "커피", "씁쓸한 맛"));
        map.put("라떼", new MenuInfo1("라떼", 4000, "커피", "고소한 맛"));
        map.put("카라멜마끼야또", new MenuInfo1("카라멜마끼야또", 4300, "커피", "달달한 맛"));
    }

    void selectMenu() {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("메뉴를 선택 하세요.");
            System.out.print("[1] 메뉴보기 [2] 메뉴조회 [3] 메뉴추가 [4] 메뉴삭제 [5]메뉴수정 [6]종료 : ");
            int selMenu = sc.nextInt();
            String menu = "";
            switch (selMenu) {
                case 1 :
                    System.out.println("======== 메뉴 보기 ========");
                    for (String key : map.keySet()) {
                        System.out.println("메뉴 : " + map.get(key).name);
                        System.out.println("가격 : " + map.get(key).price);
                        System.out.println("분류 : " + map.get(key).group);
                        System.out.println("설명 : " + map.get(key).desc);
                        System.out.println("---------------------------");
                    }
                    break;
                case 2 :
                    System.out.print("조회할 메뉴 선택 : ");
                    menu = sc.next();
                    if (map.containsKey(menu)) { // map에 키가 존재하는지 확인 (boolean)
                        System.out.println("메뉴 : " + map.get(menu).name);
                        System.out.println("가격 : " + map.get(menu).price);
                        System.out.println("분류 : " + map.get(menu).group);
                        System.out.println("설명 : " + map.get(menu).desc);
                    } else System.out.println("선택하신 메뉴는 존재하지 않습니다.");
                    break;
                case 3 :
                    System.out.print("추가할 메뉴를 입력 하세요 : ");
                    menu = sc.next();
                    if (map.containsKey(menu)) {
                        System.out.println("해당 메뉴가 이미 존재 합니다.");
                    } else {
                        System.out.print("가격 : ");
                        int price = sc.nextInt();
                        System.out.print("분류 : ");
                        String group = sc.next();
                        sc.nextLine(); // 버퍼 비우기
                        System.out.print("설명 : ");
                        String desc = sc.nextLine();
                        map.put(menu,new MenuInfo1(menu, price, group, desc));
                    }
                    break;
                case 4 :
                    System.out.print("삭제할 메뉴를 입력 하세요 : ");
                    menu = sc.next();
                    if(map.containsKey(menu)) {
                        map.remove(menu);
                        System.out.println(menu + "을(를) 삭제하였습니다.");
                    }else System.out.println("삭제 할 메뉴가 없습니다.");
                    break;
                case 5 :
                    System.out.print("수정할 메뉴를 입력 하세요 : ");
                    menu = sc.next();
                    if (map.containsKey(menu)) {
                        System.out.print("메뉴 : ");
                        String name = sc.next();
                        System.out.print("가격 : ");
                        int price = sc.nextInt();
                        System.out.print("분류 : ");
                        String group = sc.next();
                        sc.nextLine(); // 버퍼 비우기
                        System.out.print("설명 : ");
                        String desc = sc.nextLine();
                        map.replace(menu,new MenuInfo1(name, price, group, desc));
                    } else System.out.println("수정할 메뉴가 없습니다.");
                    break;
                case 6 :
                    System.out.println("메뉴를 종료 합니다.");
                    return;
            }
        }
    }
}
