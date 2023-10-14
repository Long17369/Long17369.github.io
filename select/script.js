// Version : 1.1.0.10debuged
// Date : 2023/08/02 09:08
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
	}
};
var pos = {};
var count = 0;
var Chinese = false;
function showword(who) {
	if (who == 'main') {
		action2.style.display = 'none';
		wordCard.style.display = '';
		console.log('载入单词' + who);
		loadWord(who);
		waitWordload(who, Next, 'reset', who);
	};
};
function waitWordload(who, fun, await1, await2, await3) {
	if (word.Version.time == undefined) {
		setTimeout(() => {
			waitWordload(who, fun, await1, await2, await3);
		}, 10);
	}
	else {
		fun(who, await1, await2, await3)
	};
};
function waitPosload(who, fun, await1, await2, await3) {
	if (!(word.word[count] in pos)) {
		setTimeout(() => {
			waitPosload(who, fun, await1, await2, await3);
		}, 10);
	}
	else {
		fun(who, await1, await2, await3);
	};
};
// function show(who) {
// 	var Word = document.getElementById('Word');
// 	var Creat;
// 	sleep(who);
// 	var words = word.word;
// 	Word.innerHTML = '';
// };
function Next(who, info) {
	if (info == "reset") {
		count = 0;
	}
	else if (info == 'next') {
		count++;
	};
	word.understand[count] = true
	next(who, info);
};
function next(who, info) {
	// sleep(who);
	if (info == 'reset') {
		var SetCount = document.getElementById('Count');
		SetCount.innerText = (word.word.length);
	}
	else {
		if (count == word.word.length) {
			return End(who)
		};
	}
	var setcount = document.getElementById('count');
	setcount.innerText = (count + 1);
	var SetWord = document.getElementById('Word');
	SetWord.innerText = word.word[count];
	Chinese = false
	waitPosload(who, show_pos)
};
function show_pos(who) {
	var posTag = document.getElementById('posTag');
	if (word.word[count] in pos) {
		var pos_tag = pos[word.word[count]];
		if (pos_tag.length == 0) {
			posTag.innerText = '短语';
		}
		else {
			var pos__tag = [];
			for (p in pos_tag) {
				if (pos__tag.includes(pos_tag[p]['词性'][1])) { }
				else {
					pos__tag.push(pos_tag[p]['词性'][1]);
				};
			};
			var postag = pos__tag.join('/');
			posTag.innerText = postag;
		};
	}
	else {
		posTag.innerText = 'null';
		// setTimeout(() => {
		// 	show_pos(who)
		// }, 10);
	};
};
// function sleep(who) {
// 	if (word.word == []) {
// 		loadWord(who);
// 	}
// };
function loadWord(who) {
	{
		if (who == 'main') {
			var date = getDate(who);
			var open = `./每日单词/${date}.json`;
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
	};
	var request = new XMLHttpRequest();
	request.open('GET', open);
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		Object.assign(word, request.response);
		if (word.Version.time == undefined) {
			console.log('main载入失败');
			return loaderroe(who, 1)
		}
		else if (word.Version.time != date) {
			console.log('载入日期不正确');
			console.log(`实际日期：${date}`);
			console.log(`错误日期：${word.Version.time}`);
		};
		console.log('main载入成功');
		loadpos(who);
	};
};
function loadpos(who) {
	for (info in word.word) {
		// pos.pos[word.word[info]] = false;
		load_pos(who, word.word[info]);
	};
};
function load_pos(who, info) {
	var open = `./word/synonym/${info}.json`;
	var request = new XMLHttpRequest();
	request.open('GET', open);
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		pos[info] = request.response;
		if (pos[info] == null) {
			console.log(`单词：${info} 载入失败`);
			loaderroe_pos(who, 1, info);
		}
		else {
			console.log(`单词：${info} 载入成功`);
			// pos.pos[info] = true;
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
function getDate(who) {
	var date = new Date();
	var strDate = date.getDate();
	var nowMonth = date.getMonth() + 1;
	var nowDate = nowMonth + '.' + strDate;
	return nowDate;
};
function loaderroe(who, errorcount) {
	{
		if (who == 'main') {
			var asfghsa = 24 * 3600000 * errorcount
			var date = new Date(new Date().getTime() - asfghsa);
			var strDate = date.getDate();
			var nowMonth = date.getMonth() + 1;
			var open = `./每日单词/${nowMonth}.${strDate}.json`;
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
	};
	var request = new XMLHttpRequest();
	request.open('GET', open);
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		Object.assign(word, request.response);
		if (word.Version.time == undefined) {
			console.log('main载入失败');
			errorcount++;
			return loaderroe(who, errorcount);
		}
		else if (word.Version.time != `${nowMonth}.${nowDate}`) {
			console.log('载入日期不正确');
			console.log(`实际日期：${nowMonth}.${strDate}`);
			console.log(`错误日期：${word.Version.time}`);
		};
		console.log('main载入成功');
		loadpos(who);
	};
};
function loaderroe_pos(who, errorcount, info) {
	var open = `./word/synonym/${info}.json`;
	var request = new XMLHttpRequest();
	request.open('GET', open);
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		pos[info] = request.response;
		if (pos[info] == null) {
			console.log(`单词：${info} 载入失败`);
			errorcount++
			loaderroe_pos(who, errorcount, info)
		}
		else {
			console.log(`单词：${info} 载入成功`);
			pos['载入状态'] = true
		};
	};
};
function showChinese(who) {
	if (!Chinese) {
		var posTag = document.getElementById('posTag');
		if (pos[word.word[count]].length == 0) {
			posTag.innerText('短语暂缺翻译，请自行翻译');
		}
		else {
			var chineses = pos[word.word[count]];
			var chinese = [];
			for (i in chineses) {
				chinese[i] = chineses[i].Chinese;
			};
			var Chineses = chinese.join(';')
			posTag.innerText = `中文：${Chineses}`;
			word.understand[count] = false
		};
		Chinese = true;
	}
	else {
		Chinese = false;
		show_pos(who);
	};
};
// function showword() {
// 	showWord(loadWord())
// }
function select(who) {
    
}