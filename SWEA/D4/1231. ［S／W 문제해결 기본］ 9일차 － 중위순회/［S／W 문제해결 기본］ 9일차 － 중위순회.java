import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();

    static StringTokenizer st;
    static int T = 10;
    static int N;
    static String[] tree;

    public static void inOrder(int node) {
        if (node <= N) {
            inOrder(node * 2);
            sb.append(tree[node]);
            inOrder(node * 2 + 1);
        }
    }



    public static void main (String[] args) throws IOException {

        for (int t = 1; t <= T; t++) {
            N = Integer.parseInt(br.readLine());
            tree = new String[N + 1];

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                tree[Integer.parseInt(st.nextToken())] = st.nextToken();
            }

            sb.append("#" + t + " ");
            inOrder(1);
            sb.append('\n');
        }
        System.out.println(sb);
    }
}