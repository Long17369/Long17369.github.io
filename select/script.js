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
	},
	'Words':[]
};
$.ajax({
	type:"get", //使用get方式
	url: "../word/word.json", //json文件相对于这个HTML的路径
	dataType:"json",
	success:function(data) {
		word.Words = data
		for (const i in word.Words){
			for (const j in word.Words[i].word) {
				if (word.Words[i].word[j] in word.word){}
				else{
					word.word.push(word.Words[i].word[j])
				};
			};
		};
		//这个data就是json数据
	},
	error:function() {
		alert("请求失败");
	}
});
function select() {
	var randomNumber
	for (let i = 0; i < 10; i++) {
		randomNumber = Math.floor(Math.random() * word.word.length);
		document.getElementById('word'+i).innerHTML = word.word[randomNumber];
	}
}