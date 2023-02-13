#include <vector>
#include <set>

class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        // Split
        vector<string> split;
        int start_idx = 0;
        for (int i = 0; i < text.length(); i++) {
            if (isblank(text.at(i))) {
                int len = i - start_idx;
                split.push_back(text.substr(start_idx, len));
                start_idx = i+1;
            }
        }
        split.push_back(text.substr(start_idx, text.length()));
        int working_words = split.size();
        // Set
        set<char> keys;
        for (int i = 0; i < brokenLetters.length(); i++) {
            keys.insert(brokenLetters.at(i));
        }
        // Find in set
        for (int i = 0; i < split.size(); i++) {
            string word = split[i];
            for (int j = 0; j < word.length(); j++) {
                char c = word.at(j);
                if (keys.find(c) != keys.end()) {
                    working_words--;
                    break;
                }
            }
        }
        return working_words;
    }
};
