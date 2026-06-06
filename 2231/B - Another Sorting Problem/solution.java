import java.io.*;
import java.util.*;
 
public class Main {
 
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
 
        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }
 
        long nextLong() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ');
 
            long sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
 
            long val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
 
        int nextInt() throws IOException {
            return (int) nextLong();
        }
    }
 
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        StringBuilder out = new StringBuilder();
 
        int T = fs.nextInt();
 
        while (T-- > 0) {
            int n = fs.nextInt();
            long[] a = new long[n];
 
            for (int i = 0; i < n; i++) {
                a[i] = fs.nextLong();
            }
 
            long L = 1;
            int[] forced = new int[n];
            Arrays.fill(forced, -1);
 
            boolean ok = true;
 
            for (int i = 0; i < n - 1; i++) {
                if (a[i] > a[i + 1]) {
                    L = Math.max(L, a[i] - a[i + 1]);
 
                    if (forced[i] == 1 || forced[i + 1] == 0) {
                        ok = false;
                        break;
                    }
 
                    forced[i] = 0;
                    forced[i + 1] = 1;
                }
            }
 
            if (!ok) {
                out.append("NO
");
                continue;
            }
 
            boolean[] tight = new boolean[n - 1];
 
            for (int i = 0; i < n - 1; i++) {
                if (a[i] <= a[i + 1] && a[i + 1] - a[i] < L) {
                    tight[i] = true;
                }
            }
 
            boolean[] mustOne = new boolean[n];
            boolean[] mustZero = new boolean[n];
 
            for (int i = 0; i < n; i++) {
                if (forced[i] == 1) mustOne[i] = true;
                if (forced[i] == 0) mustZero[i] = true;
            }
 
            for (int i = 0; i < n - 1; i++) {
                if (tight[i] && mustOne[i]) {
                    mustOne[i + 1] = true;
                }
            }
 
            for (int i = n - 2; i >= 0; i--) {
                if (tight[i] && mustZero[i + 1]) {
                    mustZero[i] = true;
                }
            }
 
            for (int i = 0; i < n; i++) {
                if (mustOne[i] && mustZero[i]) {
                    ok = false;
                    break;
                }
            }
 
            out.append(ok ? "YES
" : "NO
");
        }
 
        System.out.print(out);
    }
}