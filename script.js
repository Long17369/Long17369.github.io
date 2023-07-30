// Version : 1.0.1.06
// Date : 2023/07/30 12:57
// Author : Long17369
var word;
var wordL = true;
function showword(who) {
	action2.style.display = 'none';
	wordCard.style.display = '';
	console.log('载入单词' + who);
	sleep(who);
	setTimeout(() => {
		show(who);
	}, 1000);
};
function show(who) {
	var Word = document.getElementById('Word');
	var Creat;
	sleep(who);
	var words = word.word;
	Word.innerHTML = '';
};
function Next(info, who) {
	var count;
	if (info == "reset") {
		count = 0;
	}
	else if (info == 'next') {
		count += 1;
	};
	next(count, who, info);
};
function next(count, who, info) {
	sleep(who);
	if (info == 'reset') {
		var SetCount = document.getElementById('Count');
		SetCount.innerText = (word.word.length + 1);
	}
	else {
		var setcount = document.getElementById('count');
		setcount.innerText = (count + 1);
	};
	var SetWord = document.getElementById('Word');
	SetWord.innerText = word.word[count];
};
function showWord(count) {

};
function sleep(who) {
	if (wordL) {
		loadWord(who);
	};
};
function loadWord(who) {
	if (who == 'main') {
		var date = getDate();
		var open = './每日单词/' + date + '.json';
		console.log('main载入中');
	}
	else if (who == 'history') {
		return history();
	}
	else if (who == 'all') {
		return all();
	}
	else {
		console.log('载入失败');
		return
	};
	wordL = false;
	var request = new XMLHttpRequest();
	request.open('GET', open);
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		word = request.response;
		if (word == null) {
			console.log('main载入失败');
		}
		else {
			console.log('main载入成功');
		};
	};
};
// function showWord(word) {
// 	var Word = document.getElementById('word');
// 	var Creat;
// 	var words = word.word;
// 	Word.innerHTML = '';
// 	for (var i in words) {
// 		Creat = document.createElement('word' + i);
// 		Creat.append(words[i] + '\n');
// 		var Creat1 = document.createElement('div');
// 		Creat1.append(Creat);
// 		Word.append(Creat1);
// 	};
// };
function getDate() {
	var date = new Date();
	var strDate = date.getDate();
	var nowMonth = date.getMonth() + 1;
	var nowDate = nowMonth + '.' + strDate;
	return nowDate;
};
function showChinese() {

};
// function showword() {
// 	showWord(loadWord())
// }
