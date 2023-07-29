function showword(who = 'main') {
	wordCard.style.display = '';
	var word = loadWord(who);
	return show(who, word);
}
function show(who, word) {
	var Word = document.getElementById('Word');
	var Creat;
	var words = word.word;
	Word.innerHTML = '';
}
function showWord(word, count) {

}

function loadWord(who) {
	if (who == 'main') {
		var date = getDate()
		var open = './每日单词/' + date + '.json'
	}
	else {
		if (who == 'history') {
			return history()
		}
		else {
			if (who == 'all') {
				return all()
			}
			else {
				return
			}
		}
	}
	var request = new XMLHttpRequest();
	request.open('GET', open);
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		var word = request.response;
		return word
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
	var date = new Date()
	var strDate = date.getDate()
	var nowMonth = date.getMonth() + 1
	var nowDate = nowMonth + '.' + strDate
	return nowDate
}
function showChinese() {

}
function showword() {
	showWord(loadWord())
}
