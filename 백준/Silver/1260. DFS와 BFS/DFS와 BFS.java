import java.io.*;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public  static  int n;
    public  static  int m;
    public  static boolean [] visited;
    public static int [][] arr;
    public  static  StringBuilder res=new StringBuilder();
    public static Queue<Integer> q=new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st=new StringTokenizer(br.readLine());

        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        int v=Integer.parseInt(st.nextToken());

        arr=new int[n+1][n+1];
        visited=new boolean[n+1];

        for(int i=0;i<m;i++){
            st=new StringTokenizer(br.readLine());
            int x=Integer.parseInt(st.nextToken());
            int y=Integer.parseInt(st.nextToken());

            arr[x][y]=arr[y][x]=1;
        }

        dfs(v);
        Arrays.fill(visited,false);
        bfs(v);
        System.out.println(res);



    }
    public  static void dfs(int v){
        visited[v]=true;
        res.append(v).append(" ");
        for(int i=1;i<=n;i++){
            if(arr[v][i]==1 && !visited[i]){
                dfs(i);
            }
        }
    }

    public static void bfs(int v){
        q.add(v);
        visited[v]=true;
        res.append('\n').append(v).append(" ");
        while (!q.isEmpty()){
            int idx=q.poll();
            for(int i=1;i<=n;i++){
                if(arr[idx][i]==1 && !visited[i]){
                    q.add(i);
                    visited[i]=true;
                    res.append(i).append(" ");
                }
            }
        }
    }

}