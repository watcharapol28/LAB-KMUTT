public class Employee{
    private String name;
    private double salary;

    public Employee(String Name, double Salary){
        name = Name;
        salary = Salary;
    }

    public String getName(){return name;}
    public void setName(String name){this.name = name;}
    public double getSalary(){return salary;}
    public void setSalary(double salary){this.salary = salary;}

    @Override
    public String toString(){return " Name is " + name + " Salary is " + salary;}
}