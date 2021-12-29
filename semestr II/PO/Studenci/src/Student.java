public abstract class Student {
    String name;
    String surname;
    String index;

    public Student() {
    }

    public Student(String index) {
        this.index = index;
    }

    public String getIndex() {
        return index;
    }

    public  void setIndex(String Index){
        this.index = index;
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getSurname(){
        return surname;
    }

    public void setSurname(String surname){
        this.surname = surname;
    }


}
