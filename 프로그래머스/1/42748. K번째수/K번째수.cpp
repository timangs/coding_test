#include <string>
#include <vector>
#include <algorithm>

using namespace std;



vector<int> solution(vector<int> array, vector<vector<int>> commands) {
	vector<int> result;
	vector<int> buffer;
	for_each(commands.begin(), commands.end(), [&](vector<int> i) {

		for (int j = i[0]-1; j < i[1]; j++) {
			buffer.push_back(array[j]);
		}
		sort(buffer.begin(), buffer.end());
		result.push_back(buffer[i[2]-1]);
		buffer.clear();
		});
	return result;
}