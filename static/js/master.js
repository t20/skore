$(document).ready(function() {
  check_responded_boxes();
  score_me();
  $(".scorable:checkbox").click(function(){
    score_me();
  });
});

var score_me = function () {
  var num_of_items = $('.scorable:checkbox').length;
  var num_of_items_checked = $('.scorable:checkbox:checked').length;
  $('#score span.total').html(num_of_items);
  $('#score span.ticked').html(num_of_items_checked);
}

var check_responded_boxes = function () {
  var response_item_ids = $('#response_item_ids').val();
  if (! response_item_ids)
    return;
  response_item_ids = response_item_ids.replace(']', '').replace('[', '').trim().split(',');
  response_item_ids.forEach(function (element, index, array) {
    $('.scorable#' + element.trim()).attr('checked', true);
  })
}