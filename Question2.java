import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;
import java.util.HashMap;
import java.util.Map;


public class Main{

    public static void main(String[] args) {

       // int coins[] = {1,3,2,4};
        System.out.println("Result: " +

                decode("2[b3[a]]"));




    }

    public static String decode(String s) {
        StringBuilder res = new StringBuilder();
        Stack<StringBuilder> resStack = new Stack<>();
        Stack<Integer> countStack = new Stack<>();
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                int count = 0;
                while (Character.isDigit(s.charAt(i)))
                    count = count * 10 + s.charAt(i++) - '0';
                countStack.push(count);
            } else if (c == '[') {
                resStack.push(new StringBuilder(res)); // important
                res.setLength(0);
                i++;
            } else if (c == ']') {
                StringBuilder temp = resStack.pop();
                int count = countStack.pop();
                while (count-- > 0)
                    temp.append(res.toString());
                res = temp;
                i++;
            } else
                res.append(s.charAt(i++));
        }
        return res.toString();
    }









}


