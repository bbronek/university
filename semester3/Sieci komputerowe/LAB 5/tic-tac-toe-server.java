import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;

/**
 * A server for a network multi-player tic tac toe game.  Modified and
 * extended from the class presented in Deitel and Deitel "Java How to
 * Program" book.  I made a bunch of enhancements and rewrote large sections
 * of the code.  The main change is instead of passing *data* between the
 * client and server, I made a TTTP (tic tac toe protocol) which is totally
 * plain text, so you can test the game with Telnet (always a good idea.)
 * The strings that are sent in TTTP are:
 *
 *  Client -> Server           Server -> Client
 *  ----------------           ----------------
 *  MOVE <n>  (0 <= n <= 8)    WELCOME
 *  QUIT                       VALID_MOVE
 *                             OTHER_PLAYER_MOVED <n>
 *                             VICTORY
 *                             DEFEAT
 *                             TIE
 *                             MESSAGE <text>
 *
 * A second change is that it allows an unlimited number of pairs of
 * players to play.
 */
public class ttt {

    /**
     * Runs the application. Pairs up clients that connect.
     */
    public static void main(String[] args) throws Exception {
        ServerSocket listener = new ServerSocket(8787);
        System.out.println("Tic Tac Toe Server is Running");
        try {
            while (true) {
                Game game = new Game();
                Game.Player playerX = game.new Player(listener.accept(), 'X');
                Game.Player playerO = game.new Player();
                playerX.setOpponent(playerO);
                //playerO.setOpponent(playerX);
                game.currentPlayer = playerX;
                playerX.start();
                //playerO.start();
            }
        } finally {
            listener.close();
        }
    }
}

/**
 * A two-player game.
 */
class Game {

    /**
     * A board has nine squares.  Each square is either unowned or
     * it is owned by a player.  So we use a simple array of player
     * references.  If null, the corresponding square is unowned,
     * otherwise the array cell stores a reference to the player that
     * owns it.
     */
    private Player[] board = {
        null, null, null, null, null,
        null, null, null, null, null,
        null, null, null, null, null,
        null, null, null, null, null,
        null, null, null, null, null};

    /**
     * The current player.
     */
    Player currentPlayer;

    /**
     * Returns whether the current state of the board is such that one
     * of the players is a winner.
     */
    public boolean hasWinner() {
        return
            (board[0] != null && board[0] == board[1] && board[0] == board[2] && board[0] == board[3] && board[0] == board[4])
          ||(board[5] != null && board[5] == board[6] && board[5] == board[7] && board[5] == board[8] && board[5] == board[9])
          ||(board[10] != null && board[10] == board[11] && board[10] == board[12] && board[10] == board[13] && board[10] == board[14])
          ||(board[15] != null && board[15] == board[16] && board[15] == board[17] && board[15] == board[18] && board[15] == board[19])
          ||(board[20] != null && board[20] == board[21] && board[20] == board[22] && board[20] == board[23] && board[20] == board[24])
          ||(board[0] != null && board[0] == board[5] && board[0] == board[10] && board[0] == board[15] && board[0] == board[20])
          ||(board[1] != null && board[1] == board[6] && board[1] == board[11] && board[1] == board[16] && board[1] == board[21])
          ||(board[2] != null && board[2] == board[7] && board[2] == board[12] && board[2] == board[17] && board[2] == board[22])
          ||(board[3] != null && board[3] == board[8] && board[3] == board[13] && board[3] == board[18] && board[3] == board[23])
          ||(board[4] != null && board[4] == board[9] && board[4] == board[14] && board[4] == board[19] && board[4] == board[24])
          ||(board[0] != null && board[0] == board[6] && board[0] == board[12] && board[0] == board[18] && board[0] == board[24])
          ||(board[4] != null && board[4] == board[8] && board[4] == board[12] && board[4] == board[16] && board[4] == board[20]);
    }

    /**
     * Returns whether there are no more empty squares.
     */
    public boolean boardFilledUp() {
        for (int i = 0; i < board.length; i++) {
            if (board[i] == null) {
                return false;
            }
        }
        return true;
    }

    /**
     * Called by the player threads when a player tries to make a
     * move.  This method checks to see if the move is legal: that
     * is, the player requesting the move must be the current player
     * and the square in which she is trying to move must not already
     * be occupied.  If the move is legal the game state is updated
     * (the square is set and the next player becomes current) and
     * the other player is notified of the move so it can update its
     * client.
     * @param output
     */
    public synchronized boolean legalMove(int location, Player player, PrintWriter output) {
        if (player == currentPlayer && board[location] == null) {
            board[location] = currentPlayer;
            //currentPlayer = currentPlayer.opponent;
            //currentPlayer.otherPlayerMoved(location);

            output.println("OK");
            if (hasWinner() || boardFilledUp()) {
            	output.println(hasWinner() ? "WIN"
                         : boardFilledUp() ? "WIN"
                         : "");
            	currentPlayer.win++;
            }

            if (!hasWinner() && !boardFilledUp()){
            Random r = new Random();
            int ile=r.nextInt(25);
            while(board[ile] != null) ile=r.nextInt(25);
            board[ile] = currentPlayer.opponent;
            currentPlayer.otherPlayerMoved(ile);
            }


            return true;
        }
        return false;
    }

    /**
     * The class for the helper threads in this multithreaded server
     * application.  A Player is identified by a character mark
     * which is either 'X' or 'O'.  For communication with the
     * client the player has a socket with its input and output
     * streams.  Since only text is being communicated we use a
     * reader and a writer.
     */
    class Player extends Thread {
        char mark;
        Player opponent;
        Socket socket;
        BufferedReader input;
        PrintWriter output;
        String name;
        int win;
        int lost;

        public Player(){

        }

        /**
         * Constructs a handler thread for a given socket and mark
         * initializes the stream fields, displays the first two
         * welcoming messages.
         */
        public Player(Socket socket, char mark) {
            this.socket = socket;
            this.name="";
            this.mark = mark;
            try {
                input = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));
                output = new PrintWriter(socket.getOutputStream(), true);
                output.println("WELCOME, STATE YOUR NAME");
                //output.println("MESSAGE Waiting for opponent to connect");
            } catch (IOException e) {
                System.out.println("Player died: " + e);
            }
            this.win=0;
            this.lost=0;
        }

        /**
         * Accepts notification of who the opponent is.
         */
        public void setOpponent(Player opponent) {
            this.opponent = opponent;
        }

        /**
         * Handles the otherPlayerMoved message.
         */
        public void otherPlayerMoved(int location) {
            output.println("OPPONENT " + location);
            if (hasWinner() || boardFilledUp()) {
            	output.println(hasWinner() ? "LOST" : boardFilledUp() ? "WIN" : "");
            	this.lost++;
            }
        }

        /**
         * The run method of this thread.
         */
        public void run() {
            try {
                // The thread is only started after everyone connects.
                //output.println("MESSAGE All players connected");

                // Tell the first player that it is her turn.
                //if (mark == 'X') {
                    //output.println("MESSAGE Your move");
                //}

                // Repeatedly get commands from the client and process them.
                while (this.lost+this.win<100) {
                    String command = input.readLine();
                    System.out.println(command);
                    int location =-1;
                    if (this.name.length()>0 && command.startsWith("MOVE")) {
                        try {
                        	location = Integer.parseInt(command.substring(5));
                        } catch(Exception e)
                        {  }
                        if(location <0 || location>=25)  output.println("ERROR");
                        else
                        if (legalMove(location, this, output)) {

                        } else {
                            output.println("ERROR");
                        }
                    } else if (command.startsWith("LOGIN")) {
                    	output.println("OK");
                        name = command.substring(5, command.length());
                    } else if (command.startsWith("QUIT")) {
                    	return;
                    } else {
                        output.println("ERROR");
                    }
                    if(this.lost+this.win<100 && (hasWinner() || boardFilledUp())) {
                    	for(int i=0;i<25;i++) board[i]=null;
                    	output.println("NEW GAME");
                    }
                }
                if(this.win>=75) {
                	try{
                		output.println("SUCCESS");
                		 String filename= "wyniki.txt";
                		 FileWriter fw = new FileWriter(filename,true); //the true will append the new data
                		 fw.write(this.name + '\n');//appends the string to the file
                		 fw.close();

                	} catch (IOException e) {
    					// TODO Auto-generated catch block
    					e.printStackTrace();
    				}
                	System.out.println(this.name + " " + this.win + " " + this.lost);
                	}
        			else
                    	{
        				output.println("FAILED");
        				System.out.println(this.name + " " + this.win + " " + this.lost);
                    	}
            } catch (IOException e) {
                System.out.println("Player died: " + e);
            } finally {


                try {socket.close();} catch (IOException e) {}
            }
        }
    }
}
