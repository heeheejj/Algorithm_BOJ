import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_11659_구간합구하기4_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");

        // 수의 개수 N, 합을 구해야 하는 tc수 M 입력받기
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // N개의 수 입력받아 배열에 저장
        int[] nums = new int[N+1];
        int[] sums = new int[N+1];    // sums[i]는 1부터 i까지의 합
        st = new StringTokenizer(in.readLine(), " ");
        for(int i = 1; i <= N; i++){
            int tempNum = Integer.parseInt(st.nextToken());
            nums[i] = tempNum;
            sums[i] = sums[i-1] + tempNum;
        }

        // 합을 구해야하는 구간 i, j 입력받아 계산
        for(int x = 0; x < M; x++){
            st = new StringTokenizer(in.readLine(), " ");
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            System.out.println(sums[j]-sums[i-1]);
        }
    }
}
