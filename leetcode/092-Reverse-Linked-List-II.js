// Given the head of a singly linked list and two integers left and right where left <= right,
// reverse the nodes of the list from position left to position right, and return the reversed list.

/*
  Input: head = [1,2,3,4,5], left = 2, right = 4
  Output: [1,4,3,2,5]
*/

// T: O(n), S: O(1)
const reverseBetween = (head, left, right) => {
  let currentPosition = 1;
  let currentNode = head;
  let start = head; // left-1

  while (currentPosition < left) {
    start = currentNode;
    currentNode = currentNode.next;
    currentPosition++;
  }

  let newList = null; // right, reversed
  let tail = currentNode; // left, reversed

  while (currentPosition >= left && currentPosition <= right) {
    const next = currentNode.next;
    currentNode.next = newList;
    newList = currentNode;
    currentNode = next;
    currentPosition++;
  }

  start.next = newList;
  tail.next = currentNode; // currentNode: n+1

  if (left > 1) {
    return head;
  } else {
    return newList;
  }
};
