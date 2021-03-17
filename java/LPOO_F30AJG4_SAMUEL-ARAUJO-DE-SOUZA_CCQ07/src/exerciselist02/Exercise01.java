/*------------------------------------------------------------------
CIÊNCIA DA COMPUTAÇÃO – UNIP - 2021/1
PROFESSOR: Lauro H. de C. Tomiatti - DATA: Março/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – TURMA: CCQ07

ENUNCIADO: Faça um Programa que peça um número e então mostre a 
mensagem O número informado foi [número].
---------------------------------------------------------------------
*/
package exerciselist02;
import java.util.Scanner;

public class Exercise01{
    private double number;

    void writeNumber(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número: ");
        this.number = scanner.nextDouble();
        System.out.println("O número foi: " + number);
    }
}