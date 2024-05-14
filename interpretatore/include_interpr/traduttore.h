#include <string>
#include <vector>
using namespace std;

string traduci_lib(string a){
	return "#include \"include\\\\"+a+".h\">";
}

string virgola(string a){
	return a+";";
}

string traduci_forint(string com){
	string a,var="",cond="",passo="";
	int s=0;
	bool inizio=false;
	for(int i=0;i<com.size()-1;i++){
		if (!inizio){
			if (com[i]==' ')inizio=true;
		}
		else{
			if(com[i]!=','){
				switch (s){
				case 0:
					var+=com[i];
					break;
				case 1:
					cond+=com[i];
					break;
				case 2:
					passo+=com[i];
				}
			}
			else{
				i++;
				s++;
			}
		}
	}
	for(int i=0;var[i]!='='&&i<var.size()-1;i++)a+=var[i];
	return "for("+var+";"+cond+";"+a+"+"+passo+"){";
}

string traduci_for(string com,vector <string> vars){
	string a,var="",cond="",passo="";
	int s=0;
	bool inizio=false;
	for(int i=0;i<com.size()-1;i++){
		if (!inizio){
			if (com[i]==' ')inizio=true;
		}
		else{
			if(com[i]!=','){
				switch (s){
				case 0:
					var+=com[i];
					break;
				case 1:
					cond+=com[i];
					break;
				case 2:
					passo+=com[i];
				}
			}
			else{
				i++;
				s++;
			}
		}
	}
	for(int i=0;var[i]!='='&&i<var.size()-1;i++)a+=var[i];
	for(int i=0;i<vars.size()-1;i++)if(a==vars[i])return traduci_forint(com);
	return "for(int "+var+";"+cond+";"+a+"+"+passo+"){";
}



string traduci_if(string a){
	return "if("+a+"){";
}