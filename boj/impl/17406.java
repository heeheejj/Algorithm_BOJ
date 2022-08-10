package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 2차원 배열 깊은 복사

public class Main_17406_배열돌리기4_정희주 {
    static int[] dx = new int[]{0, 1, 0, -1};
    static int[] dy = new int[]{1, 0, -1, 0};
    static int[][] arr;
    static int[][] originalArr;
    static int[][] RCSs;
    static int N, M, K;
    static int result = Integer.MAX_VALUE;

    // 순열 관련 애들
    static int[] numbers, inputs;	// 뽑힌 애들, input
    static boolean[] isSelected;	// 뽑을 수 있는 수

    private static void perm(int cnt) {
        if(cnt == K) {
            for(int i = 0; i < K; i++){
                int tempIdx = numbers[i];
                int R = RCSs[tempIdx][0];
                int C = RCSs[tempIdx][1];
                int S = RCSs[tempIdx][2];

                // depth별로 돌리기
                for(int d = 0; d < S; d++){
                    rotate(R, C, S, d);
                }
            }

            // 배열의 값의 최솟값 구하기
            int minRowSum = Integer.MAX_VALUE;  // 행의 합의 최솟값
            for(int n = 1; n <= N; n++){
                int sum = Arrays.stream(arr[n]).sum();  // n번째 행의 합
                if(minRowSum > sum) minRowSum = sum;
            }

            if(result > minRowSum){
                result = minRowSum;
            }

            // 다음을 위해 초기화
            // 배열 복사 (깊은 복사)
            for(int i = 0; i <= N; i++){
                System.arraycopy(originalArr[i], 0, arr[i], 0, M+1);
            }
            return;
        }

        for(int i = 0; i < K; i++) {
            if(isSelected[i]) continue;
            numbers[cnt] = inputs[i];
            isSelected[i] = true;
            perm(cnt+1);
            isSelected[i] = false;
        }
    }

    static void rotate(int R, int C, int S, int depth){
        // 각 depth의 시작 좌표 (가장 왼쪽이자 가장 위쪽인 좌표)
        int nx = R-S+depth; // 시작 x좌표
        int ny = C-S+depth; // 시작 y좌표

        // 해당 depth에 대해 시작 좌표부터 → ↓ ← ↑ 이렇게 돌아서 다시 시작좌표 직전까지 오는 수열을 queue에 저장
        Deque<Integer> queue = new ArrayDeque<>();
        int xStartIdx = R-S+depth;  int xEndIdx = R+S-depth;    // 경계값 저장
        int yStartIdx = C-S+depth;  int yEndIdx = C+S-depth;
        for(int i = 0; i < 4; i++){
            while(true){
                int tempX = nx+dx[i];
                int tempY = ny+dy[i];
                if(tempX < xStartIdx || tempX > xEndIdx
                        || tempY < yStartIdx || tempY > yEndIdx) break;   // 범위 벗어나면 break하고 방향전환
                queue.add(arr[nx][ny]); // 큐에 현재 위치 일단 넣고
                nx = tempX; // nx 바꿔줌
                ny = tempY;
            }
        }

        // 돌린다. (큐에서 맨뒤에꺼 빼서 맨앞에 넣는다.)
        int firstNum = queue.pollLast();
        queue.addFirst(firstNum);

        nx = R-S+depth;
        ny = C-S+depth;

        // 돌리기가 끝난 수열을 다시 배열에 setting한다.
        for(int i = 0; i < 4; i++){
            while(true){
                int tempX = nx+dx[i];
                int tempY = ny+dy[i];
                if(tempX < xStartIdx || tempX >xEndIdx
                        || tempY < yStartIdx || tempY > yEndIdx) break;   // 범위 벗어나면 break하고 방향전환
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
        K = Integer.parseInt(st.nextToken());

        originalArr = new int[N+1][M+1];
        for(int i = 1; i <= N; i++){
            st = new StringTokenizer(in.readLine(), " ");
            for(int j = 1; j <= M; j++){
                originalArr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        arr = new int[N+1][M+1];
        // 배열 복사 (깊은 복사)
        for(int i = 0; i <= N; i++){
            System.arraycopy(originalArr[i], 0, arr[i], 0, M+1);
        }

        // R, C, S 값 입력받아 저장,
        RCSs = new int[K][3];
        inputs = new int[K];
        numbers = new int[K];
        isSelected = new boolean[K];
        for(int i = 0; i < K; i++){
            st = new StringTokenizer(in.readLine(), " ");

            RCSs[i][0] = Integer.parseInt(st.nextToken());    // R
            RCSs[i][1] = Integer.parseInt(st.nextToken());    // C
            RCSs[i][2] = Integer.parseInt(st.nextToken());   // S, S는 곧 depthMax

            // {R, C, S} set의 인덱스를 저장 -> 순열의 input이 될 것임
            inputs[i] = i;
        }

        perm(0);

        System.out.println(result);
    }
}
