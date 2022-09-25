package week3;
import java.util.Arrays;
public class lab2 {
    public static void main(String[] arg)
    {
        l21(arg);
        System.out.println();
        l22(arg);
        System.out.println();
        l23(arg);
        System.out.println();
        l24(arg);
        System.out.println();
        l25(arg);
    }

    public static void l21(String[] arg){
        int x = 0; 
        System.out.println("\nUnit 2.1.1");
        System.out.println("x = " + ++x); //2.1.1
        x = x % 3 + 2; //2.1.2
        System.out.println("\nUnit 2.1.2");
        System.out.println("x = " + x); 
        System.out.println("\nUnit 2.1.3");
        if(x > 3)
            System.out.println("x > 3"); //2.1.3
        else
            System.out.println("x <= 3"); 
        System.out.println("\nUnit 2.1.4");
        String str = (x > 3) ? "String showed x > 3":"String showed x <= 3";
        System.out.println(str);//2.1.4
    }

    public static void l22(String[] arg)
    {
        int day = 10;
        System.out.println("\nUnit 2.2.1");
        if(day > 7){
            System.out.println("Days > 7"); //2.2.1
            day %= 7;
        }
        else
            System.out.println("Days <= 7");
        System.out.println();
        System.out.println("\nUnit 2.2.2");
        switch (day) 
        { //2.2.2
            case 1:
                System.out.println("Monday");
                break;
            case 2:
                System.out.println("Tuesday");
                break;
            case 3:
                System.out.println("Wednesday");
                break;
            case 4:
                System.out.println("Thursday");
                break;
            case 5:
                System.out.println("Friday");
                break;
            case 6:
                System.out.println("Saturday");
                break;
            case 7:
                System.out.println("Sunday");
                break;
        }
        System.out.println();
        int x = 0;
        System.out.println("\nUnit 2.2.3");
        for(int i = 0; i < day; i++)//2.2.3
        {
            System.out.println("for : " + x++);
        }
        System.out.println();
        System.out.println("\nUnit 2.2.4");
        while(x > 0)//2.2.4
        {
            x--;
            System.out.println("While(" + x + " > 0)");
        }
        System.out.println();
        System.out.println("\nUnit 2.2.5");
        do //2.2.5
        {
            System.out.println("While(" + x + ") < 5");
            x++;
        }while(x < 5);
        System.out.println();
    }

    public static void l23(String[] arg)
    {
        System.out.println("\nUnit 2.3.1");
        int[] a1 = new int[10];  //2.3.1
        int[] a2 = {3, 5, 7, 1, 8, 99, 44, -10 }; 
        int[] a3 = {4, 3, 2, 1};
        System.out.println("size of a1 : "+ a1.length);
        System.out.println("size of a2 : "+ a2.length);
        System.out.println("size of a3 : "+ a3.length);

        int[][] a4 = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}}; //2.3.2
        System.out.println("\nUnit 2.3.2");
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 3; j++)
            {
                System.out.print(a4[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void l24(String[] arg)
    {
        System.out.println("\nUnit 2.4");
        int[] arr = {234,6,846,85,96,198,545,12,60,34,4,87,7,1};
        Arrays.sort(arr); //import java.util.Arrays; //2.4
        System.out.println("Sorted arr : ");
        for(int i = 0; i < arr.length; i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static void l25(String[] arg)
    {
        System.out.println("\nUnit 2.5.1");
        int[][]a = { {4,7,9,8,3},{2,4,7,8,1},{1,1,8,1,2},{0,0,1,0,4}};
        int[][]b = { {1,2,8,4,3},{4,1,8,3,1},{2,1,0,0,5},{1,2,1,1,7}};
        int[][]add = new int[5][6];
        System.out.println("Addition : ");//2.5.1
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 5; j++)
            {
                add[i][j] = a[i][j] + b[i][j];
                System.out.print(add[i][j] + "\t");
            }
            System.out.println();
        }

        System.out.println("\nUnit 2.5.2");
        int[][]aa ={{1,2,3},{4,5,6},{2,3,4}};
        int[][]bb ={{1,2,3},{4,5,6},{2,3,4}};
        int[][]mul = new int[4][4];
        System.out.println("Multiplication : ");//2.5.2
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 3; j++)
            {
                int sum = 0;
                for(int k = 0; k < 3; k++)
                {
                    sum += aa[i][k] * bb[k][j];
                }
                mul[i][j] = sum;
                System.out.print(mul[i][j] + "\t");
            }
            System.out.println();
        }


    }
}
