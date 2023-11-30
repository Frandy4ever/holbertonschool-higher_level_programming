#!/usr/bin/node
// Clone the original list to avoid modifying it directly

exports.esrever = function (list) {
  const reversedList = [...list];

  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }

  return reversedList;
};
