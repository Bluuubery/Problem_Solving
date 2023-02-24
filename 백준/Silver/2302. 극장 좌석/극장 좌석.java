import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static private StringTokenizer st;
    static private final StringBuilder sb = new StringBuilder();

    static private int N, M;
    static private final int[] dp = new int[41];
    static private Set<Integer> set;


    public static void main(String[] args) throws IOException {

        N = Integer.parseInt(br.readLine());
        M = Integer.parseInt(br.readLine());
        
        set = new HashSet<>();

        for (int i = 0; i < M; i++) {
            set.add(Integer.parseInt(br.readLine()));
        }

        dp[0] = 1; dp[1] = 1;

        for (int i = 0; i <= N; i++) {
            if (i == 0 || i == 1) {
                continue;
            }

            if (set.contains(i) || set.contains(i - 1)) {
                dp[i] = dp[i - 1];
            } else {
                dp[i] = dp[i - 1] + dp[i - 2];
            }

        }
//        System.out.println(Arrays.toString(dp));
        System.out.println(dp[N]);

    }
}