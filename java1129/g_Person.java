package java1129;

public class g_Person {
        String name;
        int age;
        double key;

        g_Person(String pName, int pAge, double pKey){
                System.out.println("1번 생성자 호출!");
                name = pName;
                age = pAge;
                key = pKey;
        }

        void info() {
                System.out.println("*** 사람의 정보 ***");
                System.out.println("# 이름: " + name);
                System.out.println("# 나이: " + age);
                System.out.println("# 키: " + key);
        }
}
