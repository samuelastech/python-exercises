package exerciselist02;

import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class App {
    public static void main(String[] args) throws Exception {
        boolean controller = true;
        Scanner scanner = new Scanner(System.in);

        while(controller){
            System.out.println("EXERCÍCIOS");
            System.out.println("- 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 - 11 - 12 - 13 - 14 - 15");
            System.out.println("Para sair digite '0'\n");
            System.out.print("DIGITE O NÚMERO DO EXERCÍCIO: ");
            int exercise = scanner.nextInt();

            switch(exercise){
                case 0:
                    controller = false;
                    break;
                case 1:
                    Exercise01 exercise01 = new Exercise01();
                    exercise01.writeNumber();
                    TimeUnit.SECONDS.sleep(2);
                    break;
                case 2:
                    Exercise02 exercise02 = new Exercise02();
                    exercise02.getSum();
                    TimeUnit.SECONDS.sleep(2);
                    break;
            }
        }
    }
}