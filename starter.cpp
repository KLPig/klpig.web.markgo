#include <iostream>
#include <fstream>


using namespace std;
int main(int argv, const char** argc){
	ofstream fout;
	fout.open("./target.mgtgt");
	if(argv == 2)
		fout << argc[1];
	else
		fout << "";
	fout.close();
	system("python runner.py");
	return 0;
}
