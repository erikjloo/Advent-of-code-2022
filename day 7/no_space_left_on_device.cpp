#include <iostream>
// #include <string>
#include <sstream>
#include <fstream>
#include <set>
#include <unordered_map>
#include <queue>
// #include <algorithm>
// #include <utility>
#include <cctype>

class Tree
{

private:
    class Node
    {
    public:
        std::string key;
        long data{0};
        Node *parent;
        std::unordered_map<std::string, Node *> children;
        Node(const std::string &newKey) : key(newKey), data(0), parent(this) {}
        Node(const std::string &newKey, Node *newParent) : key(newKey), data(0), parent(newParent) {}
        Node(const std::string &newKey, const long &newData, Node *newParent) : key(newKey), data(newData), parent(newParent) {}
        ~Node() {}
        void add_child(const std::string &newKey) { children.emplace(newKey, new Node(newKey, parent)); }
        void add_child(const std::string &newKey, const long &newData) { children.emplace(newKey, new Node(newKey, newData, parent)); }
    };
    Node *root_;
    Node *polonger_;
    // std::priority_queue<std::pair<long, std::string>> dirs;
    std::unordered_map<std::string, long> dirs2;
    std::vector<long> blaaaa;

public:
    Tree() : root_(new Node("/")), polonger_(root_) {}
    Tree(const std::string &newKey) { root_ = new Node(newKey); }
    void add_child(const std::string &newKey) { polonger_->add_child(newKey); }
    void add_child(const std::string &newKey, const long &newData) { polonger_->add_child(newKey, newData); }
    void change_dir(const std::string &dir) {
        if (dir == "/")
            polonger_ = root_;
        else if (dir == "..")
            polonger_ = polonger_->parent;
        else
        {
            add_child(dir);
            polonger_ = polonger_->children.at(dir);
        }
    }
    // void go_to_child(const std::string &key) { polonger_ = polonger_->children.at(key); }
    // void go_to_parent() { polonger_ = polonger_->parent; }
    long dfs(Node *ptr) {
        if (ptr->children.empty())
            return ptr->data;
        long sum = 0;
        for (const auto& [filename, ptr]: ptr->children ) {
            long temp = dfs(ptr);
            if (ptr->data == 0)
            {
                // dirs.emplace(temp, filename);
                dirs2.emplace(filename, temp);
                blaaaa.push_back(temp);
            }
            sum += temp;
        }
        return sum;
    }
    long sum_of_dirs(long upper_limit) {
        long top_dir = dfs(root_);
        long sum = top_dir * (top_dir <= upper_limit);
        // std::set<std::string> check;
        for (const auto &val : blaaaa)
            sum += val * (val <= upper_limit);
            // for (const auto &[name, val] : dirs2)
                // sum += val * (val <= upper_limit);
        // while (!dirs.empty())
        // {
        //     const auto& [size, name] = dirs.top();
        //     sum += size * (size <= upper_limit);
        //     std::cout << name << " of size  " << size << std::endl;
        //     dirs.pop();
        // }
        return sum;
    }
    void read_dir(const char *filename)
    {
        std::ifstream file(filename);
        std::string line, a, b, c("");
        while (std::getline(file, line))
        {
            std::stringstream ss(line);
            ss >> a >> b >> c;
            if (b=="cd")
                change_dir(c);
            else if (a == "dir")
                add_child(b);
            else if (b == "ls")
                continue;
            else
            // else if (std::isdigit(static_cast<unsigned char>(a[0])))
                add_child(b, stoi(a));
            std::cout << a << " and " << b << " and " << c << std::endl;
        }
    }
};

int main()
{
    Tree t;
    t.read_dir("input.txt");
    std::cout << t.sum_of_dirs(100000) << std::endl;
    return 0;
}