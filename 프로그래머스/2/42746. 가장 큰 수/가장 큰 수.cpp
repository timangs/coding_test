#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
	vector<string> vec_string;
	string answer;
	for (int num : numbers) {
		vec_string.push_back(to_string(num));
	}

	sort(vec_string.begin(), vec_string.end(), [](const string& a, const string& b) {
		if (a.length() == b.length()) {
			return a > b;
		}
		else {
			return a + b > b + a;
		}
		});
	for (const string& s : vec_string) {
		if (vec_string[0] == "0") {
			return "0";
		}
		answer += s;
	}
	return answer;
}
