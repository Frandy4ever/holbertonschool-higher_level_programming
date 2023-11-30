#!/usr/bin/node
// Returns the number of occurrences in a list
exports.nbOccurrences = function (list, searchElement) {
  const occurrences = list.reduce((count, element) => {
    return element === searchElement ? count + 1 : count;
  }, 0);

  return occurrences;
};
