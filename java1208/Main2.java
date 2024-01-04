package java1208;
import java.util.ArrayList;
import java.util.List;

public class Main2 {
    public static void main(String[] args) {
        List<MenuInfo> m1 = new ArrayList<>();
        m1.add(new MenuInfo("아메리카노",4500,"커피","씁쓸한 맛"));
        m1.add(new MenuInfo("라떼",5200,"커피","우유가 포함되어 고소함"));

        MenuInfo test = new MenuInfo("카라멜마끼야또",5800,"커피","카라멜이 들어가 달달함");
        m1.add(test);

        for (MenuInfo e : m1) e.getMenuInfo();
    }
}
