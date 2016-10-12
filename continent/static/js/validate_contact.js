$('document').ready(function(){
		$('#form').validate(
		{
			//Правила
			rules:{
				"subject":{ required:true, maxlength:40 },
				"sender":{ required:true, email: true },
				"message":{ required:true },
			},
			//Текста предупреждений
			messages:{
				"subject":{ required:"<br/><span style='color:red;'>Пожалуйста введите тему сообщения</a>",
maxlength: "<br/><span style='color:red;'>Максимальное кол-во символов 40 единиц</a>" },
				"sender":{ required:"<br/><span style='color:red;'>Пожалуйста укажите вашу почту</a>",
				email: "<br/><span style='color:red;'>Неверный адрес электронной почты</a>"},
				"message":{required:"<br/><span style='color:red;'>Пожалуйста введите сообщение</a>"}
			},
			//Обработчик и отправка данных
			submitHandler: function(form){
				$(form).ajaxSubmit({
					target: '#result',
					success: function() {
						$('#FormBox').slideUp('fast');
					}
				});
			}


		})
	});