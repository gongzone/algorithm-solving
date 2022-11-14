// const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// const commands = inputs.slice(1, inputs.length);

const commands = [
  'push 1',
  'push 2',
  'top',
  'size',
  'empty',
  'pop',
  'pop',
  'pop',
  'size',
  'empty',
  'pop',
  'push 3',
  'empty',
  'top',
];

class Stack {
  data;
  length;

  constructor() {
    this.data = [];
    this.length = 0;
  }

  push(item) {
    this.data.push(item);
    this.length++;
  }

  pop() {
    if (this.length === 0) {
      return -1;
    }

    this.length--;
    return this.data.pop();
  }

  size() {
    return this.length;
  }

  empty() {
    return this.length === 0 ? 1 : 0;
  }

  top() {
    if (this.length === 0) {
      return -1;
    }

    return this.data[this.length - 1];
  }
}

const emitResult = (commands) => {
  const stack = new Stack();
  const answer = [];

  const actions = {
    push: (x) => stack.push(x),
    pop: () => stack.pop(),
    size: () => stack.size(),
    empty: () => stack.empty(),
    top: () => stack.top(),
  };

  commands.forEach((command) => {
    if (command.startsWith('push')) {
      actions.push(parseInt(command.split(' ')[1]));
    } else {
      answer.push(actions[command]());
    }
  });

  return answer;
};

console.log(emitResult(commands).join('\n'));
