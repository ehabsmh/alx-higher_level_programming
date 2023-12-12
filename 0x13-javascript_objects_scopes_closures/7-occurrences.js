#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const occElement = list.filter((value) => value === searchElement);
  return (occElement.length);
};
