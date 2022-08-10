package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main_16926_배열돌리기1_정희주 {
    static int[] dx;
    static int[] dy;
    static int[][] arr;
    static int N;
    static int M;
    static int R;

    static void rotate(int depth){
        // 각 depth의 시작 좌표 (가장 왼쪽이자 가장 위쪽인 좌표)
        int nx = depth; // 시작 x좌표
        int ny = depth; // 시작 y좌표

        // 해당 depth에 대해 시작 좌표부터 → ↓ ← ↑ 이렇게 돌아서 다시 시작좌표 직전까지 오는 수열을 queue에 저장
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < 4; i++){
            while(true){
                int tempX = nx+dx[i];
                int tempY = ny+dy[i];
                if(tempX < depth || tempX >= (N-depth)
                    || tempY < depth || tempY >= (M-depth)) break;   // 범위 벗어나면 break하고 방향전환
                queue.add(arr[nx][ny]); // 큐에 현재 위치 일단 넣고
                nx = tempX; // nx 바꿔줌
                ny = tempY;
            }
        }

        // 돌린다. (큐에서 첫번째꺼 빼서 맨뒤에 넣는다.)
        for(int i = 0; i < R; i++){
            int firstNum = queue.poll();
            queue.add(firstNum);
        }

        nx = depth;
        ny = depth;
        // 돌리기가 끝난 수열을 다시 배열에 setting한다.
        for(int i = 0; i < 4; i++){
            while(true){
                int tempX = nx+dx[i];
                int tempY = ny+dy[i];
                if(tempX < depth || tempX >= (N-depth)
                        || tempY < depth || tempY >= (M-depth)) break;   // 범위 벗어나면 break
                arr[nx][ny] = queue.poll(); // 큐에서 꺼내서 배열에 저장
                nx = tempX; // nx 바꿔줌
                ny = tempY;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        // 원본배열 저장
        arr = new int[N][M];
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(in.readLine(), " ");
            for(int j = 0; j < M; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // dx, dy 할당
        dx = new int[]{0, 1, 0, -1};
        dy = new int[]{1, 0, -1, 0};

        // depth별로 큐에 넣기
        int depthMax = Math.min(N, M) / 2;

        // depth별로 돌리기
        for(int i = 0; i < depthMax; i++){
            rotate(i);
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                sb.append(arr[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
