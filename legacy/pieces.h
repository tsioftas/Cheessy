#include<vector>

#define WHITE 0
#define BLACK 1
using namespace std;

class Coord
{
private:
    int x,y;
public:
    Coord(int a,int b)
    {
        x = a;
        y = b;
    }

    int GetX()
    {
        return x;
    }

    int GetY()
    {
        return y;
    }

    void SetX(int a)
    {
        x = a;
    }

    void SetY(int a)
    {
        y = a;
    }
};

class Piece
{
private:
    Coord position = Coord(0,0);
    int color;
    vector<pair<int,int> > legal_moves;
public:
    Piece(int x,int y,int col)
    {
        position = Coord(x,y);
        color = col;
    }

    int GetColor()
    {
        return color;
    }
};

class Rook : Piece
{
public:
    Rook(int x,int y,int col):Piece(x,y,col)
    {
        for(int i=1;i<=8;++i)
        {
            legal_moves.push_back(make_pair(i,0));
            legal_moves.push_back(make_pair(-i,0));
            legal_moves.push_back(make_pair(0,i));
            legal_moves.push_back(make_pair(0,-i));
        }
    }
};
