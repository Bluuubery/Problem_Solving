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

    private static HashSet<String> hashSet;

    public static void main(String[] args) throws IOException {

        T = Integer.parseInt(br.readLine());
        hashSet = new HashSet<>();

        for (int t = 1; t <= T; t++) {
            sb.append("#").append(t).append("\n");

            hashSet.clear();

            N = Integer.parseInt(br.readLine());

            for (int i = 0; i <N; i++) {
                hashSet.add(br.readLine());
            }

//            String[] strings = hashSet.toArray(new String[0]);
//
//            Arrays.sort(strings, new Comparator<String>() {
//                @Override
//                public int compare(String o1, String o2) {
//                    if (o1.length() != o2.length()) {
//                        return o1.length() - o2.length();
//                    } else {
//                        return o1.compareTo(o2);
//                    }
//                }
//            });
//
//            for (String s :
//                    strings) {
//             sb.append(s + "\n") ;
//            }

            hashSet.stream()
                    .sorted(new Comparator<String>() {
                        @Override
                        public int compare(String o1, String o2) {
                            if (o1.length() != o2.length()) {
                                return o1.length() - o2.length();
                            } else {
                                return o1.compareTo(o2);
                            }
                        }
                    })
                    .map(s -> s + "\n")
                    .forEach(sb::append);
        }
        System.out.println(sb);

    }


}