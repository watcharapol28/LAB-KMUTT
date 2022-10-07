abstract public class Worker {
    private String name;
    private double salary_rate;

    public Worker(String Name, double Salary){
        name = Name;
        salary_rate = Salary;
    }

    public String getName(){return name;}
    public void setName(String name){this.name = name;}
    public double getSalaryrate(){return salary_rate;}
    public void setSalaryrate(double salary_rate){this.salary_rate = salary_rate;}

    @Override    
    public String toString(){return "Name is " + name;}
    abstract public double computePay();
}
