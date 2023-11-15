#!/usr/bin/node

// function increaments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
