package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main_11286_절댓값힙_정희주 {

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(in.readLine());

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> (a[1]==b[1]?a[0]-b[0]:a[1]-b[1]));
        // 절댓값을 기준으로 비교를 한다. 단, 절댓값이 같은 경우에는 그 수 자체를 비교해서 자리를 바꿔준다.
        for(int n = 0; n < N; n++){
            int temp = Integer.parseInt(in.readLine());
            if(temp != 0){  // x가 0이 아니라면 배열에 x라는 값을 추가한다.
                if(temp > 0){
                    minHeap.add(new int[]{temp, temp});
                } else {
                    minHeap.add(new int[]{temp, -1*temp});
                }
            } else {
                if(minHeap.isEmpty()){
                    sb.append(0).append("\n");
                }else{
                    int[] result = minHeap.poll();
                    sb.append(result[0]).append("\n");
                }
            }
        }
        System.out.println(sb);
    }
}
