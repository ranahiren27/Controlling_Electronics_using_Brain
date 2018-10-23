let dataset;
let data;

d3.csv("data.csv", function(_data){
   	dataset=_data;

	let attributes = Object.keys(dataset[0]);
	console.log(attributes);
   	console.log(dataset.length);
    console.log(attributes.length);

	data = new Array();
	for(let i=0; i<dataset.length; i++){
		data[i] = new Array();
	}
    for(let i=0; i<dataset.length; i++){
    	for(let j=1; j<attributes.length; j++){
    		data[i][j] = dataset[i][attributes[j]];
    	}
    }

    for(let i=0; i<data.length; i++){
    	for(let j=0; j<data[i].length; j++){
    		data[i][j] = parseFloat(data[i][j]);
    	}
    }


	let dataPointer = document.getElementById('main');
	let datas = "";
	let temp = Math.floor(Math.random())%100;
	for(let i=0; i<9; i++){	
		datas += "<input type='number' value="+data[temp][i+1]+" name='"+i+"'></br>";
	}
	console.table(data[temp]);
	dataPointer.innerHTML = datas;
});
// used setTimeout function to handle asynchronous nature
// setTimeout(
// 	function () {
// 		let attributes = Object.keys(dataset[0]);
// 		console.log(attributes);
// 	   	console.log(dataset.length);
// 	    console.log(attributes.length);

// 		data = new Array();
// 		for(let i=0; i<dataset.length; i++){
// 			data[i] = new Array();
// 		}
// 	    for(let i=0; i<dataset.length; i++){
// 	    	for(let j=1; j<attributes.length; j++){
// 	    		data[i][j] = dataset[i][attributes[j]];
// 	    	}
// 	    }

// 	    for(let i=0; i<data.length; i++){
// 	    	for(let j=0; j<data[i].length; j++){
// 	    		data[i][j] = parseFloat(data[i][j]);
// 	    	}
// 	    }
// 	}
// ,1000);

