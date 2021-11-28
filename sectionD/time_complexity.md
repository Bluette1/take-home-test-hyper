# Option 2: Time Complexity

## Worst-case time complexity of the “Collection.add” method
The worst-case time complexity is **O(n)**/Linear time
  * Explanation: - Either we are adding items to the front, in the middle or at the end of the collection. In the best case scenario we are adding to the front which case we don't have to iterate through the whole list. In the worst case scenario we have to iterate through each element of the collection until we reach the end which gives O(n) time complexity.  

## At least two alternative designs that would improve the worst-case time

*  We can keep a pointer/reference to the head and tail(end) of the collection so that we don't always have to traverse through the whole collection before adding a new item. Each time after adding a new item we can point the tail to the last added node. If create a Node class

 class Node {
  #value;
  #next;
  constructor(value, next) {
    this.#value = value;
    if (next) this.#next = new Collection(next);
    else this.#next = null;
  }
  get value() {
    return this.#value;
  }
  get next() {
    return this.#next;
  }

 }

We can modify our add method as follows:

```
class Collection {
#head = null
#tail = null

add(value) {
    let next;
    for (next = this.#next; next && next.#next; next = next.#next);
    if (!next) next = this;
    next.#next
    
    let newNode = new Node(value); 
    if (this.#head) { // Collection is empty
      this.#head = newNode
      this.#tail = newNode

    } else {
      this.tail.#next = newNode
      this.#tail = newNode //Point the tail to the last node
    }
    
  }

}
```
* We can decide to add the items to the front/head of the list, instead of adding to the end/tail.
* We can also use a doubly linked collection by using to references/pointers:
one reference pointing to the next node as well as another reference pointing to the previous one. in this way we are able to move other forwards or backwards and can add items at the head or tail easily. We can set it up in the constructor as follows:

```
#value;
#next;
#prev // Pointer to the previous node
  constructor(value, next, prev) {
    this.#value = value;
    if (next) this.#next = new    Collection(next);
    else this.#next = null;

    // Also set up the reference to the previous node
      if (prev) this.#prev = new Collection(prev);
    else this.#prev = null;
  }
  ```



## The worst-case time complexity of the alternative designs.
In each of the above alternative designs, the worst-case time complexity of the “Collection.add” method would be **O(1)**/Constant time because we would be able to directly access the point where we are adding the new item.
