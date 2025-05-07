class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
		
		// 이분탐색 변수 선언
		int left = 1;
        int right = 100000;
        int mid;
        int answer = right;
		
        // 이분탐색
        while (left <= right) {

            mid = (left + right) / 2;

            if (check(diffs, times, limit, mid)) {
                // 시간 내에 풀 수 있음 -> 숙련도 내림
                answer = mid;
                right = mid  - 1;
            } else {
                // 시간 내에 못 품 -> 숙련도 올림
                left = mid + 1;
            }
        }
			
        return answer;
    }

    // 시간 내에 풀 수 있는지지
    private boolean check(int[] diffs, int[] times, long limit, int level) {

        // 변수 선언
        long totalTime = 0;
        int retry, timeCur, timePrev;

        for (int i = 0; i < diffs.length; i++) {
            retry = diffs[i] - level;
            timeCur = times[i];
            timePrev = (i == 0) ? 0 : times[i - 1];

            if (retry > 0) {
                totalTime += retry * (timeCur + timePrev);
            }
            totalTime += timeCur;

            if (totalTime > limit) {
                return false;
            }
        }

        return true;


    }
}