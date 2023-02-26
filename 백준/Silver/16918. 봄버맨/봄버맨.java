import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;

    private static int R, C, N;
    private static char[][] ans;
    private static int[][] timeArr;

    private static final int[] dr = {-1, 1, 0, 0};
    private static final int[] dc = {0, 0, -1, 1};

    private static void boom() {


        List <int[]> boomList = new ArrayList<>();

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (timeArr[r][c] == 0) {
                    boomList.add(new int[]{r, c});
                }
            }
        }
        
        for (int[] bomb : boomList) {
            int r = bomb[0];
            int c = bomb[1];

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (0 <= nr && nr < R && 0 <= nc && nc < C) {
                    timeArr[nr][nc] = 0;
                }
            }
        }

    }

    private static void setBomb() {

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (timeArr[r][c] == -1) {
                    timeArr[r][c] = 3;
                }
            }
        }

    }

    public static void main (String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        timeArr = new int[R][C];

        for (int i = 0; i < R; i++) {
            String input = br.readLine();
            for (int j = 0; j < C; j++) {
                if (input.charAt(j) == '.') {
                    timeArr[i][j] = 0;
                } else {
                    timeArr[i][j] = 2;
                }
            }
        }

        for (int i = 1; i < N; i++) {

            for (int r = 0; r < R; r++) {
                for (int c = 0; c < C; c++) {
                    timeArr[r][c] --;
                }
            }

            if (i % 2 == 1) {
                setBomb();
            } else {
                boom();
            }
        }


        ans = new char[R][C];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (timeArr[r][c] > 0) {
                    ans[r][c] = 'O';
                } else {
                    ans[r][c] = '.';
                }
                sb.append(ans[r][c]);
            }
            sb.append("\n");
        }

//        for (int[] row : timeArr) {
//            System.out.println(Arrays.toString(row));
//        }

        System.out.println(sb);

    }


}