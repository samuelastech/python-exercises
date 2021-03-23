package naruto;

import java.util.Scanner;
import naruto.characters.Shinobi;

public class App {
    public static void main(String[] args) throws Exception {
        Shinobi shinobi = new Shinobi();
        Scanner read = new Scanner(System.in);
        boolean control = true;

        while(control){
            System.out.print("Digite o nome do Shinobi: ");
            String name = read.next();
            shinobi.setName(name);

            System.out.print("Digite a idade do Shinobi: ");
            int age = read.nextInt();
            shinobi.setAge(age);

            System.out.print("Digite o gênero do Shinobi: ");
            char gender = (char) read.nextByte();
            shinobi.setGender(gender);

            System.out.print("Digite a affiliação do Shinobi: ");
            String affiliation = read.next();
            shinobi.setAffiliation(affiliation);

            // Create a second loop to set Ninjutsus, genjutsus and taijutsus
            // Create a JSON to save each Character
        }

        shinobi.setGender('M');
        shinobi.setAffiliation("Konoha");

        String narutoNinjutsus[] = {"Rasengan", "Shadow Clones", "Sennin Mode"};
        shinobi.setNinjutsus(narutoNinjutsus);

        String narutoGenjutsus[] = {"Unknow"};
        shinobi.setNinjutsus(narutoGenjutsus);

        String narutoTaijutsus[] = {"Red Chakra Nine Tails"};
        shinobi.setNinjutsus(narutoTaijutsus);
    }
}
