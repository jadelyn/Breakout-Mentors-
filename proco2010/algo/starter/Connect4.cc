#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>

using namespace std;

// Constants used in the board
static const int EMPTY      = -1;
static const int SELF       = 0;
static const int OPPONENT   = 1;

static int PLAYER_X; // first player,  either == SELF or == OPPONENT
static int PLAYER_O; // second player, either == SELF or == OPPONENT
  
// Direction constants
static const int RIGHT      = 0;
static const int UP_RIGHT   = 1;
static const int UP         = 2;
static const int UP_LEFT    = 3;
static const int LEFT       = 4;
static const int DOWN_LEFT  = 5;
static const int DOWN       = 6;
static const int DOWN_RIGHT = 7;

// Size constants
static const int NUM_ROWS = 8;
static const int NUM_COLS = 8;
  
// Instance variables
int board[NUM_ROWS][NUM_COLS];

// Method declarations
void playGame();
void init();
int heightOfColumn(int ar[NUM_ROWS][NUM_COLS], int col);
bool inBounds(int ar[NUM_ROWS][NUM_COLS], int row, int col);
void visualizeBoard(int ar[NUM_ROWS][NUM_COLS]);
void submitMove(int col);
void updateBoard(int ar[NUM_ROWS][NUM_COLS]);
int numberInARow(int ar[NUM_ROWS][NUM_COLS], int row, int col, int dir);
int maxInARow(int ar[NUM_ROWS][NUM_COLS], int row, int col);

void playGame() {
  while (true) {
    visualizeBoard(board);
    submitMove(rand() % NUM_COLS);
    updateBoard(board);
  }
}
  
/* DO NOT LOOK AT THE CODE BELOW UNLESS YOU ABSOLUTELY WANT TO */
  
void init() {
  char playerCode;
  char buff[10000];
  scanf("%s", buff);
  playerCode = buff[0];
  for (int row = 0; row < 2; row++) {
    scanf("%s", buff);
    for (int col = 0; col < NUM_COLS; col++) {
      if (buff[col] == '.') {
	board[1 - row][col] = EMPTY;
      }
      else {
	board[1 - row][col] = (buff[col] == playerCode ? SELF : OPPONENT);
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
  
int heightOfColumn(int ar[NUM_ROWS][NUM_COLS], int col) {
  int row;
  for (row = 0; row < NUM_ROWS; row++) {
    if (ar[row][col] == EMPTY)
      break;
  }
  return row;
}
  
bool inBounds(int ar[NUM_ROWS][NUM_COLS], int row, int col) {
  return row >= 0 && row < NUM_ROWS && col >= 0 && col < NUM_COLS;
}
    
void visualizeBoard(int ar[NUM_ROWS][NUM_COLS]) {
  fprintf(stderr, "   ");
  for (int col = 0; col < NUM_COLS; col++) {
    fprintf(stderr, "-");
  }
  fprintf(stderr, "\n");
  for (int row = NUM_ROWS - 1; row >= 0; row--) {
    fprintf(stderr, " %c|", row + '0');
    for (int col = 0; col < NUM_COLS; col++) {
      fprintf(stderr, "%c", (ar[row][col] == EMPTY ? '.' : (ar[row][col] == PLAYER_X ? 'X' : 'O')));
    }
    fprintf(stderr, "|\n");
  }
  fprintf(stderr, "   ");
  for (int col = 0; col < NUM_COLS; col++) {
    fprintf(stderr, "-");
  }
  fprintf(stderr, "\n");
  fprintf(stderr, "   ");
  for (int col = 0; col < NUM_COLS; col++) {
    fprintf(stderr, "%c", (char) (col + '0'));
  }
  fprintf(stderr, "\n");
  fflush(stderr);
}
  
void submitMove(int col) {
  if (col >= 0 && col < NUM_COLS) {
    fprintf(stdout, "%c", (char) (col + '0'));
    fflush(stdout);
    int row = heightOfColumn(board, col);
    if (inBounds(board, row, col)) 
      board[row][col] = SELF;
  }
  else {
    fprintf(stdout, "D");
    fflush(stdout);
  }
}
  
void updateBoard(int ar[NUM_ROWS][NUM_COLS]) {
  char buff[10000];
  scanf("%s", buff);
  int col = buff[0] - '0';
  int row = heightOfColumn(ar, col);
  ar[row][col] = OPPONENT;
}
  
int numberInARow(int ar[NUM_ROWS][NUM_COLS], int row, int col, int dir) {
  if (dir >= 0 && dir < 8 && inBounds(ar, row, col)) {
    int dr[8] = {0, 1, 1, 1, 0, -1, -1, -1};
    int dc[8] = {1, 1, 0, -1, -1, -1, 0, 1};
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
  
int maxInARow(int ar[NUM_ROWS][NUM_COLS], int row, int col) {
  int max = 0;
  int numInThisDir;
  for (int dir = 0; dir < 8; dir++) {
    numInThisDir = numberInARow(ar, row, col, dir);
    if (numInThisDir > max)
      max = numInThisDir;
  }
  return max;
}
  
int main() {
  init();
  playGame();
  return 0;
}
