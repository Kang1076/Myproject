package SwitchStudy;

import java.util.Scanner;

public class TicketReservation {
    int[] seat = new int[10];

    public void printSeat() {
        for (int i = 0; i < seat.length; i++) {
            if (seat[i] == 0) System.out.print("[ ] ");
            else System.out.print("[V] ");
        }
        System.out.println();
    }

    public void ticketReserv() {
        printSeat();
        Scanner sc = new Scanner(System.in);
            System.out.print("좌석을 선택하세요. : ");
            int num = sc.nextInt();
            seat[num - 1] = 1;
            for (int e : seat) {
                if (e == 1) {
                    System.out.print("[V] ");
                }
                else System.out.print("[ ] ");
            }
                System.out.println();
    }

    public int total() {
        int cnt = 0;
        for (int e : seat) {
            if (e == 1) cnt++;
        }
        return cnt * 12000;
    }
}
