#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std; 

int main() {
    int jam = 0;
    string myints[1] = {};
    list<string> todo (myints, myints + sizeof(myints) / sizeof(string));
    ifstream fichier("s.txt");
    string ligne;
    
    if (fichier) while(getline(fichier, ligne)) todo.emplace_back(ligne);
    else cout << "ERREUR: Impossible d'ouvrir le fichier en lecture." << endl;

    for (list<string>::iterator a = todo.begin(); a != todo.end(); a++) {
        jam = 0;
        for (list<string>::iterator b = todo.begin(); b != todo.end(); b++) {
            if (*a == *b) ++jam;
        }
        if (jam > 1) cout << jam << " - " << *a << endl;
    }

    return 0;
}
