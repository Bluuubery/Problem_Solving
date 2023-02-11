import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {

//    입출력
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

//    변수
    private static int T, N, totalCore, maxCore, minCable;
    private static int[][] arr;
    private static int[] dr = {-1, 1, 0, 0};
    private static int[] dc = {0, 0, -1, 1};
    private static List<Core> coreList;

//    코어
    private static class Core {
        int r, c;
        public Core(int r, int c) {
            this.r = r;
            this.c = c;
        }

        @Override
        public String toString () {
            return "Core{" +
                    "r=" + r +
                    ", c=" + c +
                    '}';
        }
    }

//    연결 가능여부
    private static boolean isAvailable(Core core, int d){
        int nr = core.r;
        int nc = core.c;

        // 프로세서에서 시작
        while (true) {
            nr += dr[d];
            nc += dc[d];

            // 연결 성공
            if (nr < 0 || nc < 0 || nr >= N || nc >= N) {
                return true;
            }
            // 연결 실패
            if (arr[nr][nc] >= 1){
                return false;
            }
        }
    }


//    전선 설치
    private static int setCable(Core core, int d, int k) {

        int nr = core.r;
        int nc = core.c;
        int cnt = 0;

        while (true) {
            nr += dr[d];
            nc += dc[d];

            if (nr < 0 || nc < 0 || nr >= N || nc >= N) {
//                System.out.println(core.toString() + d);
//                System.out.println(cnt);
                return cnt;
            }

            arr[nr][nc] = k;
            cnt ++;
        }
    }


    // 백트래킹
    private static void backTracking(int depth, int coreCnt, int cableLen) {

        // 가지치기
        if (totalCore - depth + coreCnt <maxCore) {
            return;
        }


        // 반환조건
        if (depth == totalCore) {
            // 코어, 케이블 갱신
            if (coreCnt > maxCore) {
                maxCore = coreCnt;
                minCable = cableLen;
            }
            // 케이블 갱신
            else if (coreCnt == maxCore) {
                minCable = Math.min(cableLen, minCable);
            }
            return;
        }

//        코어 가져오기
        Core curr = coreList.get(depth);

//        연결 o
        for (int d = 0; d < 4; d++) {
//            해당 방향으로 연결이 가능할 경우
            if (isAvailable(curr, d)){
//                전선 설치
                int cnt = setCable(curr, d, 2);
//                재귀적으로 탐색
                backTracking(depth + 1, coreCnt + 1, cableLen + cnt);
//                백트래킹
                setCable(curr, d, 0);
            }
        }

//        연결 x
        backTracking(depth + 1, coreCnt, cableLen);

    }

    public static void main (String[] args) throws IOException {
//        테스트 케이스
        T = Integer.parseInt(br.readLine());

        for (int t = 1; t <= T; t++) {
//            변수 초기화
           N = Integer.parseInt(br.readLine());
           arr = new int[N][N];
           coreList = new ArrayList<>();
           totalCore = 0;

            for (int r = 0; r < N; r++) {
                st = new StringTokenizer(br.readLine());
                for (int c = 0; c < N; c++) {
//                    프로세서 및 코어 입력
                    arr[r][c] = Integer.parseInt(st.nextToken());

                    if (arr[r][c] == 1) {

                        coreList.add(new Core(r, c));
                    }

                    }
                }

//            변수 초기화
            maxCore = 0;
            minCable = Integer.MAX_VALUE;
            totalCore = coreList.size();

//            백트래킹
            backTracking(0, 0, 0);
            
            sb.append("#" + t + " "  + minCable + "\n");

            }
            System.out.println(sb.toString());
        }

    }