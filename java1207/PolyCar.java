package java1207;

import java.util.Scanner;

public class PolyCar {
    public static void main(String[] args) {
        Driver driver = new Driver("홍길동");
        SportsCar sportsCar = new SportsCar();
        Bus bus = new Bus();
        Taxi taxi = new Taxi();
        Scanner sc = new Scanner(System.in);
        System.out.print("운전하고 싶은 차를 선택하세요. [1]스포츠카 [2]버스 [3]택시 : ");
        int selCar = sc.nextInt();
        switch(selCar) {
            case 1 : driver.drive(sportsCar); break;
            case 2 : driver.drive(bus); break;
            case 3 : driver.drive(taxi); break;
        }
    }
}
