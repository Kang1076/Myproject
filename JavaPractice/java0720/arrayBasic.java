package java0720;

import java.sql.SQLOutput;
import java.util.Arrays;
public class arrayBasic {
    public static void main(String[] args) {
        // 1.배열의 변수 선언.
        int[] arr; // java style.
        int arr2[]; // c style.

        // 2.배열 객체의 생성 - 실제 값들이 저장될 공간을 생성.
        arr = new int[5];
        System.out.println(arr);

        // 3.배열의 초기화 - 배열 내부에 실제 값을 저장하는 행위.
        // 배열의 초기화는 인덱스를 통해 수행합니다.
        // 인덱스란 배열 내부의 위치를 저장하는 값이며
        // 0번부터 시작하여 1씩 순차적으로 증가합니다. 5개일 경우 -> 0~4

        arr[0] = 87; // arr=87;(x)
        arr[1] = 95;
        arr[2] = arr[0];
        arr[3] = (int) 3.14;
        arr[4] = 100;

        // 4.배열의 총 크기(길이) 확인. (배열변수명.length)
        System.out.println("arr배열의 길이: " + arr.length);

        // 5.배열에 저장된 값을 참조하는 법(사용하는 법)
        System.out.println(":배열의 1번째 데이터: " + arr[0]);
        System.out.println(":배열의 2번째 데이터: " + arr[1]);
        System.out.println(":배열의 3번째 데이터: " + arr[2]);
        System.out.println(":배열의 4번째 데이터: " + arr[3]);
        System.out.println(":배열의 5번째 데이터: " + arr[4]);

        // 6.배열의 반복문 처리.
        System.out.println("-----------------------------");
        for (int idx=0; idx<arr.length; idx++) {
                System.out.println("배열의 " + (idx+1) + "번째 데이터: " + arr[idx]);

            // 7.배열의 내부 요소값을 문자열 형태로 한눈에 출력하기
                    System.out.println("-----------------------------");
                    System.out.println(Arrays.toString(arr));   // 자동완성으로 해야 맨앞에 import

            // 8.배열의 선언과 동시에 생성을 하는 방법
                    double[] dArr = new double[3];

                    String[] sArr = new String[4];
                    byte[] bArr = new byte[7];

                    System.out.println("-----------------------------");
                    System.out.println(Arrays.toString(dArr));
                    System.out.println(Arrays.toString(sArr));
                    System.out.println(Arrays.toString(bArr));

                    // 배열의 생성과 동시에 초기화를 하는 방법
                    System.out.println("-----------------------------");

                    char[] letters = new char[] {'A', 'b', 'c', 'd'};
                    System.out.println(Arrays.toString(letters));

                    // 선언과 동시에 초기화를 할 때 단 1번만 가능한 문법.
                    String[] names = {"김철수", "홍길동", "박영희"};
                    System.out.println(Arrays.toString(names));

                    names = new String[] {"김철수", "홍길동", "박영희", "박찬호"};
                    System.out.println(Arrays.toString(names));

        }
    }
}
