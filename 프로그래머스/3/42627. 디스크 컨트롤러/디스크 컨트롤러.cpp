#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

struct Job {
    int duration;	
    int start;
    int seq;
    
    bool operator<(const Job& other) const {
        if (duration != other.duration) return duration > other.duration;
        else {
            if (start != other.start) return start > other.start;
            else return seq > other.seq;
        }
    }
};

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    // 우선순위: duration 작은 것, start 작은 것, seq 작은 것
    priority_queue<Job> pq;
    
    // 작업마다 순번 부여하여, 시작시간 내림차순으로 정렬
    vector<Job> rich_jobs;
    for (int i = 0; i < (int)jobs.size(); i++) rich_jobs.push_back({jobs[i][1], jobs[i][0], i});
    sort(rich_jobs.begin(), rich_jobs.end(), [](const Job& a, const Job& b) {
        return a.start > b.start;
    });
    // for (auto& job : rich_jobs) printf("%d,%d\n", job.seq, job.duration);
    
    // 시작시간 짧은것부터 탐색하기위해 뒤에서 순회
    int time = 0;
    while (true) {
        Job job;
        if (!rich_jobs.empty()) {
            job = rich_jobs.back();
        	// printf("%d,%d, time=%d, answer=%d\n", job.seq, job.duration, time, answer);
            if (job.start <= time) {
                pq.push(job);
                rich_jobs.pop_back();
                // printf("꺼냄\n");
                continue;
	        }
        }
        
        if (!pq.empty()) {
        	job = pq.top();
            time += job.duration;
            pq.pop();
            answer += time - job.start;
        } else {
            time++;
        }
        
        if (pq.empty() && rich_jobs.empty()) break;
    }
    
    return answer / jobs.size();
}