$(document).ready(function() {
  check_all_responded_boxes();
  score_all();
  $(".scorable:checkbox").click(function(){
    var container = $(this).closest('.response_container');
    score_me(container);
  });
});


var score_all = function () {
  var $containers = $('.response_container');
  $.each($containers, function (index, container) {
    score_me(container);
  });
}

var score_me = function (container) {
  var num_of_items = $('.scorable:checkbox', container).length;
  var num_of_items_checked = $('.scorable:checkbox:checked', container).length;
  $('.score span.total', container).html(num_of_items);
  $('.score span.ticked', container).html(num_of_items_checked);
}

var check_all_responded_boxes = function () {
  var $containers = $('.response_container');
  $.each($containers, function (index, container) {
    check_responded_boxes(container);
  });
}

var check_responded_boxes = function (container) {
  var response_item_ids = $('#response_item_ids', container).val();
  if (! response_item_ids)
    return;
  response_item_ids = response_item_ids.replace(']', '').replace('[', '').trim();
  if (! response_item_ids) {
    return;
  }
  response_item_ids = response_item_ids.split(',');

  response_item_ids.forEach(function (element, index, array) {
    $('.scorable#' + element.trim(), container).attr('checked', true);
  })
}