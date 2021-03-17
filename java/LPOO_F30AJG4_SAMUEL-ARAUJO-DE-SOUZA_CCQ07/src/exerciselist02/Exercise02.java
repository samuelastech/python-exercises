/*------------------------------------------------------------------
CIÊNCIA DA COMPUTAÇÃO – UNIP - 2021/1
PROFESSOR: Lauro H. de C. Tomiatti - DATA: Março/2020
ALUNO: Samuel Araujo de Souza  RA: F30AJG-4 – TURMA: CCQ07

ENUNCIADO: Faça um Programa que peça dois números e imprima
a soma.
---------------------------------------------------------------------
*/

package exerciselist02;

import java.util.Scanner;

public class Exercise02 {
    private double number1;
    private double number2;
    private double result;

    void getSum(){
        Scanner getNumber = new Scanner(System.in);

        System.out.print("Digite um número: ");
        this.number1 = getNumber.nextDouble();

        System.out.print("Digite outro número: ");
        this.number2 = getNumber.nextDouble();

        this.result = number1 + number2;

        System.out.print("A soma dos números é: " + result);
    }
}
