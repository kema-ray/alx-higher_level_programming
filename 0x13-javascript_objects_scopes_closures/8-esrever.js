#!/usr/bin/node

exports.esrever = function (list) {
	const i = list.length;
	const reverseList = new Array(i);

	list.forEach((item, n) => {
			reverseList[i - n - 1] = item;
			});
	return reverseList;
};
