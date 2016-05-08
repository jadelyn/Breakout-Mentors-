import java.io.*;
import java.util.*;

public class Connect4 {
  
  // Constants used in the board
  public static final int EMPTY      = -1;
  public static final int SELF       = 0;
  public static final int OPPONENT   = 1;

  public final int PLAYER_X; // first player,  either == SELF or == OPPONENT
  public final int PLAYER_O; // second player, either == SELF or == OPPONENT
  
  // Direction constants
  public static final int RIGHT      = 0;
  public static final int UP_RIGHT   = 1;
  public static final int UP         = 2;
  public static final int UP_LEFT    = 3;
  public static final int LEFT       = 4;
  public static final int DOWN_LEFT  = 5;
  public static final int DOWN       = 6;
  public static final int DOWN_RIGHT = 7;

  // Size constants
  public static final int NUM_ROWS = 8;
  public static final int NUM_COLS = 8;
  
  // Instance variables
  private int[][] board;
  
  private void playGame() throws Exception {
    Random r = new Random();
    while (true) {
      visualizeBoard(board);
      submitMove(r.nextInt(NUM_COLS));
      updateBoard(board);
    }
  }
  
  /* DO NOT LOOK AT THE CODE BELOW UNLESS YOU ABSOLUTELY WANT TO */
  
  public static final Scanner stdin = new Scanner(System.in);
  public static final PrintStream stdout = System.out;
  public static final PrintStream stderr = System.err;
  
  public Connect4() {
    board = new int[NUM_ROWS][NUM_COLS];
    char playerCode = stdin.nextLine().charAt(0);
    for (int row = 0; row < 2; row++) {
      String config = stdin.nextLine();
      for (int col = 0; col < NUM_COLS; col++) {
        if (config.charAt(col) == '.') {
          board[1 - row][col] = EMPTY;
        }
        else {
          board[1 - row][col] = (config.charAt(col) == playerCode ? SELF : OPPONENT);
        }
      }
    }
    for (int row = 2; row < NUM_ROWS; row++) {
      for (int col = 0; col < NUM_COLS; col++) {
	board[row][col] = EMPTY;
      }
    }
    if(playerCode == 'O') {
      PLAYER_X = OPPONENT;
      PLAYER_O = SELF;
      updateBoard(board);
    }
    else {
      PLAYER_X = SELF;
      PLAYER_O = OPPONENT;
    }
  }
  
  public int heightOfColumn(int[][] ar, int col) {
    int row;
    for (row = 0; row < NUM_ROWS; row++) {
      if (ar[row][col] == EMPTY)
        break;
    }
    return row;
  }
  
  public boolean inBounds(int[][] ar, int row, int col) {
    return row >= 0 && row < ar.length && col >= 0 && col < ar[0].length;
  }
    
  public void visualizeBoard(int[][] ar) {
    stderr.print("   ");
    for (int col = 0; col < NUM_COLS; col++) {
      stderr.print("-");
    }
    stderr.print("\n");
    for (int row = NUM_ROWS - 1; row >= 0; row--) {
      stderr.printf(" %c|", row + '0');
      for (int col = 0; col < NUM_COLS; col++) {
        stderr.print(ar[row][col] == EMPTY ? '.' : (ar[row][col] == PLAYER_X ? 'X' : 'O'));
      }
      stderr.print("|\n");
    }
    stderr.print("   ");
    for (int col = 0; col < NUM_COLS; col++) {
      stderr.print("-");
    }
    stderr.print("\n");
    stderr.print("   ");
    for (int col = 0; col < NUM_COLS; col++) {
      stderr.print((char) (col + '0'));
    }
    stderr.print("\n");
    stderr.flush();
  }
  
  public void submitMove(int col) {
    if (col >= 0 && col < NUM_COLS) {
      stdout.printf("%c", (char) (col + '0'));
      stdout.flush();
      int row = heightOfColumn(board, col);
      if (inBounds(board, row, col)) 
        board[row][col] = SELF;
    }
    else {
      stdout.printf("D");
      stdout.flush();
    }
  }
  
  public void updateBoard(int[][] ar) {
    int col = stdin.nextLine().charAt(0) - '0';
    int row = heightOfColumn(ar, col);
    ar[row][col] = OPPONENT;
  }
  
  public int numberInARow(int[][] ar, int row, int col, int dir) {
    if (dir >= 0 && dir < 8 && inBounds(ar, row, col)) {
      int[] dr = {0, 1, 1, 1, 0, -1, -1, -1};
      int[] dc = {1, 1, 0, -1, -1, -1, 0, 1};
      int num = 1;
      int currRow = row + dr[dir];
      int currCol = col + dc[dir];
      while (inBounds(ar, currRow, currCol) && ar[currRow][currCol] == ar[row][col]) {
        currRow += dr[dir];
        currCol += dc[dir];
        num++;
      }
      return num;
    }
    else {
      return 0;
    }
  }
  
  public int maxInARow(int[][] ar, int row, int col) {
    int max = 0;
    for (int dir = 0; dir < 8; dir++) {
      max = Math.max(max, numberInARow(ar, row, col, dir));
    }
    return max;
  }
  
  public int[][] duplicateBoard(int[][] ar) {
    int[][] nar = new int[ar.length][ar[0].length];
    for (int i = 0; i < ar.length; i++) {
      for (int j = 0; j < ar[i].length; j++) {
        nar[i][j] = ar[i][j];
      }
    }
    return nar;
  }
  
  public static void main(String[] args) throws Exception {
    Connect4 game = new Connect4();
    game.playGame();
  }
}