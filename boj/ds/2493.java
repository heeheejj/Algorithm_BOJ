package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main_2493_탑_정희주 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(in.readLine());

        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        int[] height = new int[N];
        Stack<Integer> stack = new Stack<>();   // 기둥의 번호를 담는 스택
        for(int i = 0; i < N; i++){
            int curHeight = Integer.parseInt(st.nextToken());
            height[i] = curHeight;
            while(!stack.isEmpty() && height[stack.peek()] < curHeight){
//                stack의 마지막 원소를 인덱스값으로 하는 기둥의 높이가 현재 idx의 기둥의 높이보다 더 큰게 나올때까지
//                (문제에서 서로 다른 높이 -> 같은 높이는 없음) stack에서 pop하면서 확인
                stack.pop();
            }
            if(!stack.isEmpty()){   // 스택이 비어있지 않다면 peek해서 +1을 해주고 출력
                sb.append(stack.peek()+1);
            }else{  // 스택이 비어있다면 레이저 신호를 수신하는 탑이 존재하지 않음 -> 0 출력
                sb.append(0);
            }
            sb.append(" ");
            stack.add(i);   // 기둥의 idx를 stack에 push
        }
        System.out.println(sb);
    }
}
