#!/usr/bin/node
// Returns the number of occurrences in a list
exports.nbOccurrences = function (list, searchElement) {
  return list.filter((element) => element === searchElement).length;
};
