package TicTacToe;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        char[][] board = new char[3][3];
        char activePlayer = 'X';

        for (int i = 0; i < 9; i++) {
            board[i / 3][i % 3] = ' ';
        }
        display(board);
        while (true) {
            while (true) {
                System.out.print("Enter the coordinates:");
                String[] inputs = scan.nextLine().split(" ");
                int x = Integer.parseInt(inputs[0]);
                int y = Integer.parseInt(inputs[1]);
                if (x > 3 || x < 1 || y > 3 || y < 1) {
                    System.out.println("Coordinates should be from 1 to 3!");
                } else if (board[3 - y][x - 1] != ' ') {
                    System.out.println("This cell is occupied! Choose another one!");
                } else {
                    board[3 - y][x - 1] = activePlayer;
                    display(board);
                    break;
                }
            }
            if(check(board, activePlayer)) {
                System.out.println(String.format("%c wins", activePlayer));
                break;
            }
            if(checkDraw(board)) {
                System.out.println(String.format("Draw"));
                break;
            }
            activePlayer = activePlayer == 'X' ? 'O' : 'X';
        }
    }

    public static boolean checkDraw(char[][] board) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if(board[i][j] == ' ') return false;
            }
        }
        return true;
    }

    public static boolean check(char[][] board, char player) {
        return checkVertical(board, player) || checkHorizontal(board, player) || checkDiagonal(board, player);
    }

    public static boolean checkVertical(char[][] board, char player) {
        for (int i = 0; i < 3; i++) {
            if(board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[2][i] == player) return true;
        }
        return false;
    }

    public static boolean checkHorizontal(char[][] board, char player) {
        for (int i = 0; i < 3; i++) {
            if(board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][2] == player) return true;
        }
        return false;
    }

    public static boolean checkDiagonal(char[][] board, char player) {
        if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[2][2] == player) return true;
        if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[2][0] == player) return true;
        return false;
    }

    public static void display(char[][] board) {
        System.out.println("---------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(String.format("%c ", board[i][j]));
            }
            System.out.println("|");
        }
        System.out.println("---------");
    }
}
