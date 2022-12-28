#include <fstream>
#include <iostream>
// #include <list>
#include <regex>
#include <iterator>
#include <algorithm>

class List
{
private:
    class Node
    {
    public:
        int *int_ptr;
        List *list_ptr;
        Node *prev;
        Node *next;

    public:
        Node() : list_ptr(nullptr), int_ptr(nullptr), prev(nullptr), next(nullptr) {}
        Node(int a) : int_ptr(new int{a}), list_ptr(nullptr), prev(nullptr), next(nullptr) {}
        Node(const List &a) : int_ptr(nullptr), list_ptr(new List{a}), prev(nullptr), next(nullptr) {}
        std::string print() const { return (int_ptr)? std::to_string(*int_ptr) : "[" + list_ptr->print() + "]"; }
        ~Node()
        {
            // if (list_ptr)
            // {
            //     std::cout << "Deleting" << *list_ptr << std::endl;
            //     delete list_ptr;
            //     list_ptr = nullptr;
            //     return;
            // }
            // if (int_ptr)
            // {
            //     std::cout << "Deleting" << *int_ptr << std::endl;
            //     delete int_ptr;
            //     int_ptr = nullptr;
            // }
        }
        bool operator<(const Node &node) const 
        {
            if (int_ptr && node.int_ptr)
                return *int_ptr < *(node.int_ptr);
            if (list_ptr && node.int_ptr)
                return *list_ptr < List(*(node.int_ptr));
            if (int_ptr && node.list_ptr)
                return List(*int_ptr) < *(node.list_ptr);
            return false;
        };
    };
    List *parent_;
    Node *head_;
    Node *tail_;
    size_t size_;

public:
    struct Iterator
    {
        using iterator_category = std::bidirectional_iterator_tag;
        using value_type = Node;
        using pointer = value_type *;
        using reference = value_type &;

        Iterator() : ptr_(nullptr) {}
        Iterator(Node *ptr) : ptr_(ptr) {}
        bool operator==(const Iterator &itr) const = default;
        reference operator*() const { return *ptr_; }
        pointer operator->() { return ptr_; }
        bool operator!() {return ptr_; }
        Iterator &operator++() { ptr_ = ptr_->next; return *this; }
        Iterator &operator--() { ptr_ = ptr_->prev; return *this; }
        Iterator operator++(int) { auto tmp = *this; ptr_ = ptr_->next; return tmp; }
        Iterator operator--(int) { auto tmp = *this; ptr_ = ptr_->prev; return tmp; }
        Iterator operator-(unsigned other)
        {
            Iterator k(ptr_);
            for (size_t i = 0; i < other; ++i)
                ++k;
            return k;
        }
        unsigned operator-(Iterator other)
        {
            unsigned k = 0;
            for (auto i = ptr_; i != other.ptr_; ++i)
                ++k;
            return k;
        }

    private:
        Node *ptr_;
    };

public:
    List() : parent_(this), head_(nullptr), tail_(nullptr), size_(0) {}
    List(const int &new_int) : List() { push_back(new_int); }
    // List(const List &other) : List() { *this = other; }
    // List(const List &new_list) : List() { push_back(new_list); }
    List &operator=(const List &other)
    {
        clear();
        for (auto i = other.begin(); i != other.end(); ++i)
            push_back((i->int_ptr)? *(i->int_ptr) : *(i->list_ptr));
        return *this;
    }
    bool operator<(const List& other)
    {
        auto i = begin();
        auto j = other.begin();
        for (size_t k = 0; k < std::max(size(), other.size()); ++k)
        {
            if (!i) return true;
            if (!j) return false;
            if (*i < *j) return true;
            if (*j < *i) return false;
            ++i;
            ++j;
        }
        return false;
    }
    ~List() { clear(); }
    Iterator begin() const { return Iterator(head_); }
    Iterator end() const { return Iterator(nullptr); }
    bool empty() const { return !head_; }
    int size() const { return size_; }
    void clear() { while (head_) pop_back(); }
    List *parent() { return parent_; }

    Node &front() const
    {
        if (!head_)
            throw std::runtime_error("front() on empty list");
        return *head_;
    }
    Node &back() const
    {
        if (!tail_)
            throw std::runtime_error("back() on empty list");
        return *tail_;
    }
    void push_front(int &new_data)
    {
        Node *new_node = new Node(new_data);
        if (!head_)
        {
            head_ = new_node;
            tail_ = new_node;
        }
        else
        {
            head_->prev = new_node;
            new_node->next = head_;
            head_ = new_node;
        }
        ++size_;
    }
    List *push_front(List new_data)
    {
        new_data.parent_ = this;
        Node *new_node = new Node(new_data);
        if (!head_)
        {
            head_ = new_node;
            tail_ = new_node;
        }
        else
        {
            head_->prev = new_node;
            new_node->next = head_;
            head_ = new_node;
        }
        ++size_;
        return (head_->list_ptr);

        // return static_cast<List *>(head_->contents);
    }
    void push_back(int new_data)
    {
        Node *new_node = new Node(new_data);
        if (!head_)
        {
            head_ = new_node;
            tail_ = new_node;
        }
        else
        {
            tail_->next = new_node;
            new_node->prev = tail_;
            tail_ = new_node;
        }
        ++size_;
    }
    List *push_back(List new_data)
    {
        new_data.parent_ = this;
        Node *new_node = new Node(new_data);
        if (!head_)
        {
            head_ = new_node;
            tail_ = new_node;
        }
        else
        {
            tail_->next = new_node;
            new_node->prev = tail_;
            tail_ = new_node;
        }
        ++size_;
        return (tail_->list_ptr);
        // return static_cast<List *>(tail_->contents);
    }
    void pop_front()
    {
        if (!head_)
            throw std::runtime_error("pop_front() on empty List");
        if (!head_->next)
        {
            delete head_;
            head_ = nullptr;
            tail_ = nullptr;
        }
        else
        {
            auto tmp = head_;
            head_ = head_->next;
            delete tmp;
            head_->prev = nullptr;
            // tmp = nullptr;
        }
        --size_;
    }
    void pop_back()
    {
        if (!tail_)
            throw std::runtime_error("pop_front() on empty List");
        if (!tail_->prev)
        {
            delete head_;
            head_ = nullptr;
            tail_ = nullptr;
        }
        else
        {
            auto tmp = tail_;
            tail_ = tail_->prev;
            delete tmp;
            tail_->next = nullptr;
            // tmp = nullptr;
        }
        --size_;
    }
    ulong quick_sort();


    const std::string print() const
    {
        std::string out = "";
        auto tmp = head_;
        for (auto i = begin(); i != end(); ++i)
            out += i->print() + ",";
        return out;
    }

    friend std::ostream &operator<<(std::ostream &os, const List &l)
    {
        os << l.print();
        return os;
    }
};

class DistressSignal
{
public:
    DistressSignal(const char *filename)
    {
        List l;
        l.push_back(read_line("[[2]]"));
        l.push_back(read_line("[[6]]"));
        std::ifstream file(filename);
        std::string line;
        while (file >> line)
            l.push_back(read_line(line));
        std::sort(l.begin(), l.end());
        // auto a = std::find(l.begin(), l.end(), read_line("[[2]]"));
        // auto b = std::find(l.begin(), l.end(), read_line("[[6]]"));
        // std::cout << a << std::endl;
        // std::cout << b << std::endl;
    }

    List read_line(std::string line) const
    {
        List l;
        List *curr = &l;
        List *prev = &l;
        std::regex re("(\\[|\\]|\\d+)");
        auto begin = std::sregex_iterator(line.begin(), line.end(), re);
        auto end = std::sregex_iterator();
        for (std::sregex_iterator i = begin; i != end; ++i)
        {
            std::string match = i->str();
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
    DistressSignal ds("simple.txt");
    return 1;
}