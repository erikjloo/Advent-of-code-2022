#include <iostream>
#include <sstream>
#include <fstream>
// #include <set>
#include <unordered_map>
#include <vector>
#include <algorithm>
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
        ~Node() { std::cout << "destroying node " << key << std::endl; }
        Node* add_child(const std::string &newKey) {
            children.emplace(newKey, new Node(newKey, this));
            return children.at(newKey);
            }
        Node* add_child(const std::string &newKey, const long &newData) {
            children.emplace(newKey, new Node(newKey, newData, this));
            return children.at(newKey);
        }
    };
    Node *root_;
    Node *pointer_;
    std::vector<long> dirs;

public:
    Tree() : root_(new Node("/")), pointer_(root_) {}
    Tree(const std::string &newKey) { root_ = new Node(newKey); }
    ~Tree() { clear(root_); }
    void clear(Node *ptr)
    {
        // An empty dir or a file
        if (ptr->children.empty())
            delete ptr;

        // A directory with stuff
        for (const auto &[filename, p] : ptr->children)
            clear(p);
    }
    Node* add_child(const std::string &newKey) { return pointer_->add_child(newKey); }
    Node* add_child(const std::string &newKey, const long &newData) { return pointer_->add_child(newKey, newData); }
    void change_dir(const std::string &dir) {
        if (dir == "/")
            pointer_ = root_;
        else if (dir == "..")
            pointer_ = pointer_->parent;
        else
            pointer_ = add_child(dir);
    }

    long dfs(Node *ptr) {
        // An empty dir or a file
        if (ptr->children.empty()) 
            return ptr->data;
        long sum = 0;

        // A directory with stuff
        for (const auto& [filename, p]: ptr->children ) 
            sum += dfs(p); // Sum of all files in dir

        // Update directory size
        ptr->data = sum;
        dirs.push_back(sum);
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
            if (b == "cd")
                change_dir(c);
            else if (a == "dir")
                add_child(b);
            else if (std::isdigit(static_cast<unsigned char>(a[0])))
                add_child(b, stol(a));
        }
    }

    long sum_of_dirs(long upper_limit)
    {
        long sum = 0;
        for (const auto &val : dirs)
            sum += val * (val <= upper_limit);
        return sum;
    }

    long smallest_dir(long total_size, long required_size)
    {
        long current_free = total_size - root_->data;
        // std::cout << root_->data << std::endl;
        std::sort(dirs.begin(), dirs.end(), std::less<long>());
        for (const auto &val : dirs)
            if ((current_free + val) > required_size)
                return val;
        return -1;
    }
    void print()
    {
        dfs(root_);
        print_(root_, "|");
    }

private:
    void print_(Node* ptr, std::string gap)
    {
        for (const auto &[filename, ptr] : ptr->children)
        {
            std::cout << gap << "-" << filename << " " << ptr->data << std::endl;
            print_(ptr, gap + "  |");
        }
    }

};

int main()
{
    Tree t;
    t.read_dir("input.txt");
    t.print();
    std::cout << t.sum_of_dirs(100000) << std::endl;
    std::cout << t.smallest_dir(70000000, 30000000) << std::endl;
    return 0;
}