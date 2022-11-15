// Floyd`s Tortoise And Hare
// Time Complexity: O(n), Space Complexity: O(n) -> O(1)
// 거북이와 토끼가 만나면 연결 리스트에 사이클이 존재하는 것이다!

const findCycle = (head) => {
  let hare = head;
  let tortoise = head;

  while (true) {
    hare = hare.next;
    tortoise = tortoise.next;

    if (hare === null || hare.next === null) {
      return false;
    } else {
      hare = hare.next;
    }

    // 거북이와 토끼가 만나는 지점
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

  return p1; // 사이클이 시작되는 지점 (p1 === p2)
};
