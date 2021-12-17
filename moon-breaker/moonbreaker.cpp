#include <iostream>
#include <cmath>
using namespace std;

int TtoB(string text) {
    long int result = 0;
    for (long int i = 0; i < text.length(); i++) {
        result += (long int)text[i];
    }
    return result;
}

// convert binary to int
int BtoI(string binary) {
    long int result = 0;
    for (long int i = 0; i < binary.length(); i++) {
        result += (long int)binary[i] * pow(2, binary.length() - i - 1);
    }
    return result;
}

// number of caracters in a int
int nb_caracters(long long int n) {
    int result = 0;
    while (n > 0) {
        n /= 10;
        result++;
    }
    return result;
}

long long int MakeKey (string bina, int key)
{
    long long int basse = 1;
    long int sup = BtoI(bina);
    for (long int x = 2 ; x < sizeof(bina)*key + 20 ; x = x  + 1)
    {
        basse = basse * int(bina[x%(sizeof(bina))])+1;
    }


    while (true)
    {
        if (sup > basse)
        {
            sup = sup / 2;
        }
        else if (sup*10 < basse)
        {
            sup = sup * 2;
        }
        else
        {
            break;
        }
    }
    

    basse = basse - sup;

    
    
    while (true)
    {
        cout << "while " << basse << endl;
        
        if (nb_caracters(basse) > 10)
        {
            basse = basse / 10;
        }
        else if (nb_caracters(basse) < 10)
        {
            basse = basse * 10;
        }
        else
        {
            break;
        }
    }

    return basse;
}

long long int moonbreaker(string text, int key)
{
    return MakeKey(TtoB(text) + "1", key);
}

int main()
{
    string text;
    cout << "Texte: ";
    cin >> text;
    cin.ignore();
    long long int sortie = moonbreaker(text, 2);
    cout << sortie << endl;
    return 0;
}