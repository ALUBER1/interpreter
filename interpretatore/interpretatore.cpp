#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>
#include "include_interpr/traduttore.h"
using namespace std;

vector <char> contents;
vector <string> vars;
fstream cpp("cpp.cpp",ios::out);
vector <string> comm={"if","for","while","int","float","bool","string","char",";"};

int rilevatore(int& a,string& m){
	string c="";
	m="";
	for(;contents[a]!='\n'&&a<contents.size()-1;a++){
		m+=contents[a];
	}
	a++;
	for(int i=0;i<m.size();i++){
		c+=m[i];
		for(int k=0;k<comm.size();k++){ 
			if(c==comm[k]){
				return k;
			}
		}
	}
}

void mainloop(){
	int a;
	string com;
	for(int i=0;i<contents.size()-1;i++){
		if(contents[i]!=' '){
			a=rilevatore(i,com);
			switch (a){
			case 0:
				com=traduci_if(com);
				break;
			case 1:
				com=traduci_for(com,vars);
				break;
			case 8:
				cpp<<"}"<<endl;
				com="";
				break;
			}
			cpp<<com<<endl;
		}
	}
}

void trovalibrerie(vector <string>& librerie){
	char b;
	string a="";
	bool bo=false;
	for(int i=0;i<contents.size();i++){
		if(bo&&contents[i]!='#'){
			a+=contents[i];
			contents[i]=' ';
		}
		if(contents[i]=='#'){
			contents[i]=' ';
			if(bo){
				librerie.push_back(a);
				librerie[librerie.size()-1]=traduci_lib(librerie[librerie.size()-1]);
			}
			bo=!bo;
		}
	}
}

int main(){
	cpp.close();
	cpp.open("cpp.cpp",ios::app);
	fstream file("messaggi\\path.txt",ios::in);
	string path,a;
	char b;
	getline(file,path);
	char path_char[path.size()];
	strcpy(path_char,path.c_str());
	vector <string> librerie;
	file.close();
	file.open(path_char,ios::in);
	while(!file.eof()){
		file.get(b);
		contents.push_back(b);
	}
	trovalibrerie(librerie);
	for(int i=0;i<librerie.size();i++)cpp<<librerie[i]<<endl;
	mainloop();
	return 0;
}
