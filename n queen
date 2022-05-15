#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
#define n 4
// Here we are filling the queens row-wise and checking the danger column and both-the-diagonals wise
// Basically we are maintaining extra arrays to indicate if the particular cell lies in the range of any other queen or not, these are the arrays for cols and both diags as per the movement of the queen.
// cols array indicates that the particular column no. is at risk for other queens so no. of col == no. of "n" in n-queen
// the size of the diagonal arrays needs visualization where row + col means the number of the diagonals and could act as index no. for the \diagonal
// similarly row - col + n - 1 indicates the indices for / diagonal
// so once we finish with placing a queen at a row, we move on to another one recursively
// if all queens are placed then we print the board otherwise just exit.
// this code gives us multiple configurations as the solutions because we are traversing all the rows(inner loop) of each column(outer loop) and if some solution exists it is printed
// NOTE: Recursion stops once there isn't a cell empty in a row and therefore the func doesnot reach uptil row == n ka point so that the sol. is printed and thus the "Bounding" that we don't check further this "branch" pichle recursion stack ka column could be considered as the parent and agle recursion stack ka column(s) children kehlayenge aur jaise jaise har branch(col) ko explore karre to malum hora ki us branch ke age koi branch jaapara kya, nahi to bound karke band kardere.
// CREDIT: Abdul Bari && Mera Dimaag.
void solve(vector<vector<int>> board, int row, int cols[], int bsd[], int sd[])
{

    if (row == n)
    {
        // cout << "HI!!";
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cout << board[i][j] << " ";
            }
            cout << "\n";
        }
        return;
    }
    // int cols[n], bsd[2 * n - 1], sd[2 * n - 1];
    for (int col = 0; col < n; col++)
    {
        if (cols[col] == 0 && bsd[row + col] == 0 && sd[row - col + n - 1] == 0)
        {
            board[row][col] = 1;
            cols[col] = 1;
            bsd[row + col] = 1;
            sd[row - col + n - 1] = 1;
            /*for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    cout << board[i][j] << " ";
                }
                cout << "\n";
            }*/

            solve(board, row + 1, cols, bsd, sd);

            board[row][col] = 0;
            cols[col] = 0;
            bsd[row + col] = 0;
            sd[row - col + n - 1] = 0;
        }
    }
}
int main()
{
    vector<vector<int>> board{{0, 0, 0, 0},
                              {0, 0, 0, 0},
                              {0, 0, 0, 0},
                              {0, 0, 0, 0}};
    int cols[n], bsd[2 * n - 1], sd[2 * n - 1];
    for (int i = 0; i < n; i++)
    {
        cols[i] = 0;
    }
    for (int i = 0; i < 2 * n - 1; i++)
    {
        bsd[i] = 0;
        sd[i] = 0;
    }
    // memset(*cols, 0, n);
    // memset(*bsd, 0, 2 * n - 1);
    // memset(*sd, 0, 2 * n - 1);
    // cout << bsd[3];
    solve(board, 0, cols, bsd, sd);
}
