#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using IntPair = std::pair<int, int>;

namespace std {
	template <>
		struct hash<IntPair> {
			std::size_t operator() (const IntPair& p) const {
			std::string uniqueIntPairString = std::to_string(p.first) + "##" + std::to_string(p.second);
			std::hash<std::string> stringHasher;
			return stringHasher(uniqueIntPairString);
			}
	};
}

class HillClimb{
	std::vector<std::vector<int>> grid;
	std::unordered_map<IntPair, IntPair> visited;
	IntPair start;
	IntPair end;
	int nrow;
	int ncol;

public:
	HillClimb(const char* filename) 
	{
		std::ifstream file(filename);
		std::string line;
		int i = 0;
		while (file >> line) {
			auto j = line.find("S");
			if (j != std::string::npos)
			{
				start = std::make_pair(i, j);
				line.replace(j, 1, "a");
			}
			j = line.find("E");
			if (j != std::string::npos)
			{
				end = std::make_pair(i, j);
				line.replace(j, 1, "z");
			}
			++i;
			grid.emplace_back(line.begin(), line.end());
		}

		nrow = static_cast<int>(grid.size());
		ncol = static_cast<int>(grid.front().size());
	}



	IntPair BFS() {
		visited.emplace(start, start);
		std::queue<IntPair> q;
		q.push(start);
		while (!q.empty() && q.front() != end)
		{
			auto [ic, jc] = q.front();
			q.pop();
			for (auto [i, j]: neighbors(ic, jc))
			{
				if (visited.contains(std::make_pair(i, j)))
					continue;
				if (abs(grid[ic][jc] - grid[i][j]) > 1)
					continue;
				q.emplace(std::make_pair(i, j));
				visited.emplace(std::make_pair(i, j), std::make_pair(ic, jc));
				if (std::make_pair(i, j) == end)
					return std::make_pair(i, j);
			}
		}
		return start;
	}

	std::unordered_set<IntPair> neighbors(int ic, int jc)
	{
		std::unordered_set<IntPair> neighbors;
		neighbors.emplace(ic, std::max(jc-1, 0));
		neighbors.emplace(ic, std::min(jc+1, ncol-1));
		neighbors.emplace(std::max(ic-1, 0), jc);
		neighbors.emplace(std::min(ic+1, nrow-1), jc);
		return neighbors;
	}
	
	int shortest_path(){
		auto loc = BFS();
		std::vector<IntPair> path = {loc};
		while (loc != start){
			loc = visited.at(loc);
			path.emplace_back(loc);
		}
		return static_cast<int>(path.size())-1;
	}
};







int main(){

	HillClimb hc{"simple.txt"};
	std::cout << hc.shortest_path() << std::endl;
	return 1;
}
	