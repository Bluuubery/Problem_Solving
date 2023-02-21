import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static final StringBuilder sb = new StringBuilder();

    private static int T, N, M, ans;
    private static HashSet<String> hashSet;



    public static void main (String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {

            sb.append("#").append(t).append(" ");

            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            hashSet = new HashSet<>();

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                hashSet.add(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            ans = 0;
            for (int i = 0; i < M; i++) {
                if (hashSet.contains(st.nextToken())) {
                    ans ++;
                }
            }

            sb.append(ans).append("\n");

        }
        System.out.println(sb);

    }
}