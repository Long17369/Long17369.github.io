function loadWord() {
	var request = new XMLHttpRequest();
	var date = getDate()
	request.open('GET', './每日单词/'+date+'.json');
	request.responseType = 'json';
	request.send();
	request.onload = function () {
		var word = request.response;
		showWord(word);
	};
};
function showWord(word) {
	var Word = document.getElementById('word');
	var Creat;
	var words = word.word;
	Word.innerHTML = ''
	for (var i in words) {
		Creat = document.createElement('word' + i);
		Creat.append(words[i] + '\n');
		var Creat1 = document.createElement('div');
		Creat1.append(Creat);
		Word.append(Creat1);
	};
};
function getDate(){
	var date = new Date()
	var strDate = date.getDate()
	var nowMonth = date.getMonth()+1
	var nowDate = nowMonth + '.' + strDate
	return nowDate
}