
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author wilso
 */
public class daisychainsdec2020 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int[] ref = new int[N];
        for (int i = 0; i < N; i++) {
            ref[i] = scan.nextInt();
        }
//        System.out.println(Arrays.toString(ref));
        int ret = 0;
        for (int x = 1; x <= ref.length; x++) {
            
            ret += run(ref, x);
//            System.out.println(x + " " + ret);
            
        }
        System.out.println(ret);
        
    }
    public static int run(int[] ref, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        for (int i = 0; i < k; i++) {
            map.put(ref[i], map.getOrDefault(ref[i], 0)+1);
            sum += ref[i];
        }
        int ret = 0;
        if (sum % k == 0 && map.containsKey(sum / k)) ret++;
        int l = 0;
        int r = k;
        
        while (r < ref.length) {
            int left = ref[l];
            map.put(left, map.get(left)-1);
            if (map.get(left) == 0) {
                map.remove(left);
            }
            sum -= left;
            sum += ref[r];
            map.put(ref[r], map.getOrDefault(ref[r], 0)+1);
            
            if (sum % k == 0 && map.containsKey(sum / k)) ret++;
            
            l++;
            r++;
        }
        return ret;
    }
}
