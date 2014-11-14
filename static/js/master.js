$(document).ready(function() {
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