public class FullTimeWorker extends Worker {
    private int hour_Worked;

    public FullTimeWorker(String Name, double Salary,int Hour) {
        super(Name, Salary);
        Hour = hour_Worked;
    }

    public int getHourWorked(){return hour_Worked;}
    public void setHourWorked(int hour_Worked) {this.hour_Worked = hour_Worked;}

    @Override    
    public String toString(){return super.toString();}

    @Override
    public double computePay() {
        return getSalaryrate() * hour_Worked;
    }
}
