// Version : 1.1.1.02
// Date : 2023/10/21 21:30
// Author : Long17369
var word = {
	'count': 0,
	'understand': [],
	'word': [],
	'Version': { 'time': undefined },
	'understanded': {
		'认识': [],
		'不认识': [],
		'finish': true
	},
	'Words': [],
	'randomNumber': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
	'next': [false],
	'Next': false
};
$.ajax({
	type: "get", //使用get方式
	url: "../word/word.json", //json文件相对于这个HTML的路径
	dataType: "json",
	success: function (data) {
		word.Words = data;
		for (const i in word.Words) {
			for (const j in word.Words[i].word) {
				// var exist = false;
				// for (const k in word.word) {
				// 	if (word.word[k] == word.Words[i].word[j]) {
				// 		exist = true;
				// 		// console.log(word.word[k]);
				// 		// console.log(word.Words[i].word[j]);
				// 	};
				// };
				if (word.word.some(ele => ele == word.Words[i].word[j])) { }
				// if (exist){}
				else {
					word.word.push(word.Words[i].word[j])
				};
			};
		};
		//这个data就是json数据
	},
	error: function () {
		alert("请求失败");
	}
});
function select() {
	for (let i = 0; i < 10; i++) {
		while (!word.Next) {
			word.randomNumber[i] = Math.floor(Math.random() * word.word.length);
			console.log(word.randomNumber)
			for (const j in word.randomNumber) {
				if (i !== j) {
					word.next[j] = false;
				}
				else {
					if (word.randomNumber[j] == word.randomNumber[i]) {
						word.next[j] = true;
					}
				}
			}
			word.Next = !(word.next.some(ele => ele == true))
		};
		document.getElementById('word' + i).innerHTML = word.word[word.randomNumber[i]];
		word.Next = false
	}
}