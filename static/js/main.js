/* Mysql */
$("#database").on("click", "a", function(){

	var value = $(this).attr("value");
	var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

	$.ajax({
		url: "/mysql/listar/",
		type: "POST",
		data: { "csrfmiddlewaretoken": csrftoken , "value": value },
		dataType: "json",	  
	})

	.done(function(response){
		var res = response;
		var html = '<br>';
		for(var item in res){
			for(var i = 0; i < res[item].length; i++){
				html +='<a href="#" value="'+ res[item][i] +'">' + res[item][i] + '</a>';
				html +='<br>';
			}
			
		}	
		
		$("#db_m").html(value)
		$("#tables").html(html)
	});

	return false;

});	

$("#tables").on("click", "a", function(){

	var value = $(this).attr("value");
	var db = $("#db_m").text();
	var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

	$.ajax({
		url: "/mysql/listar/campos/",
		type: "POST",
		data: { "csrfmiddlewaretoken": csrftoken , "value": value, "db":db },
		dataType: "json",	  
	})

	.done(function(response){
		var res = response;
		
		var html = '<br>';
		for(var item in res){
			console.log(res[item][0]);
			html +='<div value="'+ item +'">' + item + ' , ' + res[item] + '</div>';
			html +='<br>';	
			/*for(var i = 0; i < res[item].length; i++){
				
			}*/
			
		}	
		
		$("#campos").html(html)
	});

	return false;

});	

$("#tables").on("click", "a", function(){

	var value = $(this).attr("value");
	var db = $("#db_m").text();
	var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

	$.ajax({
		url: "/mysql/listar/campos/nombres/",
		type: "POST",
		data: { "csrfmiddlewaretoken": csrftoken , "value": value, "db":db },
		dataType: "json",	  
	})

	.done(function(response){
		var res = response;
		
		var html = '<br>';
		for(var item in res){
			console.log(res[item][0]);
			html +='<div value="'+ item +'">' + res[item] + '</div>';
			html +='<br>';	
			
		}	
		
		$("#tables_nombre").html(html)
	});

	return false;

});

/* Postgres */

$("#database_p").on("click", "a", function(){

	var value = $(this).attr("value");
	var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

	$.ajax({
		url: "/postgres/listar/",
		type: "POST",
		data: { "csrfmiddlewaretoken": csrftoken , "value": value },
		dataType: "json",	  
	})

	.done(function(response){
		var res2 = response;
		var html = '<br>';
		for(var item in res2){
			for(var i = 0; i < res2[item].length; i++){
				html +='<a href="#" value="'+ res2[item][i] +'">' + res2[item][i] + '</a>';
				html +='<br>';
			}
			
		}	
		$("#db_p").html(value)
		$("#tables_p").html(html)
	});

	return false;

});	

$("#catalogo_p").on("click", "a", function(response){

	var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

	$.ajax({
		url: "/postgres/listar/catalogo",
		type: "GET",
		data: { "csrfmiddlewaretoken": csrftoken },
		dataType: "json",	  
	})

	.done(function(response){
		var res2 = response;
		var html = '';
		for(var item in res2){

			for(var i = 0; i < res2[item].length; i++){
				html +='<a href="#" value="'+ res2[item][i] +'">' + res2[item][i] + '</a>';
				html +='<br>';
			}
			
		}	
		
		$("#db_p").html('Catalogo postgres')
		$("#tables_p").html(html)
	});

	return false;

});

$("#tables_p").on("click", "a", function(){

	var value = $(this).attr("value");
	var db = $("#db_p").text();
	var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

	$.ajax({
		url: "/postgres/listar/campos/",
		type: "POST",
		data: { "csrfmiddlewaretoken": csrftoken , "value": value, "db":db },
		dataType: "json",	  
	})

	.done(function(response){
		var res = response;
		
		var html = '<br>';
		for(var item in res){
			console.log(res[item][0]);
			html +='<div value="'+ item +'">' + item + ' , ' + res[item] + '</div>';
			html +='<br>';	
			/*for(var i = 0; i < res[item].length; i++){
				
			}*/
			
		}	
		
		$("#campos_p").html(html)
	});

	return false;

});	

$("#tables_p").on("click", "a", function(){

	var value = $(this).attr("value");
	var db = $("#db_p").text();
	var csrftoken = $('[name="csrfmiddlewaretoken"]').val();

	$.ajax({
		url: "/postgres/listar/campos/nombres/",
		type: "POST",
		data: { "csrfmiddlewaretoken": csrftoken , "value": value, "db":db },
		dataType: "json",	  
	})

	.done(function(response){
		var res = response;
		
		var html = '<br>';
		for(var item in res){
			console.log(res[item][0]);
			html +='<div value="'+ item +'">' + res[item] + '</div>';
			html +='<br>';	
			
		}	
		
		$("#tables_nombre_p").html(html)
	});

	return false;

});





