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
if (who == 'main') { newGetDate() };
if (who == 'history') { };
if (who == 'all') { };
function showword() {
	if (who == 'main') {
		action2.style.display = 'none';
		wordCard.style.display = '';
		console.log('载入单词' + who);
		loadWord();
		waitWordload(Next, 'reset');
	};
};
function waitWordload(fun, await1, await2, await3) {
	if (word.Version.time == undefined) {
		setTimeout(() => {
			waitWordload(fun, await1, await2, await3);
		}, 10);
	}
	else {
		fun(await1, await2, await3)
	};
};
function waitPosload(fun, await1, await2, await3) {
	if (!(word.word[count] in pos)) {
		setTimeout(() => {
			waitPosload(fun, await1, await2, await3);
		}, 10);
	}
	else {
		fun(await1, await2, await3);
	};
};
function Next(info) {
	if (info == "reset") {
		count = 0;
	}
	else if (info == 'next') {
		count++;
	};
	word.understand[count] = true
	next(info);
};
function next(info) {
	if (info == 'reset') {
		var SetCount = document.getElementById('Count');
		SetCount.innerText = (word.word.length);
	}
	else {
		if (count == word.word.length) {
			return End()
		};
	}
	var setcount = document.getElementById('count');
	setcount.innerText = (count + 1);
	var SetWord = document.getElementById('Word');
	SetWord.innerText = word.word[count];
	Chinese = false
	waitPosload(show_pos)
};
function show_pos() {
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
	};
};
function loadWord() {
	{
		if (who == 'main') {
			var date = word.date[word.date.length - 1]
			var open = `./每日单词/${date}`;
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
		}
		else if (word.Version.time != date) {
			console.log('载入日期不正确');
			console.log(`实际日期：${date}`);
			console.log(`错误日期：${word.Version.time}`);
		};
		console.log('main载入成功');
		loadpos();
	};
};
function loadpos() {
	for (info in word.word) {
		// pos.pos[word.word[info]] = false;
		load_pos(word.word[info]);
	};
};
function load_pos(info) {
	var open = `./word/synonym/${info}.json`;
	var request = new XMLHttpRequest();
	request.open('GET', open);
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		pos[info] = request.response;
		if (pos[info] == null) {
			console.log(`单词：${info} 载入失败`);
			loaderroe_pos(1, info);
		}
		else {
			console.log(`单词：${info} 载入成功`);
			// pos.pos[info] = true;
		};
	};
};
function getDate() {
	var date = new Date();
	var strDate = date.getDate();
	var nowMonth = date.getMonth() + 1;
	var nowDate = nowMonth + '.' + strDate;
	return nowDate;
};
function loaderroe(errorcount) {
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
			return loaderroe(errorcount);
		}
		else if (word.Version.time != `${nowMonth}.${nowDate}`) {
			console.log('载入日期不正确');
			console.log(`实际日期：${nowMonth}.${strDate}`);
			console.log(`错误日期：${word.Version.time}`);
		};
		console.log('main载入成功');
		loadpos();
	};
};
function loaderroe_pos(errorcount, info) {
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
			loaderroe_pos(errorcount, info)
		}
		else {
			console.log(`单词：${info} 载入成功`);
			pos['载入状态'] = true
		};
	};
};
function showChinese() {
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
		show_pos();
	};
};
function end() {
	Word.style.display = 'none';
	action.style.display = 'none';
	pricing.style.display = 'none';
	var zxcvbbnmdahksj = document.getElementById('posTag');
	zxcvbbnmdahksj.innerText = `完成\n共重复${word.count}次`
};
function End() {
	for (i in word.understand) {
		if (word.understand[i]) {
			word.understanded['认识'].push(word.word[i]);
		}
		else {
			word.understanded['不认识'].push(word.word[i]);
		};
		word.understanded.finish &&= word.understand[i];
	};
	word.understand = [];
	if (word.understanded.finish) {
		end();
	}
	else {
		word.word = word.understanded['不认识'];
		word.understanded = { '认识': [], '不认识': [], 'finish': true };
		word.count++;
		Next('reset');
	};
};
function newGetDate() {
	var request = new XMLHttpRequest();
	request.open('GET', './每日单词/dir.json');
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		date = request.response
		Object.assign(word, { date, });
		console.log('日期载入成功');
		loadpos();
	};
}