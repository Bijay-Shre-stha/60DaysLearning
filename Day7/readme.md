## **Tuples**

- Tuples are ordered collection of items.
- Tuples are immutable, i.e., the items in a tuple cannot be changed.
- Tuple items are ordered, unchangeable, and allow duplicate values.
- Tuples are defined using parentheses `()`.
- Tuples can contain items of different data types.
- Tuples can be used as keys in dictionaries.
- Tuples are faster than lists.
- Tuples are used to store related pieces of information together.
- Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
  - Convert into list
  - Add tuple to the tuple
- Removing items ``del tuple_name`` will delete the entire tuple.
- Unpacking a tuple: Unpacking a tuple allows you to assign the items in a tuple to a variable.
- Using the `*` operator to unpack a tuple: The `*` operator can be used to unpack a tuple and assign the remaining items to a variable.
- Using the `+` operator to combine tuples: The `+` operator can be used to combine two or more tuples.
- Looping through a tuple: `for item in tuple_name:`
- Tuple methods:
  - `count()`: Returns the number of times a specified value occurs in a tuple.
  - `index()`: Searches the tuple for a specified value and returns the position of where it was found.

## **Sets**

- Sets are used to store multiple items in a single variable.
- Sets is a collection which is unordered, unchangeable*, and unindexed.
- Sets are defined using curly braces `{}`.
- Sets are unordered, so the items will appear in a random order.
- Sets are unchangeable, meaning that we cannot change the items after the set has been created.
- Sets do not allow duplicate values.
- Sets can contain items of different data types.
- Sets are used to store unique values.
- Sets are used to perform mathematical set operations like union, intersection, symmetric difference, etc.
- The values  `True` and `False` are considered as `1` and `0` respectively.
- Set constructor: `set()` used to create a set.
- Adding on set:
  - `add()`: Adds an element to the set.
  - `update()`: Adds multiple elements to the set.

- Removing items from set:
  - `remove()`: Removes the specified element.
  - `discard()`: Remove the specified item.
  - `pop()`: Removes an element from the set.
  - `clear()`: Removes all the elements from the set.

- Set methods:
  - `add()`: Adds an element to the set.
  - `clear()`: Removes all the elements from the set.
  - `copy()`: Returns a copy of the set.
  - `difference()`: Returns a set containing the difference between two or more sets.

    - Shortcut: `set1 - set2`

  - `difference_update()`: Removes the items in this set that are also included in another, specified set.

    - Shortcut: `set1 -= set2`

  - `discard()`: Remove the specified item.
  - `intersection()`: Returns a set, that is the intersection of two other sets.

    - Shortcut: `set1 & set2`

  - `intersection_update()`: Removes the items in this set that are not present in other, specified set(s).

    - Shortcut: `set1 &= set2`

  - `isdisjoint()`: Returns whether two sets have a intersection or not.
  - `issubset()`: Returns whether another set contains this set or not.

    - Shortcut: `set1 <= set2`
    - Shortcut: `set1 < set2`

  - `issuperset()`: Returns whether this set contains another set or not.

    - Shortcut: `set1 >= set2`
    - Shortcut: `set1 > set2`

  - `pop()`: Removes an element from the set.
  - `remove()`: Removes the specified element.
  - `symmetric_difference()`: Returns a set with the symmetric differences of two sets.

    - Shortcut: `set1 ^ set2`

  - `symmetric_difference_update()`: Inserts the symmetric differences from this set and another.

    - Shortcut: `set1 ^= set2`

  - `union()`: Return a set containing the union of sets.

    - Shortcut: `set1 | set2`

  - `update()`: Update the set with the union of this set and others.

    - Shortcut: `set1 |= set2`

## **Summary**

- Tuples are ordered, unchangeable, and allow duplicate values.
- Sets are unordered, unchangeable, and do not allow duplicate values.
- Tuples are defined using parentheses `()`.
- Sets are defined using curly braces `{}`.
- Tuples are faster than lists.
- Sets are used to store unique values.
- Tuples are used to store related pieces of information together.
- Sets are used to perform mathematical set operations like union, intersection, symmetric difference, etc.
- Tuples are immutable, i.e., the items in a tuple cannot be changed.
- Sets are unchangeable, meaning that we cannot change the items after the set has been created.
- Tuples can be used as keys in dictionaries.
- The values `True` and `False` are considered as `1` and `0` respectively on `set`.
- Tuples and Sets can contain items of different data types.
