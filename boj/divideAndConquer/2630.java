package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2630_색종이만들기_정희주 {
    static int[][] map;
    static int bCnt;
    static int wCnt;
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());

        map = new int[N][N];
        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(in.readLine(), " ");
            for(int j = 0; j < N; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        divide(N, 0, 0);

        System.out.println(wCnt);
        System.out.println(bCnt);
    }

    static void divide(int N, int startX, int startY){
        // 색깔 확인
        int firstColor = 0; // 가장 왼쪽 위 인덱스의 색을 저장 - 1이면 파란색, 0이면 하얀색
        if(map[startX][startY] == 1){
            firstColor = 1;
        }

//        System.out.println("N: "+N+"/ startX: "+startX+"/ startY: "+startY+"/ firstColor: "+firstColor);

        if(N == 1){
            if(firstColor == 1){
                bCnt++;
//                System.out.println("bCnt: "+bCnt);
            }else{
                wCnt++;
//                System.out.println("wCnt: "+wCnt);
            }
            return;
        }

        // 모두 같은 색인지 확인
        boolean isSameColor = true;
        for(int i = startX; i < startX+N; i++){
            for(int j = startY; j < startY+N; j++){
                if(firstColor != map[i][j]){
                    isSameColor = false;
                }
            }
        }

        if(isSameColor){
            if(firstColor == 1){
                bCnt++;
//                System.out.println("bCnt: "+bCnt);
            }else{
                wCnt++;
//                System.out.println("wCnt: "+wCnt);
            }
            return;
        }else{
            N /= 2;
            divide(N, startX, startY);
            divide(N, startX+N, startY);
            divide(N, startX, startY+N);
            divide(N, startX+N, startY+N);
        }
    }
}