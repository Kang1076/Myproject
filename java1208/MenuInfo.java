package java1208;

public class MenuInfo {
    String name;
    int price;
    String group;
    String desc;

    public MenuInfo(String name, int price, String group, String desc) {
        this.name = name;
        this.price = price;
        this.group = group;
        this.desc = desc;
    }

    public void getMenuInfo() {
        System.out.println("메뉴명 : " + name);
        System.out.println("가격 : " + price);
        System.out.println("분류 : " + group);
        System.out.println("설명 : " + desc);
        System.out.println();
    }
}
