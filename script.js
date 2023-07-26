function loadWord(){
	var request = new XMLHttpRequest();
	request.open('GET','./word/7.26.json');
	request.responseType='json';
	request.send();
	request.onload = function(){
		var word = request.response;
		showWord(word);
	}
}
function showWord(word){
	var Word = document.getElementById('word');
	var strWord
	strWord = stringWord(word)
	Word.innerHTML=strWord;
}
function stringWord(word){
	var Word = word
}