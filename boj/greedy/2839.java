package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main_2839_설탕배달_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());

        int cnt = 0;
        for(int i = 0, len = N/5; i <= len; i++){

            if((N - 5*i) % 3 == 0){
                cnt = 0;
                cnt += i;
                cnt += (N - 5*i) / 3;
            }
        }
        if(cnt == 0){
            cnt = -1;
        }
        System.out.println(cnt);
    }
}