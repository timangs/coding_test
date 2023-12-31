#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
	int size_higher = 0;
	int size_weight = 0;
	for_each(sizes.begin(), sizes.end(), [&size_higher, &size_weight](vector<int> size) {
		sort(size.begin(),size.end());
			if (size[0] > size_higher) {
				size_higher = size[0];
			}
			if (size[1] > size_weight) {
				size_weight = size[1];
			}
		});
	
	int answer = size_higher * size_weight;
	return answer;
}