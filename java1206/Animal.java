package java1206;

public class Animal {
    String name;
    void setName(String name) {
        this.name = name;
    }
}

class Dog extends Animal {
    void sleep() {
        System.out.println(name + "은(는) 잠을 잡니다.");
    }
}
class HouseDog extends Dog {
    @Override // (어노테이션) 오버라이드 했다는 걸 관례적으로 알려주는 것
    void sleep() {
        System.out.println(name + "은(는) 집에서 잠을 잡니다.");
    }
    // 오버로딩 관계가 성립함
    void sleep(int time) {
        System.out.println(name + "가(이) " + time + "시간 동안 집에서 잠을 잡니다.");
    }
}
