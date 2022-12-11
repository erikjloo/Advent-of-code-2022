#include <iostream>
#include <sstream>
#include <fstream>
#include <set>
#include <unordered_map>
#include <queue>
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
        Node* add_child(const std::string &newKey) {
            if (!children.count(newKey))
            {
                Node* ptr = new Node(newKey, parent);
                children.emplace(newKey, ptr); 
                return ptr;
            }
            else
                return children.at(newKey);
            }
        Node* add_child(const std::string &newKey, const long &newData) {
            if (!children.count(newKey))
            {
                Node *ptr = new Node(newKey, newData, parent);
                children.emplace(newKey, ptr);
                return ptr;
            }
            else
                return children.at(newKey);
        }
    };
    Node *root_;
    Node *pointer_;
    std::priority_queue<std::pair<long, std::string>> dirs;
    std::unordered_map<std::string, long> dirs2;
    std::vector<long> blaaaa;

public:
    Tree() : root_(new Node("/")), pointer_(root_) {}
    Tree(const std::string &newKey) { root_ = new Node(newKey); }
    Node* add_child(const std::string &newKey) { return pointer_->add_child(newKey); }
    Node* add_child(const std::string &newKey, const long &newData) { return pointer_->add_child(newKey, newData); }
    void change_dir(const std::string &dir) {
        if (dir == "/")
            pointer_ = root_;
        else if (dir == "..")
            pointer_ = pointer_->parent;
        else
        {
            if (dir == "qjlvh")
                std::cout << "FUCK" << std::endl;
            pointer_ = add_child(dir);
            // pointer_ = pointer_->children.at(dir);
        }
    }
    // void go_to_child(const std::string &key) { pointer_ = pointer_->children.at(key); }
    // void go_to_parent() { pointer_ = pointer_->parent; }
    long dfs(Node *ptr) {
        if (ptr->children.empty()) // An empty dir or a file
            return ptr->data;
        long sum = 0;
        for (const auto& [filename, p]: ptr->children ) 
        {
            if (filename == "hrznddsg")
                std::cout <<  "oi" << std::endl;

            long temp = dfs(p); // Sum of all files in dir
            sum += temp;
            if (p->data == 0) // file is a folder -> store its size
            {
                dirs2.emplace(filename, temp);
                dirs.emplace(temp, filename);
                blaaaa.push_back(temp);
            }
        }
        return sum;
    }
    long sum_of_dirs(long upper_limit) {
        long top_dir = dfs(root_);
        long sum = top_dir * (top_dir <= upper_limit);
        // std::set<std::string> check;
        for (const auto &val : blaaaa)
            sum += val * (val <= upper_limit);
        //     // for (const auto &[name, val] : dirs2)
        //         // sum += val * (val <= upper_limit);
        // while (!dirs.empty())
        // {
        //     const auto& [size, name] = dirs.top();
        //     sum += size * (size <= upper_limit);
        //     // std::cout << name << " of size  " << size << std::endl;
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
            if (b == "cd")
                change_dir(c);
            // else if (b == "ls")
            //     continue;
            // else if (a == "dir")
                // add_child(b);
            else if (std::isdigit(static_cast<unsigned char>(a[0])))
            {
                // if (b == "tftmcrt")
                //     std::cout << "oi" << std::endl;
                add_child(b, stol(a));
            }
            // else if (std::isdigit(static_cast<unsigned char>(a[0])))
            // std::cout << a << " and " << b << " and " << c << std::endl;
        }
    }
    void print()
    {
        dfs(root_);
        print_(root_, "");
    }
    void print_(Node* ptr, std::string gap)
    {
        for (const auto &[filename, ptr] : ptr->children)
        {
            long size = (ptr->data == 0)? dirs2.at(filename) : ptr-> data;
            std::cout << gap << filename << " " << size << std::endl;
            print_(ptr, gap + "  |-");
        }
    }

};

int main()
{
    Tree t;
    t.read_dir("input.txt");
    t.print();
    std::cout << t.sum_of_dirs(100000) << std::endl;
    return 0;
}