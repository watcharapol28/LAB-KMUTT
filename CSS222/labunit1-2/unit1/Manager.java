public class Manager extends Employee{
    private String dept;

    public Manager(String Name, double String, String Dept){
        super(Name, String);
        dept = Dept;
    }
    
    public String getDept(){return dept;}
    public void setDept(String dept){this.dept = dept;}

    @Override
    public String toString(){return super.toString() + " Department is " + dept;}
}
