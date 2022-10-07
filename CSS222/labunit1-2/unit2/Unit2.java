public class Unit2 {
    public static void main(String[] args){
        FullTimeWorker p1 = new FullTimeWorker(null, 0, 0);
        p1.setName("Sangonomiya");
        p1.setSalaryrate(1000);
        p1.setHourWorked(200);
        System.out.println();
        System.out.println(p1 + ((p1.getHourWorked()<=240)?" Salary is " + p1.computePay():" Can't compute"));

        HourlyWorker p2 = new HourlyWorker(null, 0, 0);
        p2.setName("Yoimiya");
        p2.setSalaryrate(500);
        p2.setHourWorked(60);
        System.out.println(p2 + ((p2.getHourWorked()<=60) ? " Salary is " + p2.computePay() : " Can't compute"));
        System.out.println();
    }
}
