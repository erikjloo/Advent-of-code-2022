#include <fstream>
#include <iostream>
#include <list>
#include <regex>
#include <iterator>
// using List = std::list<int>

enum Type
{
    Int,
    list
};

class List
{
private:
    class Node
    {
    public:
        void *contents;
        Node *prev;
        Node *next;
        Type type;

    public:
        Node() : contents(nullptr), prev(nullptr), next(nullptr), type(Type::list) {}
        // Node(Type l) : Node(), type(l) {}
        Node(int a) : contents(static_cast<void *>(new int{a})), prev(nullptr), next(nullptr), type(Type::Int) {}
        Node(const List &a) : contents(static_cast<void *>(new List{a})), prev(nullptr), next(nullptr), type(Type::list) {}
        std::string print() const
        {
            if (type == Type::Int)
                return std::to_string(*(static_cast<int *>(contents)));
            else
                return "[" + (static_cast<List *>(contents))->print() + "]";
        }
        ~Node()
        {
            switch (type)
            {
            case Type::Int:
                delete static_cast<int *>(contents);
            default:
                delete static_cast<List *>(contents);
            }
        }
    };
    List *parent_;
    Node *head_;
    Node *tail_;
    size_t size_;

public:
    struct Iterator
    {
        using iterator_category = std::bidirectional_iterator_tag;
        // using difference_type = std::ptrdiff_t;
        using value_type = Node;
        using pointer = value_type *;
        using reference = value_type &;

        Iterator(Node *ptr) : ptr_(ptr) {}
        Iterator() : ptr_(nullptr) {}
        bool operator!=(const Iterator &itr) const { return ptr_ != itr.ptr_; }
        reference operator*() const { return *ptr_; }
        pointer operator->() { return ptr_; }
        Iterator &operator++()
        {
            ptr_ = ptr_->next;
            return *this;
        }
        Iterator operator++(int)
        {
            Iterator tmp = *this;
            ptr_ = ptr_->next;
            return tmp;
        }

    private:
        Node *ptr_;
    };

public:
    List() : head_(nullptr), tail_(nullptr), size_(0) {}
    List(const List &other) : List() { *this = other; }
    // ~List() { clear(); }
    List *parent() { return parent_; }
    Iterator begin() { return Iterator(head_); }
    Iterator end() { return Iterator(tail_); }
    Node &front()
    {
        if (!head_)
            throw std::runtime_error("front on empty");
        return *head_;
    }
    Node &back()
    {
        if (!tail_)
            throw std::runtime_error("front on empty");
        return *tail_;
    }
    void push_front(int &newData)
    {
        Node *newNode = new Node(newData);
        if (!head_)
        {
            head_ = newNode;
            tail_ = newNode;
        }
        else
        {
            newNode->next = head_;
            head_->prev = newNode;
            head_ = newNode;
        }
        ++size_;
    }
    List *push_front(List newData)
    {
        newData.parent_ = this;
        Node *newNode = new Node(newData);
        if (!head_)
        {
            head_ = newNode;
            tail_ = newNode;
        }
        else
        {
            newNode->next = head_;
            head_->prev = newNode;
            head_ = newNode;
        }
        ++size_;
        return static_cast<List *>(head_->contents);
    }
    void push_back(int newData)
    {
        Node *newNode = new Node(newData);
        if (!head_)
        {
            head_ = newNode;
            tail_ = newNode;
        }
        else
        {
            newNode->prev = tail_;
            tail_->next = newNode;
            tail_ = newNode;
        }
        ++size_;
    }
    List *push_back(List newData)
    {
        newData.parent_ = this;
        Node *newNode = new Node(newData);
        if (!head_)
        {
            head_ = newNode;
            tail_ = newNode;
        }
        else
        {
            newNode->prev = tail_;
            tail_->next = newNode;
            tail_ = newNode;
        }
        ++size_;
        return static_cast<List *>(tail_->contents);
    }
    void pop_front()
    {
    }
    void pop_back()
    {
    }
    ulong quick_sort();
    int size() const { return size_; }
    bool empty() const { return !head_; }
    // void clear() { while (head_) pop_back(); }
    std::ostream &print(std::ostream &os) const;


    const std::string print() const
    {
        std::string out = "";
        auto tmp = head_;
        while (tmp)
        {
            out += tmp->print() + ",";
            tmp = tmp->next;
        }
        return out;
    }

    friend std::ostream & operator<<(std::ostream &os, const List& l)
    {
        os << l.print();
        return os;
    }
    // for (auto i = head_; i != tail_; i = i->next)
    // i->print();
    // for (auto i = begin(); i != end(); i++)
    // i->print();

    // List() : type(Type::list) {}
    // List(int a) : contents(static_cast<void *>(new int{a})), type(Type::Int) {}
    // List(const DistressSignal::List &a) : contents(static_cast<void *>(new DistressSignal::List{a})), type(Type::list) {}
    // // void push_back(int a) {}
    // ~List() {}
};

class DistressSignal
{

public:
    DistressSignal(const char *filename)
    {
        std::ifstream file(filename);
        std::string line;
        while (file >> line)
        {
            read_line(line);
        }
    }

    List read_line(std::string line) const
    {
        List l;
        List *prev = &l;
        List *curr = &l;
        // return l;
        std::regex re("(\\[|\\]|\\d+)");
        auto begin = std::sregex_iterator(line.begin(), line.end(), re);
        auto end = std::sregex_iterator();
        for (std::sregex_iterator i = begin; i != end; ++i)
        {
            std::string match = i->str();
            // std::cout << match << std::endl;
            if (match == "[")
                curr = curr->push_back(List());
            else if (match == "]")
                curr = curr->parent();
            else
                curr->push_back(stoi(match));
        }
        std::cout << l << std::endl;
        return l;
    }
};

int main()
{
    DistressSignal ds("input.txt");
    return 1;
}