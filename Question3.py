import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.*;
import java.util.HashMap;
import java.util.Map;


public class Main{

    public static void main(String[] args) {

        int coins[] = {1,3,2,4};
        System.out.println("Result: " +

                possibilities(4, coins));




    }

    public static int possibilities(int sum, int[] coins)
    {
        int solution = 0;

        // This solution is recursive, we handle the base-case here:
        // if the total amount of change is zero, there is just one possible
        // way to resolve it, the empty set!
        if (sum == 0)
        {
            return 1;
        }

        for (int i = 0; i < coins.length; i++)
        {
            int currentCoin = coins[i];

            if (currentCoin > sum)
            {
                continue;
            }

            // Here is where we make the recursive call, we take our
            // current coin and subtract it from the total, and then
            // find the number of solutions for whatever is left.
            //
            // For example, if the call was (10, [5, 3, 1]), the
            // first time through this loop, the recursive call will
            // be (5, [5, 3, 1]).
            //
            // Using a subset of the array in subsequent interations of
            // loop is a bit subtle, but it's how we avoid counting
            // duplicate solutions. Using our example above, after the
            // recursive call to (5, [5, 3, 1]) we've counted every single
            // solution that uses the five cent coin. The only solutions
            // left are those that exclusively use some combination of three
            // and one cent coins. So, the second time through the loop, the
            // recursive call is (7, [3, 1]), and the last time through the
            // loop the recursive call is (9, [1]).
            solution += possibilities(sum - currentCoin,
                    Arrays.copyOfRange(coins, i, coins.length));
        }

        return solution;
    }









}
