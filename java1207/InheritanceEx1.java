package java1207;

public class InheritanceEx1 {
    public static void main(String[] args) {
        Worker worker = new Worker();
        Student student = new Student();
        worker.setAge(30);
        worker.setSleep(6);
        worker.setWorkTime(8);
        worker.WorkerInfo();

        student.setAge(17);
        student.setSleep(9);
        student.setStudyType();
        student.StudentInfo();
    }
}
