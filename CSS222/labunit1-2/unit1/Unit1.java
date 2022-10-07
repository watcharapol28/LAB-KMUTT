public class Unit1{
    public static void main(String[] args){
        Manager p1 = new Manager(null, 0, null);
        p1.setName("Yoimiya");
        p1.setSalary(30000);
        p1.setDept("Fireworks maker");
        System.out.println();
        System.out.println(p1);
        Employee p2 = new Employee(null, 0);
        p2.setName("Sangonomiya");
        p2.setSalary(200000);
        System.out.println(p2);
        System.out.println();
    }
}