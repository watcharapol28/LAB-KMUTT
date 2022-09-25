package week3;
import java.util.Scanner;

public class lab3 {
    public static void main(String[] arg)
    {
        System.out.print("Enter temperature(Celsius) : ");
        try (Scanner input = new Scanner(System.in)) {
            double c = input.nextInt();
            System.out.println("Temperature = " + (((9 / 5) * c) + 32) + " Fahrenheit ");
        }
    }
    //Fahrenheit =( 9.0/5.0)*Celsius + 32
}
