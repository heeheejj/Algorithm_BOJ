import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_11660_구간합구하기5_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        // 표의 크기 N, 합을 구해야 하는 tc 개수 M 입력받기
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 표 입력받아 2차원 배열로 만들기
        int[][] nums = new int[N+1][N+1];
        for(int i = 1; i <= N; i++){
            st = new StringTokenizer(in.readLine(), " ");
            for(int j = 1; j <= N; j++){
                nums[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // (x1, y1)부터 (x2, y2)까지 합구하기를 M번 반복
        int[][] dp = new int[N+1][N+1];
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= N; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + nums[i][j];
            }
        }

        for(int i = 0; i < M; i++){
            st = new StringTokenizer(in.readLine(), " ");
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            System.out.println(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]);
        }
    }
}
