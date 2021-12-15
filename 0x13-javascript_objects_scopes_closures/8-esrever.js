exports.esrever = function (list) {
  const newList = [];
  const size = list.length;
  for (let i = 0; i < size; i++) {
    newList[i] = list[size - (i + 1)];
  }
  return (newList);
};
