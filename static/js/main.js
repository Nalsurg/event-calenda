(function () {
	"use strict";

	var treeviewMenu = $('.app-menu');

	// Toggle Sidebar Переключить боковую панель
	$('[data-toggle="sidebar"]').click(function(event) {
		event.preventDefault();
		$('.app').toggleClass('sidenav-toggled');
	});

	// Activate sidebar treeview toggle Активировать переключатель просмотра дерева боковой панели
	$("[data-toggle='treeview']").click(function(event) {
		event.preventDefault();
		if(!$(this).parent().hasClass('is-expanded')) {
			treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
		}
		$(this).parent().toggleClass('is-expanded');
	});

	// Set initial active toggle Установите начальный активный переключатель
	$("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

	//Activate bootstrip tooltips Активировать всплывающие подсказки начальной загрузки
	$("[data-toggle='tooltip']").tooltip();

})();
