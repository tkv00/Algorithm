import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public  static  int N;
    public  static  int M;
    public static int [][] arr;
    public static boolean [][] check;
    public static int [][] map;
    public  static int res=0;
    public static Queue<int []> q=new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());

        arr=new int[N][M];
        map=new int[N][M];
        map[0][0]=1;

        check=new boolean[N][M];
        for(int i=0;i<N;i++){
            Arrays.fill(check[i],false);
            Arrays.fill(map[i],0);
        }


        for(int i=0;i<N;i++){
            String s=br.readLine();
            for(int j=0;j<M;j++){
                arr[i][j]=s.charAt(j)-'0';
            }
        }
        check[0][0]=true;
        bfs(0,0);
        System.out.println(map[N-1][M-1]+1);

    }
    public static void bfs(int x,int y){
        int [] xy={x,y};
        q.add(xy);
        while(!q.isEmpty()){
            int [] dx={1,0,-1,0};
            int [] dy={0,1,0,-1};

            int now[]=q.poll();
            int ddx=now[0];
            int ddy=now[1];
            for(int i=0;i<4;i++){
                int k=ddx+dx[i];
                int t=ddy+dy[i];
                if(0<=k && k<N && 0<=t &&t<M){
                    if(arr[k][t]==1 && !check[k][t]){
                        q.add(new int[] {k,t});
                        map[k][t]=map[ddx][ddy]+1;
                        check[k][t]=true;

                    }
                }
            }
        }
    }
}
