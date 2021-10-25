
// Sudoku solver by Manisha Subrahmanya, 10 A

import java.util.*;

public class sudokuSolver
{
    Scanner obj =new Scanner(System.in);     
    
    public static int SIZE=9;
    
    public void main(String[] args)
    {
        System.out.print("\u000c");   //clear screen before giving all the output statements.                 
        System.out.println("Welcome to the Sudoku Solver");
        System.out.println("\n Enter:");
        System.out.println( "1. INPUT a Sudoku puzzle");
        System.out.println("2. TERMINATE the solver");
        int choice=obj.nextInt();     //input your choice to whether start the program or terminate it 
        int flag=0; //a count for the do-while loop
        do
        {
            switch(choice)
            {   
                case 1:
                {
     int readSudoku[][]=new int[SIZE][SIZE];
                   System.out.println("Enter a Sudoku puzzle");
                   int [][] givenSudoku =new int[SIZE][SIZE];
                   givenSudoku = readPuzzle(readSudoku);   // givenSudoku now holds the Sudoku to be solved
                   System.out.println(" \n The Given Sudoku is");
                   printSudoku(givenSudoku);
                   
                   System.out.println(" ");
                
                   if(solveSudoku(givenSudoku))       // Returns true
                   {   
                      System.out.println("\n Solution for this Sudoku is : ");
                      printSudoku(givenSudoku);
                    }
                    else
                       System.out.println("There is no solution to this Sudoku Puzzle");    // Returns false
                
                      System.out.println("\n If you would like to solve another sudoku, please type 1 to start the solver,else type 2  to terminate");
                     choice=obj.nextInt();
                }
                 break;
                case 2:
                {
                    System.out.println("Thank you. Have a nice day!");
                    flag=1;
                }
                break;
                
            default:
                System.out.println("Wrong input. Please try again");
                choice=obj.nextInt();
         }  // end switch
      }  while(flag==0);
    }   // end main()

 
    //this method reads the Sudoku to be solved and returns it as readSudoku 
    public static int [][] readPuzzle (int [][] sudoku)
    {
     Scanner read=new Scanner(System.in);
     int readSudoku [][] = new int [SIZE][SIZE];   // Creating temporary Sudoku. 
     for (int row = 0; row < SIZE; row++) 
        for (int column = 0; column < SIZE; column++) 
             readSudoku[row][column] = read.nextInt();
          
     return readSudoku;           // Now holds the Sudoku puzzle to be solved
    }

    public static void printSudoku (int givenSudoku [][])
    {
        for(int i= 0 ; i < SIZE ; i++)
        {
            for(int j = 0 ; j < SIZE ; j++)
            {
               System.out.print(givenSudoku [i][j] + "  ");  
            }
            System.out.println();
        }
    }
  
    // Checks if number is present in row
    public static boolean presentInRow (int givenSudoku [][], int row, int col, int number)
    {
        for(int i=0 ; i < SIZE ; i++)        
            if(i!=col && number == givenSudoku [row][i])
                return false;    // Violation! Number IS present in the row        
        return true;   // No violation! Number IS NOT present in the row. There is NO conflict
    }
    
    // Checks if number is present in column
    public static boolean presentInColumn (int givenSudoku [][], int row, int col, int number)
    {
        for(int i=0 ; i<SIZE ; i++)
            if( i!=row && number == givenSudoku [i] [col])
                return false;    // Violation! Number IS present in column}
        return true;   //  No violation! Number IS NOT present in column. There is NO conflict
    }
    
    // Checks if number is present in box
    public static boolean presentInBox (int givenSudoku [][], int row, int col, int number)
    {
        int r, c;
        r = (row/3) *3;                   // Making box
        c = (col/3) *3;
        
        for(int i = r ; i< r+3 ; i++)
           for(int j = c ; j< c+3 ; j++)            
                if(i != row && j != col && givenSudoku [i] [j] == number)
                    return false;    // Violation! Number IS present in the box
        return true;      // No violaton! Number IS NOT present in the box. There is NO conflict
    }
    
         
   /* noConflict() uses the above three methods to check if it is safe to assign a number in that cell. 
         If either of the three methods return a FALSE, that means that the number is NOT allowed in that particular cell. 
        Even if one method returns a false, noConflict() will return a false.*/
   public static boolean noConflict(int givenSudoku [][], int row, int col)   
    {
          int number = givenSudoku[row][col];
          
          return (presentInRow(givenSudoku,row,col,number) && presentInColumn(givenSudoku,row,col,number) &&  presentInBox(givenSudoku,row,col,number));
    }
          
    // function getEmptyCells() is to return an integer 2D Array of location of all the empty cells
    public static int [][] getEmptyCells (int  givenSudoku [][])            
    {
        int count = 0;
        for (int i = 0 ; i < SIZE ; i++)
            for ( int j = 0 ; j< SIZE ; j++)
            {
                if(givenSudoku[i][j] == 0)              
                count++ ;                 // Count is number of empty cells.
            }
                
        int emptyCells [][] = new int [count] [2] ; /* Make a 2D array of the location of the empty cells. Number of 
                                                                                      rows of this array = count, and 2 columns. */
        int index = 0;
        
        for(int i = 0 ; i< SIZE ; i++)
           for( int j = 0 ; j<SIZE ; j++)            
               if (givenSudoku [i][j] == 0)   // If cell is empty
               {
                  emptyCells [index][0] = i;  // i = Storing row number of empty cell
                  emptyCells [index][1] = j;  // j = Storing column number of empty cell
                  index++;
               }
            
        return emptyCells;
    }
    
    // Solves Sudoku and replaces the 0 in the givenSudoku wth numbers of no conflcit
    public static boolean solveSudoku(int givenSudoku [][])
    {
       int emptyCells [][] = getEmptyCells(givenSudoku);
       if(emptyCells.length == 0)   // No more empty cells. Sudoku is solved.
         return true;
       
       int m = 0;   // Acts as 'index' in this method for emptyCells[][]. Will give the first empty cell in emptyCells[][]
       
       while(true)
       {
           int row = emptyCells [m][0]; // row of the 1st empty cell
           int column = emptyCells [m][1]; // column of the first empty cell
               
           if(givenSudoku [row][column] == 0)       // If empty cell
               givenSudoku [row][column] = 1;      // Fill empty cell with number 1
                
                
           if(noConflict(givenSudoku,row,column))   // Number filled in givenSudoku[row][column] is valid.
           {
               if(m+1 == emptyCells.length)     // Have reached the end of emptyCells array i.e. no more empty cells
                    return true;                     // Breaking out 
               else                        // Move to next empty cell                 
                     m++;                    // Go to next row of emptyCells
           }
           
           else if(givenSudoku [row] [column] < SIZE)   /* If number filled in givenSudoku[row][column] is not valid  
                                                                                              and is less than 9 */        
                 givenSudoku [row] [column] = givenSudoku [row] [column] + 1;     //Fill the empty cell with  the next 
                                                                                                                                       //possible value. 
           
           else    // The number filled in the empty cell at givenSudoku[row][column] is 9. Backtrack
           {
                while(givenSudoku [row] [column] == SIZE)
                {
                    if(m == 0)             // First cell and number is already 9. That means error.
                        return false;
                    
                        givenSudoku [row] [column] = 0;     // Resetting before backtracking i.e Make the cell 0 before 
                                                                                       // going to the previous cell. 
                    m = m-1;                                                              
                    row = emptyCells [m][0];         //row of the previous cell
                    column = emptyCells[m][1];  // column of the previous cell
                }   // end while
                                 
                givenSudoku [row] [column] = givenSudoku [row] [column] + 1; // Fill the empty cell with the next 
                                                                                       // possible value. Search continues from this cell.
           } // end else
       }  // end while
    } // end solveSudoku
} // end class



