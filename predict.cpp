#include "util.hpp"
#include "DictionaryTrie.hpp"
#include <fstream>
#include <string>
#include <vector>
#include <time.h>

void autoSuggest(int size, int stepSize, int iterations, std::string fileName, std::string input, int num_completions) {

	//load all words in fileName into vector
	//then randomly add words from vector to 3 dicts
	std::vector<std::string> v;
	std::ifstream in;
    in.open(fileName, std::ios::binary);
	Utils::load_dict(v, in);
	
	std::vector<std::string> uselessWords;
	uselessWords.push_back(input);

	//create 3 dicts
	DictionaryTrie d_trie;

	std::vector<std::pair<int,long long int>> trie;

	Timer T;
	long long time_duration;

	srand (time(NULL));
	unsigned int randomNum;
	for(int i=0; i < iterations; i++) {
		for (int j=0; j<stepSize; j++) {
			randomNum = rand() % v.size();
			d_trie.insert(v[randomNum],0);
		}	

		//now benchmark the tree find times
		T.begin_timer();
		for(auto it=uselessWords.begin(); it!= uselessWords.end();it++) {
			d_trie.find(*it);
		}
		time_duration = T.end_timer();
		trie.push_back(std::make_pair((i+1)*stepSize,time_duration));
	}

	std::vector<std::string> predictions = d_trie.predictCompletions(input, num_completions);

	for(int i = 0; i < predictions.size(); i++) {
		std::cout << predictions[i] << std::endl;
	}
}

int main(int argc, char *argv[]) {

    if(argc < 5){
        std::cout << "Incorrect number of arguments. (required 4)" << std::endl;
        std::cout << "\t 1:The minimum size of the dictionary you want to test" << std::endl;
		std::cout << "\t 2:The step size (how much to increase the dictionary size each iteration)" << std::endl;
		std::cout << "\t 3:The number of iterations (e.g. how many times do you want to increase your dictionary size" << std::endl;
		std::cout << "\t 4:The name of a dictionary file to use" << std::endl;
		std::cout << "\t 5:The word for auto suggestion" << std::endl;
		std::cout << "\t 6:The number of completions" << std::endl;
        std::cout << std::endl;
        exit(-1);
    }

    autoSuggest(atoi(argv[1]),atoi(argv[2]),atoi(argv[3]),argv[4], argv[5], atoi(argv[6]));

}