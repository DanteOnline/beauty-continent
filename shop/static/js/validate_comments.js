$('document').ready(function(){
		$('#comment_form').validate(
		{
			//Правила
			rules:{
				"name":{ required:true, maxlength:40 },
				"email":{ required:true, email: true },
				"comment":{ required:true },
			},
			//Текста предупреждений
			messages:{
				"name":{ required:"<br/><span style='color:red;'>Пожалуйста введите своё имя</a>",
maxlength: "<br/><span style='color:red;'>Максимальное кол-во символов 40 единиц</a>" },
				"email":{ required:"<br/><span style='color:red;'>Пожалуйста укажите вашу почту</a>",
				email: "<br/><span style='color:red;'>Неверный адрес электронной почты</a>"},
				"comment":{required:"<br/><span style='color:red;'>Пожалуйста введите комментарий</a>"}
			},
			//Обработчик и отправка данных
			/*submitHandler: function(form){
				$(form).ajaxSubmit({
					target: '#result',
					success: function() {
						$('#FormBox').slideUp('fast');
					}
				});
			}*/


		})
	});