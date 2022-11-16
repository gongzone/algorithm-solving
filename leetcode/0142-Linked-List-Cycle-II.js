// Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
// Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed).
// It is -1 if there is no cycle. Note that pos is not passed as a parameter.

// Do not modify the linked list.

/* 
  Input: head = [3,2,0,-4], pos = 1
  Output: tail connects to node index 1
  Explanation: There is a cycle in the linked list, where tail connects to the second node.
*/

// T: O(n), S: O(n)
const findCycle = (head) => {
  if (!head) return null;

  let currentNode = head;
  const seenNodes = new Set();

  while (!seenNodes.has(currentNode)) {
    if (currentNode.next === null) {
      return null;
    }

    seenNodes.add(currentNode);
    currentNode = currentNode.next;
  }

  return currentNode;
};

// Floyd`s Tortoise and Hare Algorithm
// T: O(n), S: O(1)
const findCycleOptimized = (head) => {
  if (!head) return null;

  let hare = head;
  let tortoise = head;

  while (true) {
    hare = hare.next;
    tortoise = tortoise.next;

    if (hare === null || hare.next === null) {
      return null;
    } else {
      hare = hare.next;
    }

    if (tortoise === hare) {
      break;
    }
  }

  let p1 = head;
  let p2 = tortoise;

  while (p1 !== p2) {
    p1 = p1.next;
    p2 = p2.next;
  }

  return p1;
};
