package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 시간 초과
public class Main_1074_Z_정희주_2 {
    static int cnt, r, c;
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        cnt = -1; // 첫번째 방문 = 0출력

        divide((int) Math.pow(2, N), 0, 0);
    }

    static void divide(int K, int startX, int startY){
        if(K == 1){
            cnt++;
            if(startX == r & startY == c){
                System.out.println(cnt);
                System.exit(1);
            }
            return;
        }
        K /= 2;
        divide(K, startX, startY);
        divide(K, startX, startY+K);
        divide(K, startX+K, startY);
        divide(K, startX+K, startY+K);
    }
}
