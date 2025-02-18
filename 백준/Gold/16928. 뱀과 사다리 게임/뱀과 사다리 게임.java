import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M;
    static Map<Integer, Integer> ladderOrSnake = new HashMap<Integer, Integer>();
    static int[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());   // 사다리
        M = Integer.parseInt(st.nextToken());   // 뱀

        for (int i = 0; i < N + M; i++) {
            st = new StringTokenizer(br.readLine());
            ladderOrSnake.put(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        visited = new int[101];
        Arrays.fill(visited, -1);
        visited[1] = 0;
        Queue<Integer> queue = new ArrayDeque<Integer>();
        queue.add(1);

        while (!queue.isEmpty()) {
            int now = queue.poll();

            if (now == 100) break;

            for (int i = 1; i <= 6; i++) {
                int nxt = now + i;
                if (nxt > 100) {
                    break;
                }

                if (ladderOrSnake.containsKey(nxt)) {
                    nxt = ladderOrSnake.get(nxt);
                }

                if (visited[nxt] == -1) {
                    visited[nxt] = visited[now] + 1;
                    queue.add(nxt);
                }
            }
        }

        System.out.println(visited[100]);
    }
}
