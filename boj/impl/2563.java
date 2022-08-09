package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2563_색종이_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());

        int result = 0;
        boolean[][] area = new boolean[100][100];   // area[i][0]일때 or area[0][j]일때 제외하고 true개수 세주면 됨

        for(int n = 0; n < N; n++){
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            int xLen = Integer.parseInt(st.nextToken());
            int yLen = Integer.parseInt(st.nextToken());

            // 현재 색종이의 구역을 true로 바꾸기
            for(int i = 0; i < 10; i++){
                for(int j = 0; j < 10; j++){
                    boolean temp = area[xLen+i][yLen+j];
                    if(temp){   // 이미 true로 바뀐 구역이라면 다음루프로
                        continue;
                    }else{
                        area[xLen+i][yLen+j] = true;
                        result++;
                    }
                }
            }
        }
        System.out.println(result);
    }
}
