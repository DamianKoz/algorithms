# Arrays vs Linked Lists

Arrays and Linked Lists are the two most basic data structures. Each comes has its own benefits and disadvantages.

- [Arrays vs Linked Lists](#arrays-vs-linked-lists)
- [Arrays](#arrays)
- [Linked Lists](#linked-lists)
- [Runtimes for Arrays vs Linked Lists](#runtimes-for-arrays-vs-linked-lists)
- [Use Cases](#use-cases)
  - [Insertion and Deletion](#insertion-and-deletion)

# Arrays

Arrays are a data structure with a relatively fixed size.

If you want to store three numbers in an array, your programm will probably safe three spaces in memory.

his is great for fast access because if you want to see the second element, your programm can directly jump to that place in memory, because it knows where to look.

A problem arises, if you have more items than space allocated. If you reserved three spaces but want to add a fourth element, you have to move everything into a new array with four reserved spaces.

So arrays are great for quick access (reads), but rather inefficient for storing flexibel amounts of data (writes).

# Linked Lists

Linked Lists work in a different way.

They can be at random locations in memory, and you navigate through it by storing the address of the next element in every element.

Therefore the name linked list, because every element is linked to the next one.

So if you want to get the third element you have to start at the beginning, then look where the next one is and then go to the third one. You can't instantly jump to the third element.

So they are great if you have to go through every element anyways.

# Runtimes for Arrays vs Linked Lists

|           | Arrays | Lists |
| --------- | ------ | ----- |
| Reading   | O(1)   | O(n)  |
| Inserting | O(n)   | O(1)  |
|           |        |       |

# Use Cases

## Insertion and Deletion

If many insertions are needed, then linked lists are the better option. It is as easy as changing the address of element to point to the new one and the new one to point to the next one. Constant Insertion Time.

For arrays this process is far worse, because you have to move every element after the new one down and maybe even to move the whole array if the reserved space is not enough.
