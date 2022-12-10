/**
 * @file Tree.h
 * @author Erik Giesen
 *
**/

#pragma once

#include <iostream>  // for std::cout
#include <stdexcept> // for std::runtime_error
#include <utility>   // std::swap
#include <stack>     // for iterative in-order traversal

template <typename K, typename Comp = std::less<K>>
class Tree
{
protected:
  class Node
  {
  public:
    const K key;
    Node *left;  // pointer to the left child
    Node *right; // pointer to the right child

    Node() : left(nullptr), right(nullptr) {}
    Node(const K &newKey) : key(newKey), left(nullptr), right(nullptr) {}
    ~Node() {}
  };

protected:
  Comp comp;
  Node *root_;
  size_t size_;

public:
  Tree() : root_(nullptr), size_(0) {}
  Tree(const Tree<K, Comp> &other) : Tree() { *this = other; }
  Tree(std::initializer_list<K> init) : Tree() { for (K obj : init) insert(obj); }
  ~Tree() { clear(); }
  void insert(const K &newKey);      // O(h)
  void erase(const K &key);          // O(h)
  bool count(const K &key) const { return (bool)_find(key, root_); }

  K min();
  K max(); 
  K popMin();
  K popMax();

  size_t size() const { return size_; }
  bool empty() const { return !root_; }
  void clear() {while (root_) erase(root_->key); }
  std::ostream &print(std::ostream &os) const;

private:
  Node *&_find(const K &key, Node *&node) const;
  void _erase(Node *&node);
  Node *&_predecessor(Node *&node) const;
  Node *&_succ(Node *&node) const;
  Node *&_rightmost_of(Node *&node) const;
  Node *&_leftmost_of(Node *&node) const;
  Node *&_swap(Node *&node1, Node *&node2) const;
};

// =======================================================================
// Class implementation part 1 - the basics
// =======================================================================

template <typename K, typename Comp>
void Tree<K, Comp>::insert(const K &newKey)
{
  Node *&node = _find(newKey, root_);
  if (node) // If node is not a nullptr, the key already exists!
    throw std::runtime_error("insert() used on an existing key");
  node = new Node(newKey);
  ++size_;
}

template <typename K, typename Comp>
typename Tree<K, Comp>::Node *&Tree<K, Comp>::_find(const K &key, Node *&node) const
{
  if (node == nullptr)
    return node;
  else if (node->key == key)
    return node;
  else if (comp(key, node->key)) // Default: key < node->key
    return _find(key, node->left);
  else
    return _find(key, node->right);
}

template <typename K, typename Comp>
void Tree<K, Comp>::erase(const K &key)
{
  Node *&node = _find(key, root_);
  if (!node) // If node is a nullptr, the key does not exist!
    throw std::runtime_error("erase() used on non-existing key");
  _erase(node);
}

template <typename K, typename Comp>
void Tree<K, Comp>::_erase(Node *&node)
{
  if (!node->left && !node->right)
  { // Node has no children (easy case)
    delete node;
    node = nullptr;
  }
  else if (node->right && !node->left)
  { // Node has a right child (medium case)
    Node *temp = node;
    node = node->right;
    delete temp;
    temp = nullptr;
  }
  else if (node->left && !node->right)
  { // Node has a left child (medium case)
    Node *temp = node;
    node = node->left;
    delete temp;
    temp = nullptr;
  }
  else
  { // Node has two children (difficult case)
    Node *&pred = _predecessor(node);      // Easy
    Node *&moved_node = _swap(node, pred); // Difficult
    _erase(moved_node);                    // Easy or medium case only
  }
  --size_;
}

template <typename K, typename Comp>
typename Tree<K, Comp>::Node *&Tree<K, Comp>::_predecessor(Node *&node) const
{
  if (!node) // Case 1: node is nullptr
    return node;
  if (!node->left) // Case 2: node does not have left subtree
    return node->left;
  return _rightmost_of(node->left); // Case 3: node has a left subtree
}

template <typename K, typename Comp>
typename Tree<K, Comp>::Node *&Tree<K, Comp>::_rightmost_of(Node *&node) const
{
  if (!node) // Base case 1: node is nullptr
    return node;
  if (!node->right) // Base case 2: node is the rightmost node
    return node;
  return _rightmost_of(node->right); // Keep going right
}

template <typename K, typename Comp>
typename Tree<K, Comp>::Node *&Tree<K, Comp>::_succ(Node *&node) const
{
  if (!node) // Case 1: node is nullptr
    return node;
  if (!node->right) // Case 2: node does not have right subtree
    return node->right;
  return _leftmost_of(node->right); // Case 3: node has a right subtree
}

template <typename K, typename Comp>
typename Tree<K, Comp>::Node *&Tree<K, Comp>::_leftmost_of(Node *&node) const
{
  if (!node) // Base case 1: node is nullptr
    return node;
  if (!node->left) // Base case 2: node is the leftmost node
    return node;
  return _leftmost_of(node->left); // Keep going left
}

template <typename K, typename Comp>
typename Tree<K, Comp>::Node *&Tree<K, Comp>::_swap(Node *&node1, Node *&node2) const
{
  Node *orig_node1 = node1;
  Node *orig_node2 = node2;
  if (node1->left == node2)
  { // node1 has node2 as its left child
    std::swap(node1->right, node2->right);
    node1->left = orig_node2->left;
    orig_node2->left = node1;
    node1 = orig_node2;
    return node1->left;
  }
  else if (node1->right == node2)
  { // node1 has node2 as its right child
    std::swap(node1->left, node2->left);
    node1->right = orig_node2->right;
    orig_node2->right = node1;
    node1 = orig_node2;
    return node1->right;
  }
  else if (node2->left == node1)
  { // node2 has node1 as its left child
    std::swap(node2->right, node1->right);
    node2->left = orig_node1->left;
    orig_node1->left = node2;
    node2 = orig_node1;
    return node2->left;
  }
  else if (node2->right == node1)
  { // node2 has node1 as its right child
    std::swap(node2->left, node1->left);
    node2->right = orig_node1->right;
    orig_node1->right = node2;
    node2 = orig_node1;
    return node2->right;
  }
  else
  { // The two nodes are not adjacent
    std::swap(node1->left, node2->left);   // Swap left children
    std::swap(node1->right, node2->right); // Swap right children
    std::swap(node1, node2);               // Swap main pointers
    return node2;                          // node2 now points to original node1
  }
}

template <typename K, typename Comp>
std::ostream &Tree<K, Comp>::print(std::ostream &os) const
{ // Iterative in-order traversal
  std::stack<Node *> s;
  Node *node = root_;
  while (node || !s.empty())
  { // Keep adding left children to the stack
    while (node)
    {
      s.push(node);
      node = node->left;
    }
    // Keep popping nodes until a right child is found
    node = s.top();
    s.pop();
    os << node->key << " ";
    // If the right child is not null, add all tis left children to the stack
    node = node->right;
  }
  return os;
}

// Operator overload that allows stream output syntax, such as with std::cout
template <typename K, typename Comp>
std::ostream &operator<<(std::ostream &os, const Tree<K, Comp> &Tree)
{
  return Tree.print(os);
}

#include "Tree.hpp"