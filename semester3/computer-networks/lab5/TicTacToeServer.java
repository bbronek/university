import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;

public class TicTacToeServer {
    private static final int SIZE = 5;
    private static final int GAMES = 100;

    static boolean hasWinner(char[] board, char mark) {
        boolean diagonal = true, reverseDiagonal = true;
        for (int row = 0; row < SIZE; row++) {
            boolean horizontal = true, vertical = true;
            for (int column = 0; column < SIZE; column++) {
                horizontal &= board[row * SIZE + column] == mark;
                vertical &= board[column * SIZE + row] == mark;
            }
            if (horizontal || vertical) return true;
            diagonal &= board[row * SIZE + row] == mark;
            reverseDiagonal &= board[row * SIZE + SIZE - row - 1] == mark;
        }
        return diagonal || reverseDiagonal;
    }

    private static List<Integer> availableMoves(char[] board) {
        List<Integer> moves = new ArrayList<>();
        for (int index = 0; index < board.length; index++) {
            if (board[index] == 0) moves.add(index);
        }
        return moves;
    }

    private static synchronized void recordWinner(String name) throws IOException {
        try (BufferedWriter writer = Files.newBufferedWriter(Path.of("results.txt"),
                StandardCharsets.UTF_8, StandardOpenOption.CREATE, StandardOpenOption.APPEND)) {
            writer.write(name);
            writer.newLine();
        }
    }

    private static void play(Socket socket) {
        try (socket;
             BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
             PrintWriter output = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true)) {
            char[] board = new char[SIZE * SIZE];
            Random random = new Random();
            String name = null;
            int completed = 0, wins = 0;
            output.println("WELCOME, STATE YOUR NAME");
            String command;
            while ((command = input.readLine()) != null) {
                if (command.equals("QUIT")) return;
                if (command.startsWith("LOGIN ") && name == null) {
                    name = command.substring(6).trim();
                    if (name.isEmpty()) {
                        name = null;
                        output.println("ERROR");
                    } else {
                        output.println("OK");
                        output.println("YOUR_TURN");
                    }
                    continue;
                }
                int location;
                try {
                    if (name == null || !command.startsWith("MOVE ")) throw new NumberFormatException();
                    location = Integer.parseInt(command.substring(5).trim());
                    if (location < 0 || location >= board.length || board[location] != 0) throw new NumberFormatException();
                } catch (NumberFormatException exception) {
                    output.println("ERROR");
                    continue;
                }
                board[location] = 'X';
                output.println("OK");
                String result = null;
                if (hasWinner(board, 'X')) {
                    result = "WIN";
                    wins++;
                } else {
                    List<Integer> moves = availableMoves(board);
                    if (!moves.isEmpty()) {
                        int opponentMove = moves.get(random.nextInt(moves.size()));
                        board[opponentMove] = 'O';
                        output.println("OPPONENT " + opponentMove);
                        if (hasWinner(board, 'O')) result = "LOST";
                    }
                    if (result == null && availableMoves(board).isEmpty()) result = "DRAW";
                }
                if (result != null) {
                    output.println(result);
                    if (++completed == GAMES) {
                        if (wins >= 75) recordWinner(name);
                        output.println(wins >= 75 ? "SUCCESS" : "FAILED");
                        return;
                    }
                    Arrays.fill(board, (char) 0);
                    output.println("NEW GAME");
                }
                output.println("YOUR_TURN");
            }
        } catch (IOException exception) {
            System.err.println("Connection failed: " + exception.getMessage());
        }
    }

    public static void main(String[] args) throws IOException {
        int port = args.length == 0 ? 8787 : Integer.parseInt(args[0]);
        try (ServerSocket listener = new ServerSocket(port)) {
            System.out.println("Tic-tac-toe server listening on " + listener.getLocalPort());
            while (true) {
                Socket socket = listener.accept();
                new Thread(() -> play(socket)).start();
            }
        }
    }
}
