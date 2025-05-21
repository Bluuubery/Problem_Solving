import java.util.*;

class Solution {
		
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        
		int[] capability = new int[24];
        
        for (int i=0; i < players.length; i++) {
			
			// 사용자 수가 기본 할당량(m)이상이며 현재 가용량보다 적을 경우
            if (players[i] >= m && players[i] > capability[i]){
                
				// 서버 증설 개수
				int addedServer = (players[i] - capability[i]) / m;
                answer += addedServer;
                
				// 지속 시간(k)만큼 증설 유지
				for(int j=0; j<k; j++){
                    // out of index 방지
                    if ((j + i) >= players.length) break;
                    
					capability[j + i] += addedServer * m;
				}
                // System.out.println(i + ": add " + addedServer );
			}
            	// System.out.println(i + ": " + Arrays.toString(capability));

            
        }
        
        return answer;
    }
}