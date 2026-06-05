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
 
        int nextInt() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ');
 
            int val = 0;
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val;
        }
    }
 
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        StringBuilder out = new StringBuilder();
 
        int t = fs.nextInt();
 
        while (t-- > 0) {
            int n = fs.nextInt();
            int k = fs.nextInt();
 
            for (int i = 0; i < k; i++) fs.nextInt(); // capacities not needed
 
            int[] b = new int[n];
            for (int i = 0; i < n; i++) {
                b[i] = fs.nextInt();
            }
 
            ArrayList<Integer> ops = new ArrayList<>();
 
            for (int level = k; level >= 1; level--) {
                for (int i = 0; i < n; i++) {
                    if (b[i] == level) {
                        while (b[i] < k + 1) {
                            ops.add(i + 1);
                            b[i]++;
                        }
                    }
                }
            }
 
            out.append(ops.size()).append('
');
 
            if (!ops.isEmpty()) {
                for (int i = 0; i < ops.size(); i++) {
                    if (i > 0) out.append(' ');
                    out.append(ops.get(i));
                }
            }
            out.append('
');
        }
 
        System.out.print(out);
    }
}