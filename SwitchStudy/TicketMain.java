package SwitchStudy;

import java.util.Scanner;

public class TicketMain {
    public static void main(String[] args) {
        TicketReservation movie = new TicketReservation();
        Scanner sc = new Scanner(System.in);
        while(true) {
            System.out.println("[1]예약하기");
            System.out.println("[2]종료하기");
            int menu = sc.nextInt();
            if (menu == 1) movie.ticketReserv();
            else {
                System.out.println(movie.total());
                break;
            }
        }
    }
}
