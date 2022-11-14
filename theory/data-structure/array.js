// Array: 항목들을 순서에 따라 정리해놓은 자료구조. (One after another in memory)

// Operations:
// - search O(n)
// - lookup O(1)
// - push(append) O(1) * can be O(n) in dynamic array
// - insert O(n)
// - delete O(n)

// static array: 할당할 수 있는 메모리 사이즈 고정
// dynamic array: 할당할 수 있는 메모리 가변 - 기존 array copy 후 새 장소에 더 많은 메모리를 할당하여 새로운 array build

class MyArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index];
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop() {
    const lastItem = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;

    return lastItem;
  }

  delete(index) {
    const item = this.data[index];
    this.#shiftItems(index);
    return item;
  }

  #shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }

    delete this.data[this.length - 1];
    this.length--;
  }
}

const newArray = new MyArray();

newArray.push('hi');
newArray.push('you');
newArray.push('!');
newArray.delete(0);
newArray.push('are');
newArray.push('nice');
newArray.delete(1);
// newArray.pop();

console.log(newArray);
