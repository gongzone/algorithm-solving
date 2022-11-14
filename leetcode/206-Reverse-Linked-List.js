// Given the head of a singly linked list, reverse the list, and return the reversed list.

/*
  Input: head = [1,2,3,4,5]
  Output: [5,4,3,2,1]
*/

// T: O(n), S: O(1) 
const reverseLinkedList = (head) => {
  let prev = null;
  let current = head;

  while(current) {
    let next = current.next;
    
    current.next = prev;
    prev = current
    current = next;
  }

  return prev;
}