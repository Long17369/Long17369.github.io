function loadWord(){
	var request = new XMLHttpRequest();
	request.open('GET','./word/7.26.json');
	request.responseType='json';
	request.send();
	request.onload = function(){
		var word = request.response;
		showWord(word);
	};
}
function showWord(word){
	var Word = document.getElementById('word');
	var Creat;
	var words = word.word;
	for(var i in words){
		Creat = document.createElement('word'+i);
		Creat.append(words[i]);
		Word.append(Creat)
	};
}