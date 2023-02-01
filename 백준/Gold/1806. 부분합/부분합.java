import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] numbers = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0;
        int right = 0;
        int sum_num = numbers[0];
        int min_len = Integer.MAX_VALUE;

        while (true) {
            if (sum_num >= M) {
                sum_num -= numbers[left];
                if (right - left + 1 < min_len) {
                    min_len = right - left + 1;
                }
                left++;
            } else {
                right++;
                if (right == N) {
                    break;
                }
                sum_num += numbers[right];
            }
        }

        if (min_len == Integer.MAX_VALUE) {
            sb.append("0");
        } else {
            sb.append(min_len);
        }

        System.out.println(sb);
        br.close();
    }
}
