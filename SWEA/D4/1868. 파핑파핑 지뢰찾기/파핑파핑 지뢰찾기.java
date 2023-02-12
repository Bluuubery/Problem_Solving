import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {

//    입출력
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static final StringBuilder sb = new StringBuilder();

//    변수 선언
    private static int T, N, ans;
    private static char[][] arr;
    private static boolean[][] visited;
    private static final int[] dr = {-1, 1, 0, 0, -1, 1, 1, -1};
    private static final int[] dc = {0, 0, -1, 1, 1, -1, 1, -1};

    private static class Node{
        int r;
        int c;

        public Node(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }


//    bfs로 클릭 
    private static void bfs (int r, int c) {

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(r, c));
        visited[r][c] = true;

        while (!queue.isEmpty()) {
            Node node = queue.remove();

//            주변에 지뢰가 없는 경우에만 진행
            if (!checkSafe(node.r, node.c)) {
                continue;
            }

            for (int i = 0; i < 8; i++) {

                int nr = node.r + dr[i];
                int nc = node.c + dc[i];

                if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                    if (!visited[nr][nc]) {
                        visited[nr][nc] = true;
                        queue.add(new Node(nr, nc));
                    }
                }
            }
        }
    }


//    주변에 지뢰 있는지 없는지 확인
    public static boolean checkSafe(int r, int c) {

        for (int i = 0; i < 8; i++) {

            int nr = r + dr[i];
            int nc = c + dc[i];

            if (0 <= nr && nr < N && 0 <= nc && nc < N) {
                if (arr[nr][nc] == '*') {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {

//            변수 초기화
            N = Integer.parseInt(br.readLine());
            arr = new char [N][N];
            visited = new boolean[N][N];
            ans = 0;

//            입력
            for (int i = 0; i < N; i++) {
                arr[i] = br.readLine().toCharArray();
            }


//            지뢰 여부 파악 후 주변에 지뢰 없는 곳만 먼저 클릭
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    
//                    지뢰 있을 경우 방문처리
                    if (arr[i][j] == '*') {
                        visited[i][j] = true;
                    }
                    
//                    지뢰 없고 미방문일 경우
                    else if (!visited[i][j] && arr[i][j] == '.') {
//                        주변에 지뢰 없을 경우
                        if (checkSafe(i, j)) {
//                            클릭
                            bfs(i, j);
                            ans ++;
                        }

                    }
                }
            }

//            남은 곳들 방문 처리 후 세주기
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (!visited[i][j]) {
                        ans ++;
                    }
                }
            }

            sb.append("#" + t + " " + ans + "\n");



        }
        System.out.println(sb);

    }

}