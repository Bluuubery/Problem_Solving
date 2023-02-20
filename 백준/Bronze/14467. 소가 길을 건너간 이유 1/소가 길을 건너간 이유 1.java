import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();

    private static int N, cow, status, ans;
    private static HashMap<Integer, Integer> cross = new HashMap<>();

    public static void main (String[] args) throws IOException {

        N = Integer.parseInt(br.readLine());
        ans = 0;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            cow = Integer.parseInt(st.nextToken());
            status = Integer.parseInt(st.nextToken());

            if (cross.containsKey(cow))
                if (cross.get(cow) != status)
                    ans++;

            cross.put(cow, status);
        }

        System.out.println(ans);

    }
}