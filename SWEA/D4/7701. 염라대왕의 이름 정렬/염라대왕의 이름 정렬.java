import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();


    private static int T, N;

    private static Set<String> set;

    public static void main(String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());
        set = new TreeSet<>(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() != o2.length()) {
                    return o1.length() - o2.length();
                } else {
                    return o1.compareTo(o2);
                }
            }
        });

        for (int t = 1; t <= T; t++) {
            sb.append("#").append(t).append("\n");

            set.clear();

            N = Integer.parseInt(br.readLine());

            for (int i = 0; i <N; i++) {
                set.add(br.readLine());
            }

            for (String s:set) {
                sb.append(s).append("\n");
            }

        }
        System.out.println(sb);

    }


}