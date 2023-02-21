import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;



public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();

    private static int N, K, R, ans;

    private static boolean[][] visited;
    private static boolean[][][][] road;

    private static ArrayList<Pos> cows;
    private static final int[] dr = {-1, 1, 0, 0};
    private static final int[] dc = {0, 0, -1, 1};

    private static void bfs(Pos pos1) {

        Queue<Pos> queue = new LinkedList<>();
        queue.add(pos1);
        visited[pos1.r][pos1.c] = true;

        while (!queue.isEmpty()) {
            Pos curr = queue.remove();

            for (int i = 0; i < 4; i++) {
                int nr = curr.r + dr[i];
                int nc = curr.c + dc[i];

                if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                    if (road[curr.r][curr.c][nr][nc] || road[nr][nc][curr.r][curr.c]) {
                        continue;
                    }

                    if (!visited[nr][nc]) {
                        queue.add(new Pos(nr, nc));
                        visited[nr][nc] = true;
                    }
                }
            }
        }

    }


    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        cows = new ArrayList<>();
        road = new boolean[N][N][N][N];

        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());

            Pos pos1 = new Pos(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1);
            Pos pos2 = new Pos(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1);

            road[pos1.r][pos1.c][pos2.r][pos2.c] = true;

            road[pos2.r][pos2.c][pos1.r][pos1.c] = true;
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            Pos cow = new Pos(Integer.parseInt(st.nextToken()) - 1, Integer.parseInt(st.nextToken()) - 1);
            cows.add(cow);
        }

        ans = 0;



        for (int i = 0; i < K; i++) {
            Pos cow = cows.get(i);
            visited = new boolean[N][N];
            bfs(cow);
            
            for (int j = i + 1; j < K; j++) {
                Pos cow2 = cows.get(j);
                if (!visited[cow2.r][cow2.c]) {
                    ans ++;
                }
            }
        }

        System.out.println(ans);


    }

    private static class Pos {
        int r;
        int c;

        public Pos(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}