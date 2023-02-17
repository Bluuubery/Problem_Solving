import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static String string1;
    static String string2;

    static int[][] dp;

    static int T, N, M;

    static int Lcs(String string1, String string2) {
        N = string1.length();
        M = string2.length();
        dp = new int[N + 1][M + 1];

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= M; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (string1.charAt(i - 1) == string2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }


        return dp[N][M];
    }

    public static void main (String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {

            st = new StringTokenizer(br.readLine());
            string1 = st.nextToken();
            string2 = st.nextToken();

            sb.append("#" + t + " " + Lcs(string1, string2) + "\n");
        }

        System.out.println(sb.toString());
    }
}
