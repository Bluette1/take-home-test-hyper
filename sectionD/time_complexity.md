## Option 2: Time Complexity

### Worst-case time complexity of the “Collection.add” method
The worst-case time complexity is *O(n)*
Either we are adding items to the front, in the middle or at the end of the collection. In the best case scenario we are adding to the front which case we don't have to iterate through the whole list. In the worst case scenario we have to iterate through each element of the collection until we reach the end which gives O(n) time complexity.  

### At least two alternative designs that would improve the worst-case time

●  We can keep a pointer/reference to the tail(end) of the collection so that we don't always have to traverse through the whole collection before we add a new item.
● We can decide to add the items to the front/head of the list, instead of adding to the end/tail.


### The worst-case time complexity of the alternative designs.
In each of the above alternative designs, the worst-case time complexity of the “Collection.add” method would be O(1)/Constant time because we would be able to directly access the point where we are adding the new item.
