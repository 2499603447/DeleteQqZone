/**
*打开空间主页，点到说说页面，F12打开审查元素，切换至Console，复制代码version 1.0回车，若version 1.0报错则切换至version 2.0
*/

//version 1.0
function deleteCurPageTalk(){
	let delay = 1000;
	let btnList = document.querySelector('#app_canvas_frame').contentWindow.document.querySelectorAll('.del_btn');
	btnList = Array.prototype.slice.call(btnList);
	btnList.forEach((ele,index)=>{
		setTimeout(()=>{
			ele.click();
			setTimeout(()=>{
				let btn = document.querySelector(".qz_dialog_layer_btn");
				//console.log(btn);
				//document.querySelector('#QM_Feeds_Iframe').contentWindow.document.querySelector('.arrow-down').click()
				//console.log(document.querySelector('#QM_Feeds_Iframe').contentWindow.document.querySelector('.arrow-down').click());
				btn.click();
			},500)
			
			
		},delay*index);
	})
}


deleteCurPageTalk();

//version 2.0
function deleteCurPageTalk(){
	let delay = 1000;
	let btnList = document.querySelector('.mod_wrap_iframe').children[0].contentWindow.document.querySelectorAll('.del_btn');
	btnList = Array.prototype.slice.call(btnList);
	btnList.forEach((ele,index)=>{
		setTimeout(()=>{
			ele.click();
			setTimeout(()=>{
				let btn = document.querySelector(".qz_dialog_layer_btn");
				//console.log(btn);
				//document.querySelector('#QM_Feeds_Iframe').contentWindow.document.querySelector('.arrow-down').click()
				//console.log(document.querySelector('#QM_Feeds_Iframe').contentWindow.document.querySelector('.arrow-down').click());
				btn.click();
			},500)
			
			
		},delay*index);
	})
}


deleteCurPageTalk();