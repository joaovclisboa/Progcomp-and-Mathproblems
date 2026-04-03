#include <iostream>
#include <vector>
#include <string>


int max(int a, int b){
    return a > b ? a:b;
}

std::string MergeStrAlt(std::string word1, std::string word2){
    std::string merged;
    size_t i = 0, j = 0;
    while (i < word1.length() || j < word2.length()){
        if (i < word1.length()) merged += word1[i++];
        if (j < word2.length()) merged += word2[j++];
    }
    return merged;
}


int main(void){
    std::cout << "oii" << std::endl;
    std::cout << MergeStrAlt("abc", "pqr");
}
