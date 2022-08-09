package heeheejj.boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 슬라이딩 윈도우 적용 (배열)
// ACGT 문자랑 각 문자 개수 Map으로해서 한번해보고싶당
public class Main_12891_DNA비밀번호_정희주 {

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("./input.txt"));
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine(), " ");
        int S = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
        char[] tempDNA = in.readLine().toCharArray();

        // 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수 입력받아 저장
        st = new StringTokenizer(in.readLine(), " ");
        int[] minCnts = new int[4];
        for (int i = 0; i < 4; i++){
            minCnts[i] = Integer.parseInt(st.nextToken());
        }

        int result = 0;
        int[] tempCnts = new int[]{0, 0, 0, 0};
        for(int i = 0; i < S; i++){
            char temp = tempDNA[i];
            if(temp == 'A'){
                tempCnts[0]++;
            } else if(temp == 'C'){
                tempCnts[1]++;
            } else if(temp == 'G'){
                tempCnts[2]++;
            } else if(temp == 'T'){
                tempCnts[3]++;
            }

            if(i < P-1){    // i가 0부터 P-2까지는 tempCnt의 초기값을 세팅해주기만 한다.
                continue;
            } else if(i > P-1){ // i가 P이상부터는 맨앞 원소를 빼줘야함
                char tempFirst = tempDNA[i-P];
                if(tempFirst == 'A'){
                    tempCnts[0]--;
                } else if(tempFirst == 'C'){
                    tempCnts[1]--;
                } else if(tempFirst == 'G'){
                    tempCnts[2]--;
                } else if(tempFirst == 'T'){
                    tempCnts[3]--;
                }
            }   // 나머지 i == P-1일때는 pass

            boolean isValid = true;
            for(int j = 0; j < 4; j++){
                int minCnt = minCnts[j];
                if(minCnt > tempCnts[j]){
                    isValid = false;
                    break;
                }
            }
            if(isValid){
                result++;
            }
        }
        System.out.println(result);
    }
}
