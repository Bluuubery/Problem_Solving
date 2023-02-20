import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int T, N, mid, X, Y, ans;
    static final int MOD = 20171109;
    static PriorityQueue<Integer> pqMax, pqMin;


    public static void main(String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());
        pqMin = new PriorityQueue<>();
        pqMax = new PriorityQueue<>(Collections.reverseOrder());

        for (int t = 1; t <= T; t++) {

            sb.append("#").append(t).append(" ");
            st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            mid = Integer.parseInt(st.nextToken()); // 현재 중앙값
            ans = 0;

            pqMax.clear();
            pqMin.clear();

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());

                X = Integer.parseInt(st.nextToken());
                Y = Integer.parseInt(st.nextToken());

                boolean addX = X > mid ? pqMin.add(X) : pqMax.add(X);
                boolean addY = Y > mid ? pqMin.add(Y) : pqMax.add(Y);

                if (pqMax.size() > pqMin.size()) {
                    pqMin.add(mid);
                    mid = pqMax.remove();
                } else if (pqMax.size() < pqMin.size()) {
                    pqMax.add(mid);
                    mid = pqMin.remove();
                }

                ans = (ans + mid) % MOD;
//                System.out.println("pqMax: " + pqMax.toString());
//                System.out.println("pqMin: " + pqMin.toString());
//                System.out.println(mid);

            }
            sb.append(ans).append("\n");


        }
        System.out.println(sb.toString());

    }
}
