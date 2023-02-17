import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    //    입출력
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static int T, N, K;

    static int[] volume;
    static int[] price;

    static int knapsack(int N, int K, int[] volume, int[] price){
        int[][] dp = new int[N + 1][K + 1];

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= K; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (volume[i - 1] <= j) {
                    dp[i][j] = Math.max(price[i - 1] + dp[i - 1][j - volume[i - 1]], dp[i - 1][j]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[N][K];
    }

    public static void main (String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {

            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            volume = new int[N];
            price = new int[N];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                volume[i] = Integer.parseInt(st.nextToken());
                price[i] = Integer.parseInt(st.nextToken());
            }

            sb.append("#" + t + " " + knapsack(N, K, volume, price) + "\n");

        }

        System.out.println(sb.toString());

    }
}


