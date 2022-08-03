import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1929_소수구하기_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        // 에라토스체네스의 체
        boolean[] sieve = new boolean[N+1];
        Arrays.fill(sieve, true);
        sieve[0] = false;
        sieve[1] = false;
        for(int i = 2; i <= N; i++){
            if(sieve[i]) {    // sieve[i]가 true이면
                if(i >= M){
                    System.out.println(i);
                }
                for(int j = i*2; j <= N; j += i){
                    sieve[j] = false;
                }
            }
        }
    }
}
