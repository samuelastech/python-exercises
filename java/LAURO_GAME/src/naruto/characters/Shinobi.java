package naruto.characters;

public class Shinobi {
    // Personal Data
    String name, affiliation;
    char gender;
    int age;

    // Jutsu Data
    private String ninjutsus[];
    private String genjutsus[];
    private String taijutsus[];

    // public Shinobi(
    //     String name,
    //     char gender,
    //     int age,
    //     String ninjutsus[],
    //     String genjutsus[],
    //     String taijutsus[]){
    //         this.name = name;
    //         this.gender = gender;
    //         this.age = age;
    //         this.affiliation = affiliation;
    //         this.ninjutsus = ninjutsus;
    //         this.genjutsus = genjutsus;
    //         this.taijutsus = taijutsus;
    // }
    
    // Default Values
    public Shinobi(){
        name = "Unknown";
        gender = 'U';
        age = 0;
        affiliation = "Unknown";
        ninjutsus[0] = "Unknown";
        genjutsus[0] = "Unknown";
        taijutsus[0] = "Unknown";
    }

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public char getGender(){
        return gender;
    }
    
    public void setGender(char gender){
        this.gender = gender;
    }

    public int getAge(){
        return age;
    }

    public void setAge(int age){
        this.age = age;
    }

    public String getAffiliation(){
        return affiliation;
    }

    public void setAffiliation(String affiliation){
        this.affiliation = affiliation;
    }

    public String[] getNinjutsus(){
        return ninjutsus;
    }

    public void setNinjutsus(String[] ninjutsus){
        this.ninjutsus = ninjutsus;
    }

    public String[] getGenjutsus(){
        return genjutsus;
    }

    public void setGenjutsus(String[] genjutsus){
        this.genjutsus = genjutsus;
    }

    public String[] getTaijutsus(){
        return taijutsus;
    }

    public void setTaijutsus(String[] taijutsus){
        this.taijutsus = taijutsus;
    }
}
