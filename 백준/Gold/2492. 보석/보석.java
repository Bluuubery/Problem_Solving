import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());	// 열
		int M = Integer.parseInt(st.nextToken());	// 행
		int T = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		Pos[] p = new Pos[T];
		for (int i = 0; i < T; i++) {
			st = new StringTokenizer(br.readLine() ," ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			p[i] = new Pos(x, y);
		} // end of input
		
		Arrays.sort(p);
		
		int resultR = 0;
		int resultC = 0;
		int result = 0;
		
		for (int t = 0; t < T; t++) {
			
			for (int col = p[t].x - K; col <= p[t].x; col++) {
				
				if(N < col + K) break;
				if(col < 0) continue;
				
				int row = p[t].y - K < 0 ? K : p[t].y;
				int cnt = 0;
				
				for (int next = t; next < T; next++) {
					
					if(p[next].y < row - K) break;
					if(col <= p[next].x && p[next].x <= col + K) cnt++;
					
				}
				
				if(result < cnt) {
					
					resultR = row;
					resultC = col;
					result = cnt;
					
				}
				
			}
				
		}
		
		sb.append(resultC).append(" ").append(resultR).append("\n").append(result);
		System.out.print(sb.toString());
		
	}
	
	static class Pos implements Comparable<Pos> {
		
		int x, y;

		public Pos(int x, int y) {

			this.x = x;
			this.y = y;
			
		}

		@Override
		public int compareTo(Pos o) {

			return o.y - this.y;
			
		}
		
	}
	
}