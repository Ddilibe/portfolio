function openNav() {
	var jame = document.querySelector('.navigation');
	jame.setAttribute('style', "display: flex");
	jame.children[0].setAttribute('style', "display: flex");
	jame.children[1].setAttribute('style', "display: flex");
	var bounce = document.querySelector('.closebtn');
	var close = document.querySelector('.openbtn');
	close.setAttribute('style', 'display:none');
	bounce.setAttribute('style', "display:block");
}

function candid() {
	var jame = document.querySelector('.navigation');
	jame.setAttribute('style', "display: none");
	jame.children[0].setAttribute('style', "display: none");
	jame.children[1].setAttribute('style', "display: none");
	var bounce = document.querySelector('.openbtn');
	var close = document.querySelector('.closebtn');
	close.setAttribute('style', 'display:none');
	bounce.setAttribute('style', "display:block");
}
