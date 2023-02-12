#include <ctype.h>
#include <map>
#include <cctype>

class Solution {
public:
    string shortestCompletingWord(string licensePlate, vector<string>& words) {
        // Get letters
        map<char,int> letters; // letters and their dupes
        for (int i = 0; i < licensePlate.length(); i++) {
            char c = tolower(licensePlate.at(i));
            if (!isdigit(c) && c != ' ') {
                letters[c] = (letters.find(c) == letters.end())? 1 : letters[c]+1;
            }
        }

        int leadingIdx = -1;
        int shortestLen = -1;
        for (int i = 0; i < words.size(); i++) {
            map<char,int> copy = letters;
            string word = words[i];
            for (int j = 0; j < word.length(); j++) {
                char c = word.at(j);
                if (copy.find(c) != letters.end()) {
                    copy[c]--;
                }
            }
            // check if dictionary is empty
            bool isEmpty = true;
            map<char,int>::iterator it;
            for (it = copy.begin(); it != copy.end(); it++) {
                if (it->second > 0) {
                    isEmpty = false;
                    break;
                }
            }
            if (isEmpty && (word.length() < shortestLen || leadingIdx == -1)) {
                leadingIdx = i;
                shortestLen = word.length();
            }
        }

        return words[leadingIdx];
    }
};
