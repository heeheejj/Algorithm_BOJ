package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1074_Z_정희주 {
    static int cnt, r, c;
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        divide((int) Math.pow(2, N), 0, 0);
    }

    static void divide(int K, int startX, int startY){
        if(K == 1){
            System.out.println(cnt);
            return;
        }
        K /= 2;
        int borderX = startX + K;
        int borderY =  startY + K;
        int kPow = K*K;
        if(r < borderX & c < borderY){  // r, c가 1사분면
            divide(K, startX, startY);
        } else if (r < borderX & c >= borderY) { // 2사분면
            cnt += kPow;
            divide(K, startX, startY+K);
        } else if (r >= borderX & c < borderY) { // 3사분면
            cnt += 2*kPow;
            divide(K, startX+K, startY);
        } else{ // 4사분면
            cnt += 3*kPow;
            divide(K, startX+K, startY+K);
        }
    }
}
