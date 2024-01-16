package java1206;

public class FinalOverriding {
    public static void main(String[] args) {
        SportsCar sportsCar = new SportsCar("람보르기니");
        sportsCar.setTurbo(true);
        sportsCar.infoCar();
        sportsCar.accelerator();
        sportsCar.breakPanel();

        ElectricCar electricCar = new ElectricCar("테슬라");
        electricCar.setAutoDrv(true);
        electricCar.infoCar();
    }
}
