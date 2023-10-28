#include <string>
#include <vector>
#include <map>
#include <algorithm>


#include <iostream>

using namespace std;

void print_genre_count(map<string, pair<int, vector<pair<int, int>>>>& gc);
bool CompMusic(const pair<int, int>& p1, const pair<int, int>& p2);
bool CompGenre(const pair<string, pair<int, vector<pair<int, int>>>>& p1, const pair<string, pair<int, vector<pair<int, int>>>>& p2);

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    // genres : <total_plays, vector<music_id, music_play>>
    map<string, pair<int, vector<pair<int, int>>>> genre_count;
    
	    
    for (int i = 0; i < genres.size(); i++) {
        genre_count[genres[i]].first += plays[i];
        genre_count[genres[i]].second.push_back({i, plays[i]});
    }
    
    for (auto& kv : genre_count) {
        sort(kv.second.second.begin(), kv.second.second.end(), CompMusic);
    }
    
    vector<pair<string, pair<int, vector<pair<int, int>>>>> gcList(genre_count.begin(), genre_count.end());
    
    // print_genre_count(genre_count);
    
    sort(gcList.begin(), gcList.end(), CompGenre);
    
    vector<pair<int, int>> temp;
    for (auto& item : gcList) {
        temp = item.second.second;
        answer.push_back(temp[0].first);
        if (temp.size() > 1) {
            answer.push_back(temp[1].first);
        }
    }
    
    return answer;
}

void print_genre_count(map<string, pair<int, vector<pair<int, int>>>>& gc) {
    for (auto& kv : gc) {
        cout << kv.first << ", " << kv.second.first << '\n';
        for (auto item : kv.second.second) {
            cout << item.first << ", " << item.second << " / ";
        }
        cout << '\n';
    }
}

bool CompMusic(const pair<int, int>& p1, const pair<int, int>& p2) {
    return p1.second > p2.second;
}

bool CompGenre(const pair<string, pair<int, vector<pair<int, int>>>>& p1, const pair<string, pair<int, vector<pair<int, int>>>>& p2) {
    return p1.second.first > p2.second.first;
}