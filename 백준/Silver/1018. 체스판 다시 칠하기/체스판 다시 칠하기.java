import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static private BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static private StringTokenizer st;
    static private StringBuilder sb = new StringBuilder();

    static private int N, M, ans;
    static private char[][] board;


//    색 바꿔주기
    static private char switchColor (char color) {

        if (color == 'W') {
            return 'B';
        }
        return 'W';
    }


//    바꿔야 하는 색 개수
    static private int chess(int r, int c) {
        int cnt = 0;

        char color = board[r][c]; // 현재 색

        for (int i = r; i < 8 + r; i++) {
            for (int j = c; j < 8 + c; j++) {

//                다시 칠해야 하는 경우
                if (board[i][j] != color) {
//                    System.out.println("i = " + i + ", j = " + j);
                    cnt ++;
                }

//                다음 칸 넘어가면서 색 바꾸기
                color = switchColor(color);

            }
//            행 바뀔 때 한번 더 바꾸기
            color = switchColor(color);

        }

//        첫 칸의 색이 다를 경우와의 최솟값
        return Math.min(cnt, 64 - cnt);
    }



    public static void main(String[] args) throws IOException {

        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new char[N][M];

        for (int i = 0; i < N; i++) {
            board[i] = br.readLine().toCharArray();
        }

        ans = 64;

        for (int i = 0; i < N - 7; i++) {
            for (int j = 0; j < M - 7; j++) {
//                System.out.println("시작" + "i= " + i + " " +  "j = " + j);
                ans = Math.min(chess(i, j), ans);
//                System.out.println("\n");
            }
        }

        System.out.println(ans);
    }

}