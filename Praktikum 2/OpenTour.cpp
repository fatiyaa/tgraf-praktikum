#include<iostream>
#include<cstring>
#define N 8
using namespace std;

// deklarasi representasi papan catur dengan matrix
int board[N][N];

// pergerakan valid dari knight piece
int row[N] = {2, 1, -1, -2, -2, -1, 1, 2 };
int col[N] = {1, 2, 2, 1, -1, -2, -2, -1 };

// pengecekan pergerakan knight pada papan catur
bool isValid(int r,int c){
	return (r >= 0 && c >= 0 && r < N && c < N && board[r][c] == -1);
}

// memeriksa kemungkinan pergerakan knight
bool knight_tour(int r, int c, int move){
	
    // jika pergerakan sudah valid sebanyak N*N, maka seluruh posisi pada papan catur terjelajah
    if(move == N * N) return true;
	
    // variabel untuk menyimpan posisi sementara pergerakan knight
    int x, y;

    // pengecekan N kemungkinan pergerakan yang valid
	for(int i = 0; i < N; i++){
		
        // posisi setelah pergerakan
        x = r + row[i];
		y = c + col[i];

        // pengecekan posisi pada papan catur
		if(isValid(x, y)){
			
            // menghitung jumlah pergerakan
            board[x][y] = move + 1;

            // pencarian kemungkinan secara rekursif
			if(knight_tour(x, y, move + 1) == 1) return true;

			// backtracking
            else board[x][y] = -1;
		}
	}

    // jika tidak memungkinkan untuk menjelajahi semua posisi papan catur
	return false;
}


int main(){
	
    // inisialisasi semua koordinat pada papan catur menjadi -1 (belum dijelajahi)
	memset(board, -1, sizeof(board));

    // start awal knight
	board[0][0] = 1;

    // jika semua posisi papan catur dapat dijelajahi
	if(knight_tour(0, 0, 1)){
        
        // perulangan untuk menampilkan urutan pergerakan knight pada papan catur
        for(int i = 0; i < N; i++)
        {
            for(int j = 0; j < N; j++) {
                printf("%2d  ", board[i][j]);
            }
            cout << endl;
        }
	}
	
    // jika tidak papan catur tidak dapat dijelajahi
    else cout <<"Papan catur tidak dapat dijelajahi";
	return 0;
}