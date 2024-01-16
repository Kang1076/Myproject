package java0720;

import java.util.Arrays;

public class b_example {
    public static void main(String[] args) {

        int[] arr = {1, 3, 5, 7, 9, 11, 13};

        System.out.println(arr.length);

        for (int i=3; i<arr.length-1; i++) {
                arr[i] = arr[i+1];
        }

        int[] temp = new int[arr.length-1];

        for (int j=0; j<temp.length; j++) {
                temp[j] = arr[j];
        }
        arr = temp;
        temp = null;
        System.out.println(Arrays.toString(arr));
    }
}
