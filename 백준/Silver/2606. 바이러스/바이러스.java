import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public  static  int n;
    public  static  int m;
    public  static int[][] arr;
    public static  boolean [] visit;


    public static int res=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));


        n=Integer.parseInt(br.readLine());
        m=Integer.parseInt(br.readLine());

        arr=new int[n+1][n+1];
        visit=new boolean[n+1];

        for(int i=0;i<m;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int x=Integer.parseInt(st.nextToken());
            int y=Integer.parseInt(st.nextToken());
            arr[x][y]=arr[y][x]=1;

        }

        dfs(1);
        System.out.println(res-1);

    }

    public static void dfs(int v){
        visit[v]=true;
        res+=1;
        for(int i=2;i<=n;i++){
            if(!visit[i] && arr[v][i]==1){
                dfs(i);
            }
        }
    }
}
