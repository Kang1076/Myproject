package java1207;
import java.util.Scanner;

public class Person {
    protected int age;
    protected int sleep;

    void setAge(int ages) {
        age = ages;
    }

    int getAge() {
        return age;
    }
    void setSleep(int sleeping) {
        sleep = sleeping;
    }
    int getSleep() {
        return sleep;
    }
}

class Worker extends Person {
    int workTime;

    void setWorkTime(int time) {
        workTime = time;
    }
    int getWorkTime() {
        return workTime;
    }
    void WorkerInfo() {
        System.out.println("===== 직장인 =====");
        System.out.println("나이 : " + getAge() + "세");
        System.out.println("수면시간 : " + getSleep() + "시간");
        System.out.println("근무시간 : " + getWorkTime() + "시간");
    }
}

class Student extends Person {
    int studyType;

    void setStudyType() {
        Scanner sc = new Scanner(System.in) ;
        System.out.print("공부 타입 [1]열심히 [2]적당히 [3]놀면서 : ");
        studyType = sc.nextInt();
    }
    String getStudyType() {
        if (studyType == 1) return "열심히";
        else if (studyType == 2) return "적당히";
        return "놀면서";
    }
    void StudentInfo() {
        System.out.println("===== 학생 =====");
        System.out.println("나이 : " + getAge() + "세");
        System.out.println("수면시간 : " + getSleep() + "시간");
        System.out.println("근무시간 : " + getStudyType() + "합니다.");
    }
}
