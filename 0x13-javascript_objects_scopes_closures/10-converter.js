#!/usr/bin/node

exports.converter = function (base) {
  return nb => nb.toString(base);
};
