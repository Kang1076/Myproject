package java0720;

public class EnhancedForLoop {
    public static void main(String[] args) {

        String[] week = {"월", "화", "수", "목", "금", "토", "일"};

        for (int idx=0; idx<week.length; idx++) {
                System.out.println(week[idx] + "요일");
        }

        for (String day : week) {
                System.out.println(day + "요일");
        }

        System.out.println("------------------------------------");
        /*
         1. score라는 int 배열에 점수 데이터를 저장하세요.
         ex) [98, 71, 85, 67, 100, 95]
         2. 향상된 for문을 사용해서 총점과 평균을 출력하세요.
         3. 평균은 double타입입니다. 소수점 둘째자리까지 출력하세요.
         */
        int[] scores = {98, 71, 85, 66, 100, 95};

        int total = 0;
        for (int score : scores) {
                total += score;
        }
        double avg = total / scores.length;
        System.out.printf("총점: %d점, 평균: %2f\n", total, avg);
    }
}
