package week3;

public class lab1 {
    public static void main(String[] arg){
        
        System.out.println("Welcome to OOP Programming"); //1.1
        System.out.println();
        
        short shorter = 32766; //1.2
        int intiger = 2147483646;
        long longer = 9223372036854775807L;
        float floater =  3402823.5f;
        double doubles = 1.7976931348623157e+30;
        char character = 'a';
        String string = "String";
        boolean bool = true;
        System.out.println("short \t= " + shorter);
        System.out.println("int \t= " + intiger);
        System.out.println("long\t= " + longer);
        System.out.println("float\t= " + floater);
        System.out.println("double\t= " + doubles);
        System.out.println("char\t= " + character);
        System.out.println("String\t= " + string);
        System.out.println("boolean\t= " + bool);
        System.out.println();

        String str1 = "Dota2", str2 = "Dota3"; //1.3
        if(str1.equals(str2))
            System.out.println("Strings are equal");
        else
            System.out.println("Strings are not equal");
        System.out.println();
    }
}
