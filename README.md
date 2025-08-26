# Data Structures and Algorithms Repository

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A comprehensive collection of data structures and algorithms implemented in **Java** and **Python**, featuring detailed explanations, complexity analysis, practical examples, and visualizations.

<p align="center">
  <img src="https://i.imgur.com/waxVImv.png" alt="DSA Visualization" width="800">
</p>

## 📋 Table of Contents

- [Overview](#overview)
- [Data Structures](#data-structures)
- [Algorithms](#algorithms)
- [Visualizations](#visualizations)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)

## Overview

This repository contains implementations of various data structures and algorithms with clean, readable code and thorough documentation. The goal is to provide a learning resource for computer science students and developers preparing for technical interviews.

## Data Structures

### Primitive Types
| Data Structure | Java | Python | Visualization |
|----------------|:----:|:------:|:------------:|
| Arrays | ✅ | ✅ | 📊 |
| Strings | ✅ | ✅ | 📊 |
| Linked Lists (Singly, Doubly, Circular) | ✅ | ✅ | 🔗 |
| Stacks | ✅ | ✅ | 🥞 |
| Queues (Simple, Priority, Circular) | ✅ | ✅ | 📥 |
| Hash Tables | ✅ | ✅ | 🗃️ |
| Trees (Binary, BST, AVL, Heap) | ✅ | ✅ | 🌳 |
| Graphs (Adjacency List, Matrix) | ✅ | ✅ | 📊 |

### Advanced
| Data Structure | Java | Python | Visualization |
|----------------|:----:|:------:|:------------:|
| Segment Trees | ✅ | ✅ | 📐 |
| Fenwick Trees | ✅ | ✅ | 🔢 |
| Trie | ✅ | ✅ | 🔤 |
| Skip Lists | 🚧 | 🚧 | ⛷️ |

## Algorithms

### Sorting Algorithms
| Algorithm | Java | Python | Visualization |
|-----------|:----:|:------:|:------------:|
| Bubble Sort | ✅ | ✅ | 🔴🟠🟡🟢🔵 |
| Selection Sort | ✅ | ✅ | 🔴🟠🟡🟢🔵 |
| Insertion Sort | ✅ | ✅ | 🔴🟠🟡🟢🔵 |
| Merge Sort | ✅ | ✅ | 🔴🟠🟡🟢🔵 |
| Quick Sort | ✅ | ✅ | 🔴🟠🟡🟢🔵 |
| Heap Sort | ✅ | ✅ | 🔴🟠🟡🟢🔵 |

### Searching Algorithms
| Algorithm | Java | Python | Visualization |
|-----------|:----:|:------:|:------------:|
| Linear Search | ✅ | ✅ | 🔍 |
| Binary Search | ✅ | ✅ | 🔍 |
| Depth-First Search (DFS) | ✅ | ✅ | 🌀 |
| Breadth-First Search (BFS) | ✅ | ✅ | 🌀 |
| A* Search Algorithm | ✅ | ✅ | 🧭 |

### Graph Algorithms
| Algorithm | Java | Python | Visualization |
|-----------|:----:|:------:|:------------:|
| Dijkstra's Algorithm | ✅ | ✅ | 🗺️ |
| Bellman-Ford Algorithm | ✅ | ✅ | 🗺️ |
| Floyd-Warshall Algorithm | ✅ | ✅ | 🗺️ |
| Prim's Algorithm | ✅ | ✅ | 🌐 |
| Kruskal's Algorithm | ✅ | ✅ | 🌐 |
| Topological Sorting | ✅ | ✅ | 📊 |

### Dynamic Programming
| Algorithm | Java | Python | Visualization |
|-----------|:----:|:------:|:------------:|
| Fibonacci Sequence | ✅ | ✅ | 📈 |
| Knapsack Problem | ✅ | ✅ | 🎒 |
| Longest Common Subsequence | ✅ | ✅ | 📝 |
| Longest Increasing Subsequence | ✅ | ✅ | 📈 |
| Coin Change Problem | ✅ | ✅ | 💰 |


To run visualizations:
```bash
# For Python visualizations
cd visualizations/python
python sorting_visualizer.py

# For Java visualizations
cd visualizations/java
javac GraphVisualizer.java
java GraphVisualizer
```

## Project Structure

```
data-structures-algorithms/
│
├── data-structures/
│   ├── arrays/
│   │   ├── java/Array.java
│   │   ├── python/array.py
│   │   └── visualizations/array_visualization.py
│   ├── linked-lists/
│   │   ├── java/SinglyLinkedList.java
│   │   ├── python/singly_linked_list.py
│   │   └── visualizations/linked_list_visualization.py
│   └── trees/
│       ├── java/BinarySearchTree.java
│       ├── python/binary_search_tree.py
│       └── visualizations/tree_visualization.py
│
├── algorithms/
│   ├── sorting/
│   │   ├── java/MergeSort.java
│   │   ├── python/merge_sort.py
│   │   └── visualizations/sorting_visualizer.py
│   ├── searching/
│   │   ├── java/BinarySearch.java
│   │   ├── python/binary_search.py
│   │   └── visualizations/search_visualizer.py
│   └── graph-algorithms/
│       ├── java/Dijkstra.java
│       ├── python/dijkstra.py
│       └── visualizations/graph_visualizer.py
│
├── problems/
│   ├── leetcode/
│   ├── hackerrank/
│   └── codeforces/
│
├── docs/
│   ├── complexity-cheatsheet.md
│   └── interview-prep.md
│
├── tests/
│   ├── java/
│   └── python/
│
└── utilities/
    ├── generators/
    └── visualizers/
```

## Getting Started

### Prerequisites
- Java JDK 11 or higher
- Python 3.8 or higher
- matplotlib (for Python visualizations)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/data-structures-algorithms.git
cd data-structures-algorithms
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Running Examples
```bash
# Run Java example
cd data-structures/linked-lists/java
javac SinglyLinkedList.java
java SinglyLinkedList

# Run Python example
cd algorithms/sorting/python
python merge_sort.py
```

### Running Tests
```bash
# Run Java tests
cd tests/java
javac TestRunner.java
java TestRunner

# Run Python tests
cd tests/python
python -m unittest discover
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow the existing code style and naming conventions
- Add comments to explain complex logic
- Include test cases for new implementations
- Update the README.md if necessary
- Ensure your code passes all tests


### Practice Platforms
- [LeetCode](https://leetcode.com/)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by the DSA Community
</p>

<p align="center">
  <img src="https://i.imgur.com/m3GxT7W.png" alt="DSA Logo" width="200">
</p>
