package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_16935_배열돌리기3_정희주 {
    static int[][] arr;
    static int N;
    static int M;
    static void oper1(){    // 1번 연산: 상하 반전
        int[][] tempArr = new int[N][M];
        for(int i = 0; i < N; i++){
//            for(int j = 0; j < M; j++){
//                tempArr[i][j] = arr[N-1-i][j];
//            }
            // 위에처럼 안하고 2차원배열 중 안쪽배열의 레퍼런스만 교환해도 됨!!
            tempArr[i] = arr[N-1-i];
        }
        arr = tempArr;
    }

    static void oper2(){    // 2번 연산: 좌우 반전
        int[][] tempArr = new int[N][M];
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                tempArr[i][j] = arr[i][M-1-j];
            }
        }
        arr = tempArr;
    }

    static void oper3(){    // 3번 연산: 오른쪽으로 90도 회전
        int[][] tempArr = new int[M][N];
        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                tempArr[i][j] = arr[N-j-1][i];
            }
        }
        arr = tempArr;
    }

    static void oper4(){    // 4번 연산: 왼쪽으로 90도 회전
        int[][] tempArr = new int[M][N];
        for(int i = 0; i < M; i++){
            for(int j = 0; j < N; j++){
                tempArr[i][j] = arr[j][M-i-1];
            }
        }
        arr = tempArr;
    }

    static void oper5(){    // 5번 연산
        int[][] tempArr = new int[N][M];
        int[] moveXLen = new int[]{0, N/2, 0, -1*(N/2)};
        int[] moveYLen = new int[]{M/2, 0, -1*(M/2), 0};

        int startX = 0; // 각 그룹의 시작 X 인덱스
        int startY = 0; // 각 그룹의 시작 Y 인덱스
        for(int g = 0; g < 4; g++){
            for(int i = 0; i < N/2; i++){
                for(int j = 0; j < M/2; j++){
                    int movedXIdx = startX+i+moveXLen[g];   // 연산 후의 X idx 계산
                    int movedYIdx = startY+j+moveYLen[g];   // 연산 후의 Y idx 계산
                    tempArr[movedXIdx][movedYIdx] = arr[startX+i][startY+j];    // 이동
                }
            }
            startX += moveXLen[g];  // 다음 그룹의 시작 X인덱스 setting
            startY += moveYLen[g];  // 다음 그룹의 시작 Y인덱스 setting
        }

        arr = tempArr;
    }

    static void oper6(){    // 6번 연산
        int[][] tempArr = new int[N][M];

        int[] moveXLen = new int[]{N/2, 0, -1*(N/2), 0};
        int[] moveYLen = new int[]{0, M/2, 0, -1*(M/2)};

        int startX = 0; // 각 그룹의 시작 X 인덱스
        int startY = 0; // 각 그룹의 시작 Y 인덱스
        for(int g = 0; g < 4; g++){
            for(int i = 0; i < N/2; i++){
                for(int j = 0; j < M/2; j++){
                    int movedXIdx = startX+i+moveXLen[g];   // 연산 후의 X idx 계산
                    int movedYIdx = startY+j+moveYLen[g];   // 연산 후의 Y idx 계산
//                    System.out.println("arr: startX: "+startX+"/ i: "+i+"/ startY: "+startY+"/ j: "+j);
//                    System.out.println("tempArr: movedXIdx: "+movedXIdx+"/ movedYIdx: "+movedYIdx);
                    tempArr[movedXIdx][movedYIdx] = arr[startX+i][startY+j];    // 이동
                }
            }
            startX += moveXLen[g];  // 다음 그룹의 시작 X인덱스 setting
            startY += moveYLen[g];  // 다음 그룹의 시작 Y인덱스 setting
        }

        arr = tempArr;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        // 초기배열 입력받아 저장
        arr = new int[N][M];
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(in.readLine(), " ");
            for(int j = 0; j < M; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 연산하기
        st = new StringTokenizer(in.readLine(), " ");
        boolean isSwitchedNM = false;
        for(int i = 0; i < R; i++){
            int operNum = Integer.parseInt(st.nextToken());
            switch (operNum){
                case 1: oper1(); isSwitchedNM = false; break;
                case 2: oper2(); isSwitchedNM = false; break;
                case 3: oper3(); isSwitchedNM = true; break;
                case 4: oper4(); isSwitchedNM = true; break;
                case 5: oper5(); isSwitchedNM = false; break;
                case 6: oper6(); isSwitchedNM = false; break;
            }
            if(isSwitchedNM){
                int temp = N;
                N = M;
                M = temp;
            }
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
